from flask import Flask, jsonify
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)

# Replace the following with your Azure MySQL database information
host = "myappstreamlit2112.mysql.database.azure.com"
user = "nguyenanhtien"
password = "1234560aA"
ssl_ca = "DigiCertGlobalRootCA.crt.pem"
database = "labdata"

# Connect to Azure MySQL server with SSL
def connect():
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            ssl_ca=ssl_ca,
            database=database
        )
        return connection

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

@app.route('/degree', methods=['GET'])
def get_degree_values():
    connection = connect()
    if not connection:
        return jsonify({"error": "Unable to connect to the database"}), 500

    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM degree")
        degree_values = cursor.fetchall()
        return jsonify(degree_values)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": "Unable to fetch data from the database"}), 500

    finally:
        cursor.close()
        connection.close()

@app.route('/timestamp', methods=['GET'])
def get_timestamp_values():
    connection = connect()
    if not connection:
        return jsonify({"error": "Unable to connect to the database"}), 500

    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM timestamp")
        timestamp_values = cursor.fetchall()
        return jsonify(timestamp_values)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": "Unable to fetch data from the database"}), 500

    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
