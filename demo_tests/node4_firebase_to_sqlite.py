import os, time, sqlite3, requests

DB = os.environ.get("FIREBASE_DB_URL")
PATH = "/nodes/node1/climate.json"
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

N = 10
logged = 0

while logged < N:
    data = requests.get(DB + PATH, timeout=5).json() or {}
    ts = data.get("ts")
    if ts and ts != last_ts:
        last_ts = ts
        # your existing sqlite insert here
        logged += 1
        print(f"SQLite LOGGED [{logged}/{N}]:", data)
    time.sleep(0.5)

print(f"\nSUMMARY: logged={logged}/{N}")
