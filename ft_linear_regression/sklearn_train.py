import os
import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

# Constants
DATA_FILE_PATH = './data.csv'
MODEL_FILE_PATH_SGD = './sklearn_sgd_model.pkl'
TRAINED_MODEL_TXT = './sklearn_trained_model.txt'


def load_data(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file {path} was not found.")
    dataset = pd.read_csv(path)
    if 'km' not in dataset.columns or 'price' not in dataset.columns:
        raise ValueError("The file data.csv must contain 'km' and 'price' columns.")
    mileage = dataset['km'].astype(float).values.reshape(-1, 1)
    price = dataset['price'].astype(float).values
    if not len(mileage) or not len(price):
        raise ValueError("Dataset is empty.")
    return mileage, price


def normalize_data(mileage):
    scaler = MinMaxScaler()
    normalized_mileage = scaler.fit_transform(mileage)
    return normalized_mileage, scaler.data_max_[0], scaler.data_min_[0]


def train_and_save_model(mileage, price, model_file_path, text_file_path):
    scaler = MinMaxScaler()
    mileage_normalized = scaler.fit_transform(mileage)
    model = SGDRegressor(max_iter=10000, tol=1e-3)
    model.fit(mileage_normalized, price)
    joblib.dump((model, scaler), model_file_path)
    theta_0 = model.intercept_[0]
    theta_1 = model.coef_[0]
    max_mileage = scaler.data_max_[0]
    min_mileage = scaler.data_min_[0]
    with open(text_file_path, 'w') as file:
        file.write(f"{theta_0}\n{theta_1}\n{max_mileage}\n{min_mileage}\n")
    return model, scaler


def plot_results(mileage, price, model, scaler):
    mileage_normalized = scaler.transform(mileage)
    predicted_prices = model.predict(mileage_normalized)
    plt.scatter(mileage, price, color='blue', label='Data points')
    plt.plot(mileage, predicted_prices, color='green', label='SGD Regression Line')
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('SKlearn SGD Regression: Price vs Kilometers')
    plt.legend()
    plt.show()


def evaluate_model(mileage, price, model, scaler):
    mileage_normalized = scaler.transform(mileage)
    predicted_prices = model.predict(mileage_normalized)
    rmse = np.sqrt(mean_squared_error(price, predicted_prices))
    mae = mean_absolute_error(price, predicted_prices)
    return rmse, mae


def main():
    mileage, price = load_data(DATA_FILE_PATH)
    # Train and save SGD regression model
    sgd_model, sgd_scaler = train_and_save_model(mileage, price, MODEL_FILE_PATH_SGD, TRAINED_MODEL_TXT)
    # Plot results
    plot_results(mileage, price, sgd_model, sgd_scaler)
    # Evaluate model
    sgd_rmse, sgd_mae = evaluate_model(mileage, price, sgd_model, sgd_scaler)
    print(f"SGD Regression - RMSE: {sgd_rmse:.2f}, MAE: {sgd_mae:.2f}")


if __name__ == "__main__":
    main()