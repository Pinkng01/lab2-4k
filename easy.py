"""
[Easy] Написати просту обробку запиту метода GET сервером.
На запит повертати строку “Hello World!” 
"""
from flask import Flask



app=Flask(__name__)
@app.route("/", method=["GET"])
def hello_world():
    return "Hello world!"

if __name__ == '__main__':
    app.run(host = "127.0.0.1", port=8000, debug=True)
