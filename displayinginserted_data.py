import psycopg2
from psycopg2 import sql

# Define the connection parameters
host = "127.0.0.1"
port = "5432"
user = "postgres"
password = "admin@123"
database = "firstpostgresdatabase"

# Initialize connection and cursor to None
conn = None
cur = None

# Connect to the PostgreSQL server
try:
    # Connect to the new database
    conn = psycopg2.connect(dbname=database, user=user,
                            password=password, host=host, port=port)
    conn.autocommit = True  # Enable autocommit mode
    cur = conn.cursor()

    # Retrieve data from the table
    retrieve_data="SELECT * FROM firstpostgrestable"
    cur.execute(retrieve_data)
    # Fetch all rows from the executed query
    rows = cur.fetchall()

    print("Data retrived from table 'firstpostgrestable':")
    for row in rows:
        print(row)

except Exception as e:
    print(f"Error:{e}")

finally:
    # Close the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()
