import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon=":map:")
st.markdown("**Data Page**")
import streamlit as st
import pandas as pd
import pyodbc
from dotenv import dotenv_values
import os

# Database connection
# load environment variable from .env file
environment_variables =dotenv_values('.env')
# Get the values for the credentials you set in the '.env' file
server = environment_variables.get("SERVER")
database = environment_variables.get("DATABASE")
username = environment_variables.get("UID")
password = environment_variables.get("PWD")

connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};MARS_Connection=yes;MinProtocolVersion=TLSv1.2;"
 
connection = pyodbc.connect(connection_string)
query="SELECT * FROM dbo.LP2_Telco_churn_first_3000"
data=pd.read_sql(query, connection)
data.head()

# Display sample data
st.write("Sample Data from the Database")
st.write(data.head())

# Allow user to filter numeric or categorical data
if st.checkbox("Show Numeric Features"):
    st.write(data.select_dtypes(include='number').head())
if st.checkbox("Show Categorical Features"):
    st.write(data.select_dtypes(include='object').head())