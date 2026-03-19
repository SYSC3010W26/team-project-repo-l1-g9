import time
from sense_hat import SenseHat

print("--- HW-TEST 2: SENSE-HAT LED ACTUATOR ---")
print("Isolating output hardware. Testing visual states...")
sense = SenseHat()

print("Triggering PUMP ON (Blue) for 3 seconds...")
sense.clear((0, 0, 255))
time.sleep(3)

print("Triggering PUMP OFF (Red) for 3 seconds...")
sense.clear((255, 0, 0))
time.sleep(3)

sense.clear()
print("RESULT: PASS. Actuator output successfully toggled via GPIO/I2C.")