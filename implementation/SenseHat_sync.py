import sqlite3
import time
import requests

DB_NAME = "sensor_data.db"
# Make sure to add the .json at the end of the URL for the REST API
FB_URL = "https://lab3-iot-communication-default-rtdb.firebaseio.com/readings.json"

def sync_to_cloud():
    while True:
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            
            # Get unsynced data
            cursor.execute("SELECT id, timestamp, temp, humidity, pressure FROM environment WHERE synced = 0")
            rows = cursor.fetchall()

            for row in rows:
                row_id, ts, temp, hum, press = row
                payload = {"ts": ts, "temp": temp, "hum": hum, "press": press}
                
                # Using your requests method
                r = requests.post(FB_URL, json=payload)
                
                if r.status_code == 200:
                    cursor.execute("UPDATE environment SET synced = 1 WHERE id = ?", (row_id,))
                    conn.commit()
                    print(f"Synced ID {row_id} successfully.")
            
            conn.close()
        except Exception as e:
            print(f"Sync failed: {e}")

        time.sleep(10) # Check for new local data every 10 seconds

if __name__ == "__main__":
    sync_to_cloud()