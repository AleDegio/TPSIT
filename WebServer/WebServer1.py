"""
Alessia De Giovannini
Web Server
"""
from flask import Flask, render_template, redirect, url_for, request
import sqlite3 
import socket

app = Flask(__name__)

def server():
    body = "username=MARIO&password=ROSSI"
    content_type="application/x-www-form-urlencoded",
    content_length=len(body)   

def validate(username, password):
    completion = False
    con = sqlite3.connect('static.db')
    #with sqlite3.connect('static/db.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT * FROM login")
    rows = cur.fetchall()
    for row in rows: 
        dbUser = row[0]
        dbPass = row[1]
        if dbUser == username:
            completion = check_password(dbPass, password)
    return completion

def check_password(hashed_password, user_password):
    return hashed_password == user_password

#decoratote 
@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion == False: 
            error = 'Credenziali Invalide. Perfavore riprovare'
        else: 
            return redirect(url_for('pagina2'))
    return render_template('index.html', error=error)

#decoratote 2
@app.route('/pagina2')
def index2(): 
    return "pagina secondaria"

if __name__ == "__main__":
    app.run(host="127.0.0.1")