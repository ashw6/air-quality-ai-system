import pandas as pd
import numpy as np

np.random.seed(42)
rows = 1500

data = {
    "PM2.5": np.random.uniform(10, 300, rows),
    "PM10": np.random.uniform(20, 400, rows),
    "NO2": np.random.uniform(5, 150, rows),
    "SO2": np.random.uniform(2, 80, rows),
    "CO": np.random.uniform(0.1, 5, rows),
    "Temperature": np.random.uniform(10, 45, rows),
    "Humidity": np.random.uniform(20, 90, rows),
    "WindSpeed": np.random.uniform(0, 20, rows),
}

df = pd.DataFrame(data)

# Generate AQI (always ensures AQI exists)
df["AQI"] = (
    df["PM2.5"] * 0.5 +
    df["PM10"] * 0.2 +
    df["NO2"] * 0.1 +
    df["SO2"] * 0.1 +
    df["CO"] * 8 -
    df["WindSpeed"] * 0.3
)

df.to_csv("data/air_quality.csv", index=False)
print("✅ Dataset generated successfully!")