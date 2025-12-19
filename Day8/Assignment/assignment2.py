import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="maneger",   # CHANGE THIS
        database="sunbeam_project"
    )
