import sqlite3, time, requests

DB_URL = "https://lab3-iot-communication-default-rtdb.firebaseio.com"
conn = sqlite3.connect("greenhouse.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS readings (id INTEGER PRIMARY KEY, ts REAL, temp REAL, hum REAL)")

last_ts = None
print("Node 4: Central Logger Started...")

while True:
    try:
        # Fetch the very last reading from Firebase
        r = requests.get(f"{DB_URL}/nodes/node1/climate.json?orderBy=\"$key\"&limitToLast=1")
        data = r.json()
        
        if data:
            push_id = list(data.keys())[0]
            val = data[push_id]
            
            if val['ts'] != last_ts:
                cur.execute("INSERT INTO readings (ts, temp, hum) VALUES (?, ?, ?)", 
                            (val['ts'], val['temperature_c'], val['humidity_pct']))
                conn.commit()
                last_ts = val['ts']
                print(f"Logged to SQLite DB -> Temp: {val['temperature_c']}C | Hum: {val['humidity_pct']}%")
    except Exception as e:
        pass
    time.sleep(5)