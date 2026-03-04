import os, time, sqlite3, requests

DB = os.environ.get("FIREBASE_DB_URL")
if not DB:
    raise SystemExit("Missing FIREBASE_DB_URL")

CLIMATE_PATH = "/nodes/node1/climate.json"

conn = sqlite3.connect("demo_greenhouse.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS readings (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ts REAL,
  temperature_c REAL,
  humidity_pct REAL,
  source TEXT
)
""")
conn.commit()

last_ts = None

while True:
    data = requests.get(DB + CLIMATE_PATH, timeout=5).json() or {}
    ts = data.get("ts")
    if ts and ts != last_ts:
        last_ts = ts
        cur.execute(
            "INSERT INTO readings(ts, temperature_c, humidity_pct, source) VALUES (?,?,?,?)",
            (ts, data.get("temperature_c"), data.get("humidity_pct"), "firebase")
        )
        conn.commit()
        print("SQLite LOGGED:", data)

    time.sleep(1)
