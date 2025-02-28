import mysql.connector
# Connect to the MySQL database
connection = mysql.connector.connect(
     host="localhost", 
    user="your_username",
    password="", 
    database="mysql_02" 
)
# Check if the connection was successful
if connection.is_connected():
    print("Connected to MySQL database.")
else:
    print("Failed to connect to database.")