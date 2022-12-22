import sqlite3

def execute_query(query_file):
    # Connect to the database
    conn = sqlite3.connect('../risk-system-db/stable.db')

    # Create a cursor
    cursor = conn.cursor()

    # Read the .sql file
    with open(query_file, 'r') as f:
        query = f.read()

    # Execute the query
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    return results