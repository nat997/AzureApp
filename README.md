# Azure MySQL Data Visualization

This project demonstrates how to set up a simple data visualization application using Streamlit, Flask, and Azure services. The project consists of two main components:

- **Backend:** A Flask API that connects to an Azure MySQL database and provides endpoints to fetch degree and timestamp data.

- **Frontend:** A Streamlit app that visualizes the data obtained from the Flask API.

## Project Structure

The project is organized into two folders:

- **backend:** Contains the Flask API code and Docker configuration.
- **frontend:** Contains the Streamlit app code and Docker configuration.

# DATABASE SET UP IF YOU WANT TO USE ON YOUR AZURE :

1.Create your MySQL database on Azure Portal 
2.Place yourself in backend folder : 
cd /Backend
3.Run the command to create database and tables:
python database.py

----------------------------

# Run the Docker container:

docker compose up --build

### For the report of this TP please view Azure TP.pdf 

# Streamlit Flask API with Azure MySQL Data Visualization

This project showcases a Streamlit and Flask-based web application for data visualization using data retrieved from an Azure MySQL database. The application is Dockerized and can be easily deployed on Azure.

## Features

- **Backend (Flask API):** Connects to an Azure MySQL database, providing endpoints to fetch degree and timestamp data.
  
- **Frontend (Streamlit App):** Visualizes data obtained from the Flask API.

- **Docker Compose:** Enables easy deployment of the entire application stack.

- **Azure Deployment:** The application is hosted on Azure for convenient access.

## Access the Live App

Visit [https://streamlitflaskapi2212.azurewebsites.net/](https://streamlitflaskapi2212.azurewebsites.net/) to access the live application.

## Local Development

To run the application locally, you can use Docker Compose. Follow these steps:

git clone https://github.com/your-username/your-repo.git
cd your-repo
   
Run Docker Compose:

bash
Copy code
docker-compose up
Access the application:

Streamlit App: http://localhost:8501
Flask API: http://localhost:5000

[Azure TP .pdf](https://github.com/nat997/AzureTP/files/13754335/Azure.TP.pdf)

