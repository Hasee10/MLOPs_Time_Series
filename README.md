# ⚡ MLOps Time Series Forecasting Pipeline

![MLOps](https://img.shields.io/badge/MLOps-End--to--End-blueviolet?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square\&logo=python\&logoColor=white)
![Prefect](https://img.shields.io/badge/Prefect-Orchestration-0052CC?style=flat-square)
![Weights & Biases](https://img.shields.io/badge/W%26B-Experiment%20Tracking-orange?style=flat-square)

---

## 🚀 Overview

A fully automated **MLOps pipeline** for forecasting energy consumption using time series data. Built with modern tools like **Prefect**, **Weights & Biases**, and **XGBoost**, this project automates data preprocessing, model training, evaluation, and monitoring — ready for production or research.

---

## 📦 Project Structure

```
MLOPS_Time_Series/
├── data/
│   ├── raw/                # Raw datasets (CSV)
│   └── processed/          # Cleaned datasets
├── src/
│   ├── preprocess.py       # Cleans and prepares data
│   ├── train.py            # Trains XGBoost model
│   └── flow.py             # Prefect flow combining above
├── deploy.py               # Local deployment (no cloud needed)
├── requirements.txt        # Python dependencies
└── README.md               # You're here 🚀
```

---

## 🔁 Pipeline Phases

### ✅ Phase 1: Data Preprocessing

* Clean missing values
* Generate lag features

### ✅ Phase 2: Model Training

* XGBoost regression
* Train/Test split
* MSE evaluation

### ✅ Phase 3: Experiment Tracking

* Logged to **Weights & Biases**
* Track metrics, hyperparameters, and predictions

### ✅ Phase 4: Workflow Orchestration

* Uses **Prefect** to manage dependencies
* Flows can run manually or on schedule

### ✅ Phase 5: Local Scheduling

* Flow scheduled every 1 hour using `flow.deploy()`
* Powered by `prefect orion start`

---

## 📊 Visualization (Streamlit — Coming Soon)

* Forecast trends
* Model performance plots
* Comparison of actual vs predicted

---

## ⚙️ How to Run

### 1. Clone Repo

```bash
git clone https://github.com/<your-username>/MLOPS_Time_Series.git
cd MLOPS_Time_Series
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Preprocess + Train

```bash
python src/preprocess.py
python src/train.py
```

### 4. Run Flow

```bash
python src/flow.py
```

### 5. Deploy Locally (1-hour interval)

```bash
python deploy.py
prefect orion start  # Run in new terminal
```

---

## 🧪 Tools Used

| Tool          | Purpose                        |
| ------------- | ------------------------------ |
| **Prefect**   | Workflow orchestration (local) |
| **W\&B**      | Experiment tracking & logging  |
| **XGBoost**   | Time series regression         |
| **Streamlit** | Visualization dashboard        |
| **GitHub**    | Code versioning & CI/CD        |

---

## 📌 Upcoming

* [ ] Streamlit dashboard integration
* [ ] GitHub Actions CI/CD
* [ ] Model registry + auto-promotion

---

## 🤝 Let's Connect

Made with 💙 by [@ihaseebarshad10](https://github.com/ihaseebarshad10)
For collaborations, ideas or questions — feel free to connect!

---

## 📸 Previews

> *Replace the links below with screenshots/gifs of your own*

* ![Flow Graph](https://github.com/your-username/MLOPS_Time_Series/assets/preview-flow.png)
* ![W\&B Dashboard](https://github.com/your-username/MLOPS_Time_Series/assets/wandb.png)
* ![Streamlit Demo](https://github.com/your-username/MLOPS_Time_Series/assets/streamlit.png)
