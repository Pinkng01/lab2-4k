from flask import Flask
from flask import request
import requests
import sqlite3

DB_NAME = "app.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)



app=Flask(__name__)

@app.route("/", methods=["POST"])
def data_to_db():
    print(f"Content-Type: {request.headers.get('Content-Type')}")
    print(f"Raw data: {request.get_data()}")

    data = request.get_json(silent=True)
    if not data or "message" not in data:
        return {"error" : "invalid json or miison message key"}, 444
    text_message = data["message"]
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
                "INSERT INTO notes (message) VALUES (?)",
                (text_message,)
        )
    return {"status" : "NICE"}, 200

@app.route("/", methods=["GET"])
def hello_world():
    return "Hello world!"


if __name__ == '__main__':
    init_db()
    app.run(host = "127.0.0.1", port=8000, debug=True)

