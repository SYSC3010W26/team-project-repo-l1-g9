import sqlite3
import time
from datetime import datetime
from sense_hat import SenseHat

# Configuration
DB_NAME = "sensor_data.db"
INTERVAL = 2  # seconds

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS environment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            temp REAL,
            humidity REAL,
            pressure REAL,
            synced INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def log_data():
    sense = SenseHat()
    init_db()
    
    print("Starting logger...")
    while True:
        # Read sensors
        t = sense.get_temperature()
        h = sense.get_humidity()
        p = sense.get_pressure()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Save to SQLite
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO environment (timestamp, temp, humidity, pressure)
            VALUES (?, ?, ?, ?)
        ''', (now, t, h, p))
        
        # Optional: Keep only last 30 days (approx 43,200 rows if 1min interval)
        cursor.execute('''
            DELETE FROM environment WHERE timestamp <= datetime('now', '-30 days')
        ''')
        
        conn.commit()
        conn.close()
        
        time.sleep(INTERVAL)

if __name__ == "__main__":
    log_data()