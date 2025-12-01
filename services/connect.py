import psycopg2 #connection to postgresql
import traceback  #error and debug

def connect_to_db():  # Function to connect to the PostgreSQL database
    try:
        #create object of connect()
        conn = psycopg2.connect(
            dbname="hotel",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )
        print("Connected to the database successfully")
        return conn
    except psycopg2.Error as e:
        print(f"Unable to connect to the database: {e}")
        print(traceback.format_exc())
        return None        