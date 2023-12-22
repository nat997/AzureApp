import streamlit as st
import pandas as pd
import requests

# Define the Flask API endpoints
degree_api_url = "http://127.0.0.1:5000/degree"
timestamp_api_url = "http://127.0.0.1:5000/timestamp"

# Fetch data from the API
degree_data = requests.get(degree_api_url).json()
timestamp_data = requests.get(timestamp_api_url).json()

# Convert data to Pandas DataFrames
degree_df = pd.DataFrame(degree_data)
timestamp_df = pd.DataFrame(timestamp_data)

# Streamlit app
st.title("Azure MySQL Data Visualization")

# Display degree data
st.subheader("Degree Data")
st.dataframe(degree_df)

# Display a line chart for degree values
st.subheader("Degree Line Chart")
st.line_chart(degree_df['value'])

# Display timestamp data
st.subheader("Timestamp Data")
st.dataframe(timestamp_df)

# Display a line chart for timestamp values
st.subheader("Timestamp Line Chart")
st.line_chart(timestamp_df['time'])
