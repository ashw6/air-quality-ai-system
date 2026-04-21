import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from utils import label

# Load models
reg_model = joblib.load("models/regression_model.pkl")
clf_model = joblib.load("models/classification_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.set_page_config(page_title="Air Quality AI System", layout="wide")
st.title("🌍 Air Quality Intelligence System")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Custom dataset loaded!")
else:
    df = pd.read_csv("data/air_quality.csv")

df.columns = df.columns.str.strip()

# ---------------- INPUT ----------------
st.sidebar.header("Enter Values")

pm25 = st.sidebar.number_input("PM2.5", 0.0)
pm10 = st.sidebar.number_input("PM10", 0.0)
no2 = st.sidebar.number_input("NO2", 0.0)
so2 = st.sidebar.number_input("SO2", 0.0)
co = st.sidebar.number_input("CO", 0.0)
temp = st.sidebar.number_input("Temperature", 0.0)
hum = st.sidebar.number_input("Humidity", 0.0)
wind = st.sidebar.number_input("WindSpeed", 0.0)

input_data = np.array([[pm25, pm10, no2, so2, co, temp, hum, wind]])

# ---------------- PREDICTION ----------------
if st.sidebar.button("Predict AQI"):

    scaled = scaler.transform(input_data)

    aqi_value = reg_model.predict(scaled)[0]
    aqi_class = clf_model.predict(scaled)[0]

    st.subheader("🔮 Prediction Result")
    st.metric("AQI", round(aqi_value, 2))
    st.success(f"{label(aqi_class)}")

    # -------- PDF --------
    from reportlab.platypus import SimpleDocTemplate, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet

    if st.button("Download Report"):
        doc = SimpleDocTemplate("AQI_Report.pdf")
        styles = getSampleStyleSheet()

        content = [
            Paragraph("Air Quality Report", styles["Title"]),
            Paragraph(f"AQI: {round(aqi_value,2)}", styles["Normal"]),
            Paragraph(f"Category: {label(aqi_class)}", styles["Normal"]),
        ]

        doc.build(content)

        with open("AQI_Report.pdf", "rb") as f:
            st.download_button("Download PDF", f, "AQI_Report.pdf")

# ---------------- VISUALS ----------------
st.subheader("📊 Dataset Insights")

if "AQI" in df.columns:
    fig, ax = plt.subplots()
    ax.hist(df["AQI"], bins=20)
    st.pyplot(fig)
else:
    st.warning("AQI column missing")

# Feature Importance
st.subheader("📊 Feature Importance")
features = df.drop("AQI", axis=1).columns
importance = reg_model.feature_importances_

fig, ax = plt.subplots()
ax.barh(features, importance)
st.pyplot(fig)