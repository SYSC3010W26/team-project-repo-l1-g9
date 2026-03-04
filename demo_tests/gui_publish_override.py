import time, os, requests

DB = os.environ.get("FIREBASE_DB_URL")
if not DB:
    raise SystemExit("Set FIREBASE_DB_URL first (source demo_tests/env.sh)")

PATH = "/commands/override.json"
state = False

N = 10
success = 0
state = False

for i in range(N):
    state = not state
    payload = {"ts": time.time(), "pump_enable": state, "source": "gui_stub"}
    r = requests.put(DB + PATH, json=payload, timeout=5)
    ok = (r.status_code == 200)
    success += 1 if ok else 0
    print(f"GUI -> Firebase [{i+1}/{N}]: {r.status_code}", payload)
    time.sleep(2)

print(f"\nSUMMARY: sent={N}, success={success}, fail={N-success}")
