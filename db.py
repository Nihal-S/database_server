from flask import Flask, render_template, request, jsonify
import json
import requests
import sqlite3
import string
import datetime
app = Flask(__name__)

@app.route('/api/v1/read',methods=['GET'])
def read():
    conn = sqlite3.connect('parking.db')
    c = conn.cursor()
    table = request.json['table']
    columns = request.json['columns']
    where = request.json['where']
    query = "SELECT "+columns+" FROM "+table+" WHERE "+where
    c.execute(query)
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return json.dumps(rows)

@app.route('/api/v1/write', methods=['POST'])
def write_db():
    conn = sqlite3.connect('parking.db')
    c = conn.cursor()
    data = request.json['insert']
    column = request.json['column']
    table = request.json['table']
    what = request.json['what']
    if(what == "delete"):
        print("deleting")
        print(data)
        query = "DELETE FROM "+table+" where "+data
    else:
        print("inserting")
        query = "INSERT INTO "+table+" ("+column+") "+"VALUES ("+data+")"
    c.execute(query)
    conn.commit()
    conn.close()
    res = jsonify()
    return res, 201

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port = 12345)