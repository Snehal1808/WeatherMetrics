import streamlit as st
import mysql.connector
import pandas as pd
from config import DB_CONFIG
from predict import predict_next_day

st.title("🌦 Live Weather Dashboard")

conn = mysql.connector.connect(**DB_CONFIG)
df = pd.read_sql("SELECT * FROM weather_data ORDER BY timestamp DESC", conn)
conn.close()

st.subheader("Latest Weather Data")
st.dataframe(df.head())

st.subheader("Temperature Trend")
st.line_chart(df.set_index("timestamp")["temperature"])

st.subheader("📈 Prediction")
st.success(f"Predicted Next Day Temperature: {predict_next_day()} °C")
