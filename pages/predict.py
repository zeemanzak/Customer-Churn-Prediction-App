import streamlit as st
import joblib 
import pandas as pd
import os 
import datetime

st.set_page_config(page_title="Predict", page_icon="",layout="wide")

@st.cache_resource(show_spinner="Model_loading")
def load_logistic_model():
    model = joblib.load("./models/logistic_model.pkl")
    return model

@st.cache_resource(show_spinner="Model_loading")
def load_svc_model():
    model = joblib.load("./models/svc_model.pkl")
    return model

def select_model():
    col1, col2 = st.columns(2)
    
    with col1:
        st.selectbox("select a model", options=[
            "Logistic Regression","SVC"],key="selected_model")
    with col2:
        pass
    if st.session_state ["selected_model"] == "Logistic Regression" :
       model = load_logistic_model()
    else :
        model = load_svc_model()
    
    encoder = joblib.load("./models/label_encoder.pkl")
    
    return model, encoder

if "prediction" not in st.session_state:
    st.session_state["prediction"] = None
if "probability" not in st.session_state:
    st.session_state["probability"] = None
    
def make_prediction(model,encoder):
    features = [
        st.session_state.get("gender"),
        st.session_state.get("SeniorCitizen"),
        st.session_state.get("Partner"),
        st.session_state.get("Dependents"),
        st.session_state.get("tenure"),
        st.session_state.get("PhoneService"),
        st.session_state.get("MultipleLines"),
        st.session_state.get("InternetService"),
        st.session_state.get("OnlineSecurity"),
        st.session_state.get("OnlineBackup"),
        st.session_state.get("DeviceProtection"),
        st.session_state.get("TechSupport"),
        st.session_state.get("StreamingTV"),
        st.session_state.get("StreamingMovies"),
        st.session_state.get("Contract"),
        st.session_state.get("PaperlessBilling"),
        st.session_state.get("PaymentMethod"),
        float(st.session_state.get("MonthlyCharges", 0)),  # Convert text input to float
        float(st.session_state.get("TotalCharges", 0))   
        ]
    
    feature_names = ["gender", "SeniorCitizen", "Partner", "Dependents", "tenure",
                      "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity",
                      "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV",
                      "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod",
                      "MonthlyCharges", "TotalCharges"]
    
    # Create a DataFrame
    df = pd.DataFrame(data=[features], columns=feature_names)  
     # Ensure the data is properly encoded
    df_encoded = pd.DataFrame(encoder.transform(df).toarray(), columns=encoder.get_feature_names_out())
    
    # Check the shape of df_encoded
    if df_encoded.shape[0] != 1:
        # Reshape if necessary
        df_encoded = df_encoded.reshape(1, -1)
    
    # Make prediction
    pred = model.predict(df_encoded)
    
    # Get probability
    probability = model.predict_proba(df_encoded)[0]
    
    # Update state
    st.session_state["prediction"] = pred[0]
    st.session_state["probability"] = probability
    
    return pred[0], probability
    # Reshape the encoded data if necessary (flatten it)
    # df_encoded = df_encoded.values.reshape(1, -1)
    # make prediction
    # pred = model.predict(df_encoded)
    # pred = int(pred[0])
    # prediction = encoder.inverse_transform([pred[0]])        
        # get probability
    # probability = model.predict_proba(df_encoded)[0]
        
    # update state
    # st.session_state["prediction"] = prediction[0]
    # st.session_state["probability"] = probability
        
    # return prediction[0], probability
    
    
def display_form():
        model, encoder = select_model()
         
        with st.form("input-features"):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write("### Personal Information")
                st.selectbox("Gender", options=["Male", "Female"], key="gender")
                st.selectbox("Senior Citizen",options=["Yes","No"],key="SeniorCitizen")
                st.selectbox("Partner", options=["Yes","No"], key="Partner")
                st.selectbox("Dependents",options=["Yes","No"], key="Dependents")
                
            with col2:
                st.write("### Account Information")
                st.number_input("Input Tenure (months)", min_value=0,  key="tenure")
                st.selectbox("Contract", options=["Month-to-month","One year","Two year",], key="Contract")
                st.selectbox("PaperlessBilling", options=["Yes","No"], key="PaperlessBilling")
                
            with col3:
                st.write("### Bill Information")
                st.text_input("Enter Monthly Charges (USD)", key="MonthlyCharges")
                st.text_input("Enter Total Charges (USD)", key="TotalCharges")
                st.selectbox("Select Payment Method", options=["Electronic check","Mailed check","Credit card"], key="PaymentMethod")
                
            with col4:
                st.write("### Service Details")
                st.selectbox("Phone Service", options=["Yes", "No"], key="PhoneService")
                st.selectbox("Multiple Lines", options=["Yes", "No"], key="MultipleLines")
                st.selectbox("Internet Service", options=["DSL", "Fiber optic", "No"], key="InternetService")
                st.selectbox("Online Security", options=["Yes", "No", "No internet service"],key="OnlineSecurity")
                st.selectbox("Online Backup", options=["Yes", "No", "No internet service"], key="OnlineBackup")
                st.selectbox("Device Protection", options=["Yes", "No", "No internet service"], key="DeviceProtection")
                st.selectbox("Tech Support", options=["Yes", "No", "No internet service"], key="TechSupport")
                st.selectbox("Streaming TV", options=["Yes", "No", "No internet service"], key="StreamingTV")
                st.selectbox("Streaming Movies", options=["Yes", "No", "No internet service"], key="StreamingMovies")
            
            st.form_submit_button("Make Prediction", on_click=make_prediction, kwargs={"model": model, "encoder": encoder})
            
display_form()
