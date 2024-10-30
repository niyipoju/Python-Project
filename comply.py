import mysql.connector
# Connect to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="folakemifasanya",
    database="classicmodels", 
    port=3306 
)
if connection.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect to database")