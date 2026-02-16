import mysql.connector
from mysql.connector import Error
import os
from config import DB_config

def get_connection():
    try:
        connection = mysql.connector.connect(**DB_config)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Erro ao contatar o Myslq: {e}")
        return None