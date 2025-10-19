import mysql.connector

try:
    
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="AYOUB2004"
    )
    cursor = connection.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"MySQL Error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()

