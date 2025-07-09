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
    # 1-10  ───────── India
    ("Virat Kohli",        "India",       "Batter",       27599,   9),   # :contentReference[oaicite:0]{index=0}
    ("Rohit Sharma",       "India",       "Batter",       19700,  12),   # :contentReference[oaicite:1]{index=1}
    ("Ravindra Jadeja",    "India",       "All-rounder",   6691, 608),   # :contentReference[oaicite:2]{index=2}
    ("Jasprit Bumrah",     "India",       "Bowler",         431, 443),   # :contentReference[oaicite:3]{index=3}
    ("KL Rahul",           "India",       "WK-Batter",     4506,   1),   # infobox 6 Jul 2025
    ("Hardik Pandya",      "India",       "All-rounder",   4248, 202),   # :contentReference[oaicite:4]{index=4}
    ("Shubman Gill",       "India",       "Batter",        4335,   4),   # ICC records, Jul 2025
    ("Rishabh Pant",       "India",       "WK-Batter",     4143,   3),   # ICC records, Jul 2025
    ("Kuldeep Yadav",      "India",       "Bowler",         224, 319),   # ICC records, Jul 2025
    ("Mohammed Siraj",     "India",       "Bowler",         171, 203),   # ICC records, Jul 2025

    # 11-16 ───────── Australia
    ("Steven Smith",       "Australia",   "Batter",       17318,  64),   # :contentReference[oaicite:5]{index=5}
    ("David Warner",       "Australia",   "Batter",       18995,   4),   # :contentReference[oaicite:6]{index=6}
    ("Mitchell Starc",     "Australia",   "Bowler",        2986, 718),   # :contentReference[oaicite:7]{index=7}
    ("Pat Cummins",        "Australia",   "Bowler",        2193, 513),   # :contentReference[oaicite:8]{index=8}
    ("Glenn Maxwell",      "Australia",   "All-rounder",   6993, 128),   # :contentReference[oaicite:9]{index=9}
    ("Travis Head",        "Australia",   "Batter",        7104,  30),   # ICC records, Jul 2025

    # 17-22 ───────── England
    ("Joe Root",           "England",     "Batter",       20213,  99),   # :contentReference[oaicite:10]{index=10}
    ("Ben Stokes",         "England",     "All-rounder",  10829, 318),   # :contentReference[oaicite:11]{index=11}
    ("Jonny Bairstow",     "England",     "WK-Batter",    11581,   0),   # :contentReference[oaicite:12]{index=12}
    ("Moeen Ali",          "England",     "All-rounder",   6678, 366),   # :contentReference[oaicite:13]{index=13}
    ("Jofra Archer",       "England",     "Bowler",         399, 137),   # :contentReference[oaicite:14]{index=14}
    ("Mark Wood",          "England",     "Bowler",         528, 257),   # ICC records, Jul 2025

    # 23-26 ───────── New Zealand
    ("Kane Williamson",    "New Zealand", "Batter",       19086,  73),   # :contentReference[oaicite:15]{index=15}
    ("Trent Boult",        "New Zealand", "Bowler",         759, 611),   # :contentReference[oaicite:16]{index=16}
    ("Tim Southee",        "New Zealand", "Bowler",        3288, 776),   # :contentReference[oaicite:17]{index=17}
    ("Daryl Mitchell",     "New Zealand", "All-rounder",   5021,  55),   # NZC stats, Jul 2025

    # 27-30 ───────── Pakistan / S Africa / Sri Lanka
    ("Babar Azam",         "Pakistan",    "Batter",       12558,   1),   # PCB stats, Jul 2025
    ("Shaheen Afridi",     "Pakistan",    "Bowler",         330, 305),   # PCB stats, Jul 2025
    ("Kagiso Rabada",      "South Africa","Bowler",        1161, 457),   # CSA stats, Jul 2025
    ("Wanindu Hasaranga",  "Sri Lanka",   "All-rounder",   2154, 217)    # SLC stats, Jul 2025
]


cursor.executemany(insert_sql, players)
connection.commit()

data=cursor.execute("""SELECT * FROM CRICKETER""")

for row in data:
    print(row)

if connection:
    connection.close()