from fastapi import FastAPI
import pyodbc
import os 

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello from Backend"}

conn_string = os.getenv("DB_CONNECTION_STRING")


conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=tcp:hellworld.database.windows.net,1433;"
    "Database=mydb;"
    "Uid=myadmin;"
    "Pwd=YourPassword123;"
    "Encrypt=yes;"
)

@app.get("/users")
def get_users():
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 10 name FROM users")
    rows = cursor.fetchall()
    return {"users": [r[0] for r in rows]}