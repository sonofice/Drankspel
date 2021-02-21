# Imports
import sqlite3

def create_table():
    conn = sqlite3.connect("playerdb.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exits Playerdata (Player VARCHAR(15), Score INTEGER)")
    conn.commit()
    conn.close()

def insert_name(Player):
    conn = sqlite3.conncect("playerdb.db")
    cur = conn.cursor()   
    cur.execute("INSERT INTO Playerdata")
    conn.commit()
    conn.close()

def insert_score(Score):
    conn = sqlite3.conncect("playerdb.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Playerdata VALUES(?,?)", (Player, Score))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("playerdb.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Playerdata")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(score):
    conn = sqlite3.connect("playerdb.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM score Where Player=?", (Player))

def update(score):
    conn = sqlite3.connect("playerdb.db")
    cur = conn.cursor()
    cur.execute("UPDATE Playerdata SET Score=? WHERE Player=?", (Score, Player))
    conn.commit()
    conn.close()