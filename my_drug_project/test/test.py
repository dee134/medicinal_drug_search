import pyodbc

# Update with your connection string
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6ET4EQU\MSSQLSERVER01;DATABASE=Sample1;Trusted_Connection=yes;'

try:
    conn = pyodbc.connect(conn_str)
    print("Connection successful!")
    conn.close()
except pyodbc.Error as e:
    print(f"Error: {e}")
