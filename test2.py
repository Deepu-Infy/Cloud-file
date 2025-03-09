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
    # ... (This function remains the same as in the previous response)

def close_connection(mydb, cursor):
    # ... (This function remains the same as in the previous response)

if __name__ == "__main__":
    mydb, cursor = connect_to_mysql()

    if mydb and cursor:
        results = execute_query(cursor, "SELECT * FROM your_table") # Replace with your query
        if results:
            for row in results:
                print(row)
        close_connection(mydb, cursor)
    else:
        print("Failed to connect to MySQL.")