import mysql.connector
import pandas as pd
from config import DB_CONFIG

def predict_next_day():
    conn = mysql.connector.connect(**DB_CONFIG)
    df = pd.read_sql("SELECT temperature FROM weather_data", conn)
    conn.close()

    predicted_temp = df["temperature"].rolling(window=3).mean().iloc[-1]
    return round(predicted_temp, 2)

if __name__ == "__main__":
    print("Predicted Next Day Temperature:", predict_next_day(), "°C")
