# 🌍 Air Quality AI System

An end-to-end Machine Learning project that predicts **Air Quality Index (AQI)** using environmental and pollution data, with an interactive dashboard and automated report generation.

---

## 🚀 Live Demo

👉  https://air-quality-ai-system-nmpsidjipmvwy44s6j6mxk.streamlit.app/

---

## 📌 Features

* 🔮 **AQI Prediction**

  * Regression model to predict AQI value
  * Classification model to categorize air quality

* 📊 **Interactive Dashboard**

  * Built using Streamlit
  * Real-time input-based predictions

* 📂 **Custom Dataset Upload**

  * Users can upload their own CSV file
  * Dynamic analysis and visualization

* 📈 **Data Insights**

  * AQI distribution
  * Feature correlation
  * Feature importance visualization

* 📄 **PDF Report Generation**

  * Downloadable AQI report for predictions

---

## 🧠 Machine Learning Models

* 🌲 Random Forest Regressor
* 🌲 Random Forest Classifier

### ⚙️ Pipeline

* Data Cleaning & Validation
* Feature Scaling (StandardScaler)
* Train-Test Split
* Model Training & Evaluation

---

## 📊 Dataset

* Synthetic dataset generated using environmental simulation
* Includes features like:

```
PM2.5, PM10, NO2, SO2, CO, Temperature, Humidity, WindSpeed
```

* AQI is computed using a weighted formula based on pollutant impact

---

## 🗂️ Project Structure

```
air-quality-ai-system/
│
├── data/
│   └── air_quality.csv
│
├── models/
│   ├── regression_model.pkl
│   ├── classification_model.pkl
│   └── scaler.pkl
│
├── generate_data.py
├── train.py
├── utils.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run Locally

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Generate dataset

```
python generate_data.py
```

### 3️⃣ Train models

```
python train.py
```

### 4️⃣ Run application

```
streamlit run streamlit_app.py
```

---

## 📈 Model Performance

* Regression Model (R² Score): ~0.90+
* Classification Accuracy: ~90%+

*(May vary depending on dataset)*

---

## 🎯 Use Case

* Environmental monitoring
* Pollution analysis
* Smart city applications
* Health risk awareness

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Matplotlib
* ReportLab

---

## 💡 Future Improvements

* 🌐 Live AQI data integration (API)
* 📍 Location-based predictions
* 🔐 User authentication
* ☁️ Cloud deployment with CI/CD
* 📊 Advanced visual analytics

---

## 👨‍💻 Author

N Ashwitha Reddy
GitHub:https://github.com/ashw6

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!
