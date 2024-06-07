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

    # Create a new table
    create_table_query = """
    CREATE TABLE firstpostgrestable (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER
    )
    """
    cur.execute(create_table_query)
    print("Table 'firstpostgrestable created successfully!")

    # Insert data into the new table
    insert_data_query = """
    INSERT INTO firstpostgrestable (name,age) VALUES
    ('Alice',30),
    ('Bob',25),
    ('Charlie',35)
    """

    cur.execute(insert_data_query)
    print("Data inserted successfully!")

except Exception as e:
    print(f"Error:{e}")

finally:
    # Close the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()
