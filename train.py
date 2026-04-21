import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import r2_score, accuracy_score

from utils import categorize_aqi

# ---------------- LOAD DATA ----------------
df = pd.read_csv("data/air_quality.csv")

# Clean column names
df.columns = df.columns.str.strip()
print("Columns:", df.columns.tolist())

# If AQI missing → generate it (failsafe)
if "AQI" not in df.columns:
    print("⚠️ AQI not found. Generating AQI...")
    df["AQI"] = (
        df["PM2.5"] * 0.5 +
        df["PM10"] * 0.2 +
        df["NO2"] * 0.1 +
        df["SO2"] * 0.1 +
        df["CO"] * 8
    )

df = df.dropna()

# ---------------- FEATURES ----------------
X = df.drop("AQI", axis=1)
y_reg = df["AQI"]
y_clf = df["AQI"].apply(categorize_aqi)

# ---------------- SCALING ----------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---------------- SPLIT ----------------
X_train, X_test, y_train_reg, y_test_reg = train_test_split(
    X_scaled, y_reg, test_size=0.2, random_state=42
)

_, _, y_train_clf, y_test_clf = train_test_split(
    X_scaled, y_clf, test_size=0.2, random_state=42
)

# ---------------- MODELS ----------------
reg_model = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)
clf_model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)

reg_model.fit(X_train, y_train_reg)
clf_model.fit(X_train, y_train_clf)

# ---------------- METRICS ----------------
r2 = r2_score(y_test_reg, reg_model.predict(X_test))
acc = accuracy_score(y_test_clf, clf_model.predict(X_test))

print(f"✅ R2 Score: {r2:.2f}")
print(f"✅ Classification Accuracy: {acc:.2f}")

# ---------------- SAVE ----------------
joblib.dump(reg_model, "models/regression_model.pkl")
joblib.dump(clf_model, "models/classification_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("✅ Models saved successfully!")