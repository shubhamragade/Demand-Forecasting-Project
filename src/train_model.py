from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os
import pandas as pd
from src.preprocess import load_data

MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

def train_model():
    train, _ = load_data()

    # Target column
    y = train["num_orders"]
    X = train.drop(columns=["num_orders", "id"])  # drop id

    # Convert categorical variables
    X = pd.get_dummies(X, drop_first=True)

    # Train-test split
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, os.path.join(MODEL_DIR, "food_demand_model.pkl"))
    print("✅ Model trained and saved successfully!")

if __name__ == "__main__":
    train_model()
