import time, os, requests

DB = os.environ.get("FIREBASE_DB_URL")
if not DB:
    raise SystemExit("Set FIREBASE_DB_URL first: source demo_tests/env.sh")

PATH = "/commands/override.json"
last_ts = None

N = 10
received = 0
last_ts = None

while received < N:
    cmd = requests.get(DB + PATH, timeout=5).json() or {}
    ts = cmd.get("ts")
    if ts and ts != last_ts:
        last_ts = ts
        received += 1
        print(f"Node2 RECEIVED [{received}/{N}]:", cmd)
        print("Node2 ACTUATE:", "ON" if cmd.get("pump_enable") else "OFF")
    time.sleep(0.5)

print(f"\nSUMMARY: received={received}/{N}")
