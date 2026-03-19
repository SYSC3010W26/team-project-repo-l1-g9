import os
import time

print("--- HW-TEST 3: MIPI CSI-2 CAMERA MODULE ---")
test_file = "test_capture.jpg"

# Remove old test file if it exists
if os.path.exists(test_file):
    os.remove(test_file)

print("Capturing test frame...")
# Using libcamera-jpeg for modern Pi OS
result = os.system(f"libcamera-jpeg -o {test_file} -t 1000 --nopreview")

if result == 0 and os.path.exists(test_file) and os.path.getsize(test_file) > 0:
    print(f"RESULT: PASS. Image successfully captured. Size: {os.path.getsize(test_file)} bytes.")
else:
    print("RESULT: FAIL. Hardware did not capture image.")