# 🏠 California House Price Prediction

A machine learning web application that predicts California house prices using Linear Regression, built with Scikit-learn and deployed via Streamlit.

---

## 📌 Overview

This project uses the **California Housing Dataset** to train a Linear Regression model that estimates median house values based on key property and demographic features. The best-performing model from **5,000 training iterations** is selected and served through a polished, responsive Streamlit web interface.

---

## 📁 Project Structure

```
Mini_Project_clg/
│
├── app.py                              # Streamlit web application
├── model.py                            # Model training pipeline
├── House_Price_Prediction.ipynb        # Jupyter notebook (EDA + training)
├── Model_For_House_Price_Prediction.pkl  # Saved best LinearRegression model
├── scaler.pkl                          # Saved MinMaxScaler
├── fetch_california_housing.xlsx       # Exported dataset
└── requirements.txt                    # Python dependencies
```

---

## 🤖 Machine Learning Pipeline

### Step 1 — Dataset
- Source: `sklearn.datasets.fetch_california_housing`
- 20,640 samples, 8 input features
- Target: Median House Value (in $100,000s)

### Step 2 — Features Used

| Feature | Description |
|---|---|
| `MedInc` | Median income in block group |
| `HouseAge` | Median house age in block group |
| `AveRooms` | Average number of rooms per household |
| `AveBedrms` | Average number of bedrooms per household |
| `Population` | Block group population |
| `AveOccup` | Average number of household members |
| `Latitude` | Block group latitude |

### Step 3 — Preprocessing
- No missing values in dataset
- Features scaled using **MinMaxScaler** (range 0–1)

### Step 4 — Model Selection
- Algorithm: **Linear Regression**
- Trained **5,000 models** with different `random_state` splits (90/10 train-test)
- Best model selected based on **highest R² score**

### Step 5 — Model Evaluation (Best Model)

| Metric | Value |
|---|---|
| R² Score | Best across 5,000 runs |
| MAE | Mean Absolute Error |
| MSE | Mean Squared Error |
| RMSE | Root Mean Squared Error |

### Step 6 — Saving
- Best model serialized with `pickle` → `Model_For_House_Price_Prediction.pkl`
- Fitted scaler saved → `scaler.pkl`

---


## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| ML Library | Scikit-learn 1.6.0 |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Web Framework | Streamlit |
| Deployment | Render |

---

## 📦 Requirements

```
streamlit
scikit-learn==1.6.0
pandas
```

---

## 📊 How It Works

1. User enters property details (income, house age, rooms, etc.) in the web UI
2. Input is scaled using the saved `MinMaxScaler`
3. Scaled input is passed to the saved `LinearRegression` model
4. Predicted value (in $100,000 units) is multiplied by 100,000
5. Final estimated price is displayed in the result card

---

## 👩‍💻 Author

**Tulasi Raya**
- GitHub: [@TulasiRaya](https://github.com/TulasiRaya)

---
