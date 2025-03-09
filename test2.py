import mysql.connector
import configparser

def connect_to_mysql(config_file="config.ini"):
    """Connects to MySQL using configuration from config_file."""
    config = configparser.ConfigParser()
    config.read(config_file)

    try:
        mydb = mysql.connector.connect(
            host=config["mysql"]["host"],
            user=config["mysql"]["user"],
            password=config["mysql"]["password"],
            database=config["mysql"]["database"]
        )
        cursor = mydb.cursor()
        return mydb, cursor
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None, None

def execute_query(cursor, query):
    """Executes a query and handles errors."""
    try:
        print(f"Executing query: {query}")
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
        return None

def close_connection(mydb, cursor):
    """Closes the database connection and cursor safely."""
    if cursor:
        cursor.close()
    if mydb:
        mydb.close()

if __name__ == "__main__":
    mydb, cursor = connect_to_mysql()

    if mydb and cursor:
        query = "SELECT * FROM your_table"  # Replace with your query
        results = execute_query(cursor, query)
        if results:
            for row in results:
                print(row)
        else:
            print("No data found for the query.")
        close_connection(mydb, cursor)
    else:
        print("Failed to connect to the MySQL database.")
