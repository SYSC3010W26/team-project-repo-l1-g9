import time, os, requests

DB = os.environ.get("FIREBASE_DB_URL")
if not DB:
    raise SystemExit("Set FIREBASE_DB_URL first (source demo_tests/env.sh)")

PATH = "/commands/override.json"
state = False

while True:
    state = not state
    payload = {
        "ts": time.time(),
        "pump_enable": state,
        "source": "gui_stub"
    }
    r = requests.put(DB + PATH, json=payload, timeout=5)
    print("GUI -> Firebase:", r.status_code, payload)
    time.sleep(5)
