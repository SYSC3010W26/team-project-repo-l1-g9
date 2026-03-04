import time, os, requests, random

DB = os.environ.get("FIREBASE_DB_URL")  # ex: https://xxx-default-rtdb.firebaseio.com
if not DB:
    raise SystemExit("Missing FIREBASE_DB_URL. Example:\nexport FIREBASE_DB_URL='https://<project>.firebaseio.com'")

PATH = "/nodes/node1/climate.json"

N = 10
success = 0

for i in range(N):
    payload = make_payload_somehow()  # keep your existing payload creation
    r = requests.put(DB + PATH, json=payload, timeout=5)
    ok = (r.status_code == 200)
    success += 1 if ok else 0
    print(f"Node1 -> Firebase [{i+1}/{N}]: {r.status_code}", payload)
    time.sleep(2)

print(f"\nSUMMARY: sent={N}, success={success}, fail={N-success}")
