import time, requests

URL = "http://127.0.0.1:5000/status"

while True:
    try:
        r = requests.get(URL, timeout=3)
        print("Flask /status:", r.status_code, r.text)
    except Exception as e:
        print("Flask poll error:", e)
    time.sleep(2)
