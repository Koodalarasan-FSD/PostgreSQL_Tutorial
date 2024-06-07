import psycopg2
from psycopg2 import sql

# Define the connection parameters
host = "127.0.0.1"
port = "5432"
user = "postgres"
password = "admin@123"

# Initialize connection and cursor to None
conn = None
cur = None

# Connect to the PostgreSQL server
try:
    # Connect to the default database (usually "postgres")
    conn = psycopg2.connect(dbname="postgres", user=user,
                            password=password, host=host, port=port)
    conn.autocommit = True  # Enable autocommit mode
    cur = conn.cursor()

    # Define the new database name
    new_database_name = "firstpostgresdatabase"

    # Create the new database
    cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_database_name)))
    print(f"Database '{new_database_name}' created successfully!")

except Exception as e:
    print(f"Error:{e}")

finally:
    # Close the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()