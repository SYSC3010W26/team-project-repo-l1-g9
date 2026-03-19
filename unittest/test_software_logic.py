import unittest
import sqlite3
import os

# --- MOCK LOGIC TO TEST ---
# (In a real app, you would import these from your main files, 
# but we define them here to guarantee isolation for the unit test).

def decide_pump_state(soil_moisture):
    """Returns True (ON) if moisture < 30, else False (OFF)."""
    if soil_moisture < 30:
        return True
    return False

def format_climate_payload(temp, hum):
    """Ensures data is formatted correctly before sending to cloud."""
    return {"temperature_c": temp, "humidity_pct": hum, "source": "node1"}

# --- THE AUTOMATED TEST SUITE ---
class TestGreenhouseSoftware(unittest.TestCase):

    def test_irrigation_threshold_logic(self):
        """SW-TEST 1: Verify pump logic acts correctly on boundaries."""
        print("\nRunning SW-TEST 1: Irrigation Logic...")
        self.assertTrue(decide_pump_state(15), "Failed: Pump should be ON at 15% moisture")
        self.assertTrue(decide_pump_state(29), "Failed: Pump should be ON at 29% moisture")
        self.assertFalse(decide_pump_state(30), "Failed: Pump should be OFF at 30% moisture")
        self.assertFalse(decide_pump_state(50), "Failed: Pump should be OFF at 50% moisture")

    def test_payload_formatting(self):
        """SW-TEST 2: Verify JSON payload formatting."""
        print("\nRunning SW-TEST 2: Payload Formatting...")
        payload = format_climate_payload(24.5, 55.2)
        self.assertEqual(payload["temperature_c"], 24.5)
        self.assertEqual(payload["source"], "node1")

    def test_sqlite_database_insertion(self):
        """SW-TEST 3: Verify local DB logging in memory (No actual file created)."""
        print("\nRunning SW-TEST 3: SQLite Database Operations...")
        # Use an in-memory database for pure unit testing (no file mess)
        conn = sqlite3.connect(':memory:')
        cur = conn.cursor()
        cur.execute("CREATE TABLE readings (id INTEGER PRIMARY KEY, ts REAL, temp REAL, hum REAL)")
        
        # Test Insertion
        cur.execute("INSERT INTO readings (ts, temp, hum) VALUES (?, ?, ?)", (1600000000.0, 22.5, 45.0))
        conn.commit()
        
        # Test Retrieval
        cur.execute("SELECT * FROM readings")
        row = cur.fetchone()
        
        self.assertIsNotNone(row, "Failed: Database returned no rows")
        self.assertEqual(row[2], 22.5, "Failed: Temperature mismatch in DB")
        self.assertEqual(row[3], 45.0, "Failed: Humidity mismatch in DB")
        conn.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)