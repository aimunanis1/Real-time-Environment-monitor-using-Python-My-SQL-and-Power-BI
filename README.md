# 🌍 Environmental Monitoring with ESP32 & Data Analytics

![ENDTOEND](https://github.com/user-attachments/assets/5648fcdf-40c6-46e5-96ae-cc7b7ec24894)

## 📌 Project Overview
This project is a **real-time environmental monitoring system** using an **ESP32 microcontroller** and a **DHT22 sensor** to measure temperature and humidity. The collected data is processed in **Python**, stored in **SQL Server**, and visualized using **Power BI**. 📊🚀

## 🛠️ Components & Technologies Used
- **ESP32** 🖥️ (Microcontroller for reading sensor data)
- **DHT22 Sensor** 🌡️ (Measures temperature & humidity)
- **Python** 🐍 (For serial communication and data processing)
- **PySerial** 🔌 (Reads data from ESP32 via Serial Communication)
- **SQL Server** 🗄️ (Stores sensor data for further analysis)
- **Power BI (Free Version)** 📊 (Visualizing trends & insights)

## 🔄 How It Works
1. **Data Collection** 📥  
   - The **DHT22 sensor** measures temperature & humidity.  
   - Data is sent to the **ESP32**, programmed using **Arduino IDE**.

2. **Data Processing & Storage** 💾  
   - **Python & PySerial** read the data via **Serial Communication**.  
   - Data is validated using **Regular Expressions (re module)**.
   - Valid data is inserted into a **SQL Server database** using **pyodbc**.

3. **Data Visualization & Analysis** 📊  
   - The stored data is analyzed using **SQL queries**.
   - **Power BI** is used to create real-time dashboards and reports.

## 📊 Why Data Analytics Matters
This project isn’t just about collecting sensor data—it’s about **turning raw data into meaningful insights**:
- **Real-Time Monitoring:** Track environmental conditions instantly.
- **Predictive Insights:** Identify trends and forecast changes. 🔍
- **Smart Decision-Making:** Use data to automate systems and improve efficiency.

## 🔥 My Passion: Merging Hardware & Data Science
I love combining **embedded systems (ESP32, sensors)** with **data analytics** to create impactful solutions. This project bridges the gap between **IoT and Data Science**, showing how real-world data can be collected, stored, and analyzed for smarter decision-making. 🚀💡




## 🛠️ Setup Instructions
### 1️⃣ Hardware Setup
- Connect the **DHT22 sensor** to the ESP32.
- Use **Arduino IDE** to upload the ESP32 code.

### 2️⃣ Software Setup
- Install Python and required libraries:
  ```sh
  pip install pyserial pyodbc
  ```
- Set up **SQL Server** and create the necessary database and table.
- Run the **Python script** to start collecting and storing data.

### 3️⃣ Power BI Integration
- Load data from SQL Server into Power BI.
- Create visualizations to analyze trends.

## 📝 Python Script
```python
import serial
import pyodbc
import time
import re

ser = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)

db = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=MSAALAPTOP1\\SQLEXPRESS;"
    "DATABASE=envmonitor;"
    "Trusted_Connection=yes;"
)
cursor = db.cursor()

def insert_data(temp, hum):
    try:
        print(f"Debug: Inserting Temp={temp}, Hum={hum}")
        query = "INSERT INTO table_3 (temperature, humidity, timestamp) VALUES (?, ?, GETDATE())"
        values = (temp, hum)
        cursor.execute(query, values)
        db.commit()
        print(f"Inserted {cursor.rowcount} row(s).")
    except Exception as e:
        print(f"Database Insert Error: {e}")

data_pattern = re.compile(r"^\s*(\d+(\.\d+)?),\s*(\d+(\.\d+)?)\s*$")

try:
    while True:
        try:
            raw_data = ser.readline()
            line = raw_data.decode('utf-8', errors='ignore').strip()
            
            if line:
                print(f"Raw data received: {line}")
                match = data_pattern.match(line)
                if match:
                    temp = float(match.group(1))
                    hum = float(match.group(3))
                    print(f"Debug: Temp={temp}, Hum={hum}")
                    insert_data(temp, hum)
                else:
                    print("Invalid data format. Skipping...")
        except UnicodeDecodeError:
            print("Error decoding serial data.")
        
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
    ser.close()
    cursor.close()
    db.close()
```

## 🏆 Future Enhancements
- Integrate **AI-powered anomaly detection** for better insights. 🤖
- Expand to multiple sensor nodes for broader environmental tracking.


---
🚀 **Let’s make data-driven decisions for a smarter world!** 🌱
