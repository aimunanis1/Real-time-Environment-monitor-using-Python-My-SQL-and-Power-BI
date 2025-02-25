import serial
import pyodbc
import time
import re

# Serial port configuration (check your port, e.g., COM3 on Windows)
ser = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)  # Wait for the serial connection to initialize

# SQL Server Database connection for pyodbc
db = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=MSAALAPTOP1\\SQLEXPRESS;"
    "DATABASE=envmonitor;"  # Make sure this is the correct database name
    "Trusted_Connection=yes;"
)
cursor = db.cursor()


# Function to insert data into SQL Server with timestamp
def insert_data(temp, hum):
    try:
        print(f"Debug: Inserting Temp={temp}, Hum={hum}")  # Debug print to verify values

        query = "INSERT INTO table_3 (temperature, humidity, timestamp) VALUES (?, ?, GETDATE())"
        values = (temp, hum)

        cursor.execute(query, values)
        db.commit()

        print(f"Inserted {cursor.rowcount} row(s).")  # Debug output

    except Exception as e:
        print(f"Database Insert Error: {e}")


# Regular expression pattern to match valid temperature and humidity data
data_pattern = re.compile(r"^\s*(\d+(\.\d+)?),\s*(\d+(\.\d+)?)\s*$")

try:
    while True:
        try:
            raw_data = ser.readline()
            line = raw_data.decode('utf-8', errors='ignore').strip()  # Ignore invalid characters

            if line:
                print(f"Raw data received: {line}")

                # Use regex to check for the expected temperature and humidity format
                match = data_pattern.match(line)
                if match:
                    temp = float(match.group(1))
                    hum = float(match.group(3))
                    print(f"Debug: Temp={temp}, Hum={hum}")  # Print values before insertion
                    insert_data(temp, hum)
                else:
                    print("Invalid data format. Skipping...")

        except UnicodeDecodeError:
            print("Error decoding serial data.")

        time.sleep(1)  # Add delay to avoid high CPU usage

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()
    cursor.close()
    db.close()
