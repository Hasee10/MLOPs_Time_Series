import pandas as pd
import wandb
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Initialize W&B
wandb.init(project="energy-forecasting", name="xgboost-run")

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_energy.csv", parse_dates=["Datetime"])
df = df.set_index("Datetime")

# Create lag features
df['lag1'] = df['PJME_MW'].shift(1)
df = df.dropna()

# Train/test split
X = df[['lag1']]
y = df['PJME_MW']
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

# Train model
model = xgb.XGBRegressor()
model.fit(X_train, y_train)

# Predict + Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Log to W&B
wandb.log({
    "mse": mse
})

print(f"✅ Training complete — MSE: {mse:.2f}")
