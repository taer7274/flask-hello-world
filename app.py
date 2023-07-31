from flask import Flask
import psycopg2

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://lab10_taer7274_user:HvgBKbFlikKwyGBEJ8wwBJ8tIsmazVRQ@dpg-cj4348d9aq047ca2h2dg-a/lab10_taer7274")
    conn.close()
    return "Database Connection Successful"


@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgres://lab10_taer7274_user:HvgBKbFlikKwyGBEJ8wwBJ8tIsmazVRQ@dpg-cj4348d9aq047ca2h2dg-a/lab10_taer7274")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
       ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

