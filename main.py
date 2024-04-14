import sqlite3
from flask import Flask, request
import json

app = Flask(__name__)

con = sqlite3.connect("users.db")

cur = con.cursor
cur.execute("CREATE TABLE users(username, password, salt)")


@app.route("/sign-up", methods = ['POST'] )  
def sign_up():
    global cur
    req = request.get_json()
    dic = json.loads(req)
    username = dic["username"]
    pw = dic["password"]
    cur.execute(f"INSERT INTO users (username, password) VALUES ({username}, {password})")
    return req
