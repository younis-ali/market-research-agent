import psycopg2
import json

class DBClient:
    # Constructor to crate the database connection and cursor 
    def __init__(self, config_path):
        with open(config_path, "r") as file:
            self.database_config = json.load(file)
            # print(self.database_config)

    # Function to connect to the database
    def connect(self):    
        try:
            self.connection = psycopg2.connect(
                user=self.database_config['user'],
                password=self.database_config['password'],
                host=self.database_config['host'],
                port=self.database_config['port'],
                database=self.database_config['database']
            )

            self.cursor = self.connection.cursor()
            print('CONNECTED TO DATABASE')
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
    
    # Fucntion to close the connection to the postgress database

    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")
    
    
    # Execute the query 
    def execute_query(self, query):
        if not self.connection:
            self.connect()
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
                
        except psycopg2.Error as error:
            print("Error executing query:", error)

        self.close_connection()
    