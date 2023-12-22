import mysql.connector
from mysql.connector import errorcode
import random
from datetime import datetime, timedelta

host = "myappstreamlit2112.mysql.database.azure.com"
user = "nguyenanhtien"
password = "1234560aA"
ssl_ca = "DigiCertGlobalRootCA.crt.pem"

# Connect to MySQL server with SSL
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        ssl_ca=ssl_ca
    )
    print("Connected to MySQL server successfully!")

    cursor = connection.cursor()

    # Create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS labdata")
    print("Database 'labdata' created successfully!")

    cursor.execute("USE labdata")

    # Create the 'degree' table
    cursor.execute("CREATE TABLE IF NOT EXISTS degree (id INT AUTO_INCREMENT PRIMARY KEY, value FLOAT)")
    print("Table 'degree' created successfully!")

    # Insert random values into the 'degree' table
    for _ in range(10):
        random_value = random.uniform(0, 100)
        cursor.execute("INSERT INTO degree (value) VALUES (%s)", (random_value,))
    print("Random values inserted into 'degree' table.")

    # Create the 'timestamp' table
    cursor.execute("CREATE TABLE IF NOT EXISTS timestamp (id INT AUTO_INCREMENT PRIMARY KEY, time TIMESTAMP)")
    print("Table 'timestamp' created successfully!")

    # Insert random timestamps into the 'timestamp' table
    for _ in range(10):
        random_time = datetime.now() - timedelta(days=random.randint(1, 365))
        cursor.execute("INSERT INTO timestamp (time) VALUES (%s)", (random_time,))
    print("Random timestamps inserted into 'timestamp' table.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Invalid credentials")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: Database does not exist")
    elif err.errno == 3159:
        print("Error: Insecure transport. Use SSL for a secure connection.")
    else:
        print(f"Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.commit()  # Commit the changes
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
