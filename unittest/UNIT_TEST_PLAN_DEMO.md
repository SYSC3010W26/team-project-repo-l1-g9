# SYSC3010: Unit Test Demo Plan
**Group:** L1-G9  
**Goal:** Verify and validate the correct operation of individual software and hardware components *independent* of all other components, ensuring zero test overlap.

### 1. Software Unit Tests (Automated Suite)
**File:** `unit_tests/test_software_logic.py`
**Framework:** Python `unittest`
*   **Test SW-1 (Logic):** Verifies the irrigation threshold function. Asserts that soil moisture < 30 returns `True` (ON), and >= 30 returns `False` (OFF).
*   **Test SW-2 (Formatting):** Verifies the JSON payload construction guarantees correct data types before entering the network layer.
*   **Test SW-3 (Database):** Creates an *in-memory* SQLite instance (fully isolated from the file system) to assert that SQL `INSERT` and `SELECT` statements execute without syntax errors and preserve data integrity.

### 2. Hardware Unit Tests (Isolated Scripts)
**Context:** To ensure a stable testing environment, we are validating our inputs and outputs using the SenseHAT and Pi Camera, bypassing network constraints.
*   **Test HW-1 (Climate Sensing):** `test_hw_climate.py` polls the I2C sensors and asserts the return values are valid floats within realistic physical boundaries (0-50°C).
*   **Test HW-2 (Actuation):** `test_hw_actuator.py` bypasses logic and forces a digital output to the SenseHAT LED matrix to visually verify the hardware can receive and display state changes (Pump ON/OFF).
*   **Test HW-3 (Vision):** `test_hw_camera.py` directly executes the MIPI CSI-2 interface via `libcamera` and asserts that the resulting image file is created with a size > 0 bytes.
