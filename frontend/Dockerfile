# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app/frontend

# Copy the current directory contents into the container at /app
COPY . /app/frontend

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8501

# Run streamlit_app.py when the container launches
CMD ["streamlit", "run", "streamlit_app.py"]
