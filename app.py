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

@app.route('/db_insert')
def db_insert():
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
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Populated"


@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgres://lab10_taer7274_user:HvgBKbFlikKwyGBEJ8wwBJ8tIsmazVRQ@dpg-cj4348d9aq047ca2h2dg-a/lab10_taer7274")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Basketball;")
    returned_records = cur.fetchall()
    conn.close()
    ret_string = "<table>"
    for player in returned_records:
        ret_string += "<tr>"
        for details in player:
            ret_string += f"<td>{details}</td>"
        ret_string += "</tr>"
    ret_string += "</table>"
    return ret_string

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect("postgres://lab10_taer7274_user:HvgBKbFlikKwyGBEJ8wwBJ8tIsmazVRQ@dpg-cj4348d9aq047ca2h2dg-a/lab10_taer7274")
    cur = conn.cursor()
    cur.execute("DROP TABLE Basketball")
    conn.commit()
    conn.close()
    return "Basketball Table Dropped"

