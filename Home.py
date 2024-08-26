import streamlit as st

# set pages configuration
st.set_page_config(
    page_title="Churn Prediction APP",
    page_icon=":hand:",
    layout="wide"
)
st.title("*Welcome to Customer Churn Prediction App*")
st.markdown("""
    A Customer Churn Prediction App is a tool designed to help businesses identify customers who are likely to stop using their products or services. 
    By analyzing various customer data points, the app predicts which customers are at risk of churn, allowing companies to take proactive measures to retain them.
            """)



# key features
st.subheader(
    "key Features"
)
st.markdown( """
   -Upload your CSV file containing the customers details
   -Select the desired features for classification
   -Choose a machine learning model from the dropdown menu
   -Click classify to get the predicted result  
   -The app provides a detailed result of the performance of the model 
   -The result include metrics like accuracy,precision,recall,and f1-score*    
            """)
# menu
st.subheader("App Features")
st.markdown("""
        - **view Data** : Access proprietary data
        - **Dashboard** : Explore inactive data visualization for insights
        - **Predict** : Make prediction whether or not a customer is likely to churn    
            """)


# Machine Learning Integration
st.subheader("Machine Learning Integration")
st.markdown("""
        - **Model Selection**: choose between two advanced models for accurate Classification.
        - **Seamless Integration**: Integrate predicitions into your workflow with a user-friendly interface. 
        - **Probability Estimate**: Gain insight into the likelihood of Predicted outcomes.
            """)


# Contact and Github Repository
st.subheader("Need help")
st.markdown("for collaboration contact me [assayoutiopeyemi@gmail.com]")
st.button("Repository on Github",help="visit the github repo")
