import time, os, requests, random

DB = os.environ.get("FIREBASE_DB_URL")  # ex: https://xxx-default-rtdb.firebaseio.com
if not DB:
    raise SystemExit("Missing FIREBASE_DB_URL. Example:\nexport FIREBASE_DB_URL='https://<project>.firebaseio.com'")

PATH = "/nodes/node1/climate.json"

N = 10
success = 0

for i in range(N):
    payload = {
    "ts": time.time(),
    "temperature_c": round(random.uniform(22.0, 26.0), 2),
    "humidity_pct": round(random.uniform(40.0, 60.0), 2),
    "source": "node1_stub"
}
    r = requests.put(DB + PATH, json=payload, timeout=5)
    ok = (r.status_code == 200)
    success += 1 if ok else 0
    print(f"Node1 -> Firebase [{i+1}/{N}]: {r.status_code}", payload)
    time.sleep(2)

print(f"\nSUMMARY: sent={N}, success={success}, fail={N-success}")
