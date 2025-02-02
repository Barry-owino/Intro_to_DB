import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (without specifying database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#####'  
        )
        
        if connection.is_connected():
            print("Connected to MySQL Server successfully!")
            
            # Create a cursor object
            cursor = connection.cursor()
            
            # Create the database if it does not already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            # Commit the changes
            connection.commit()
            print("Database 'alx_book_store' created successfully!")
            
            # Close the cursor and connection
            cursor.close()
            connection.close()

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        if connection.is_connected():
            connection.close()
            print("Connection closed due to error.")

# Call the function to create the database
create_database()

