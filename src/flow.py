from prefect import flow, task
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import wandb
import os

@task
def preprocess():
    df = pd.read_csv("data/raw/energy.csv", parse_dates=["Datetime"])
    df = df.set_index("Datetime").sort_index()
    df = df.fillna(method="ffill")

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/cleaned_energy.csv")
    return df

@task
def train(df):
    df["lag1"] = df["PJME_MW"].shift(1)
    df = df.dropna()

    X = df[["lag1"]]
    y = df["PJME_MW"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

    model = xgb.XGBRegressor()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    wandb.init(project="energy-forecasting", name="prefect-xgboost-run", reinit=True)
    wandb.log({"mse": mse})

    print(f"✅ Flow completed — MSE: {mse:.2f}")

@flow(name="Energy Forecasting Pipeline")
def energy_flow():
    df = preprocess()
    train(df)

if __name__ == "__main__":
    energy_flow()
