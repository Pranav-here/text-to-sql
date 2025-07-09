import sqlite3

# Connect (creates DB file if it doesn’t exist)
connection = sqlite3.connect("cricket.db")
cursor = connection.cursor()

# Define the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS CRICKETER (
        PLAYER_NAME TEXT,
        TEAM        TEXT,
        ROLE        TEXT,   -- e.g. Batsman, Bowler, All-rounder
        RUNS        INTEGER,
        WICKETS     INTEGER
    );
""")

# Seed it with some sample data
insert_sql = """
    INSERT INTO CRICKETER (PLAYER_NAME, TEAM, ROLE, RUNS, WICKETS)
    VALUES (?,?,?,?,?)
"""

players = [
    ("Virat Kohli",     "India",   "Batsman",    12000,   4),
    ("Mitchel Starc",  "Australia",   "Bowler",        1500, 750),
    ("Ben Stokes",      "England", "All-rounder",  5500, 200)
]

cursor.executemany(insert_sql, players)
connection.commit()

data=cursor.execute("""SELECT * FROM CRICKETER""")

for row in data:
    print(row)

if connection:
    connection.close()