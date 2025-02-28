# import mysql.connector
# Connect to the MySQL database
connection = mysql.connector.connect(
    host="localhost", 
    user="", 
    password="folakemifasanya", 
    database="classicmodels", 
    port=3306 
)
if(connection.is_connected()):
    print("yes!! 08 is connected o!")
else:
    print("08 could not be connected")
    # requesting changes
