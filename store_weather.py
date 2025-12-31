import mysql.connector
from datetime import datetime
from fetch_weather import fetch_weather
from config import DB_CONFIG

def store_weather():
    data = fetch_weather()
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    query = """
    INSERT INTO weather_data 
    (city, temperature, humidity, pressure, weather, wind_speed, timestamp)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (
        data["city"],
        data["temperature"],
        data["humidity"],
        data["pressure"],
        data["weather"],
        data["wind_speed"],
        datetime.now()
    ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    store_weather()
