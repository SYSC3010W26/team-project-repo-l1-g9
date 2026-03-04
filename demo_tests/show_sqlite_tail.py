import time, sqlite3

DB_FILE = "demo_greenhouse.db"
conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

while True:
    rows = cur.execute(
        "SELECT id, datetime(ts,'unixepoch'), temperature_c, humidity_pct FROM readings ORDER BY id DESC LIMIT 5"
    ).fetchall()

    print("\n--- Latest 5 rows ---")
    for r in rows:
        print(r)

    time.sleep(2)
