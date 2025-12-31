import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from config import DB_CONFIG

def visualize():
    conn = mysql.connector.connect(**DB_CONFIG)
    df = pd.read_sql("SELECT * FROM weather_data ORDER BY timestamp", conn)
    conn.close()

    plt.figure()
    plt.plot(df["timestamp"], df["temperature"])
    plt.title("Temperature Trend")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
