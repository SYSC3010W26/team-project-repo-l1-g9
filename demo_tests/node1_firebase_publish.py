import time, os, requests, random

DB = os.environ.get("FIREBASE_DB_URL")  # ex: https://xxx-default-rtdb.firebaseio.com
if not DB:
    raise SystemExit("Missing FIREBASE_DB_URL. Example:\nexport FIREBASE_DB_URL='https://<project>.firebaseio.com'")

PATH = "/nodes/node1/climate.json"

while True:
    payload = {
        "ts": time.time(),
        "temperature_c": round(22 + random.random()*4, 2),
        "humidity_pct": round(40 + random.random()*20, 2),
        "source": "node1_stub"
    }
    r = requests.put(DB + PATH, json=payload, timeout=5)
    print("Node1 -> Firebase:", r.status_code, payload)
    time.sleep(2)
