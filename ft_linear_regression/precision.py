import os
import pandas as pd
import numpy as np

# Constants
DATA_FILE_PATH = './data.csv'
MODEL_FILE_PATH = './trained_model.txt'


def load_data(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file {path} was not found.")
    dataset = pd.read_csv(path)
    if 'km' not in dataset.columns or 'price' not in dataset.columns:
        raise ValueError("The file data.csv must contain 'km' and 'price' columns.")
    mileage = dataset['km'].astype(float).tolist()
    price = dataset['price'].astype(float).tolist()
    if not mileage or not price:
        raise ValueError("Dataset is empty.")
    return mileage, price


def normalize_data(mileage, max_mileage, min_mileage):
    # Normalize each mileage value to the range [0, 1]
    normalized_mileage = [(m - min_mileage) / (max_mileage - min_mileage) for m in mileage]
    return normalized_mileage


def load_trained_model(path=MODEL_FILE_PATH):
    try:
        with open(path, 'r') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]  # Ignore empty lines
            if not lines or len(lines) != 4:
                print("Error: trained_model.txt must contain: theta_0, theta_1, max_mileage, and min_mileage.\nUsing default values.")
                return 0, 0, 1, 0
            theta_0 = float(lines[0].strip())
            theta_1 = float(lines[1].strip())
            max_mileage = float(lines[2].strip())
            min_mileage = float(lines[3].strip())
            if max_mileage <= 0 or min_mileage < 0:
                print("Error: Invalid max_mileage/min_mileage in trained_model.txt.\nUsing default values.")
                return 0, 0, 1, 0
            return theta_0, theta_1, max_mileage, min_mileage
    except FileNotFoundError:
        print("trained_model.txt not found.\nUsing default values.")
        return 0, 0, 1, 0
    except ValueError:
        print("trained_model.txt contains invalid data.\nUsing default values.")
        return 0, 0, 1, 0
    except Exception as e:
        print(f"Error: {e}. Using default values.")
        return 0, 0, 1, 0


def estimate_price(theta_0, theta_1, mileage, max_mileage, min_mileage):
    normalized_mileage = (mileage - min_mileage) / (max_mileage - min_mileage)
    estimated_price = theta_0 + (theta_1 * normalized_mileage)
    return max(estimated_price, 0)  # Ensure the price is not negative


def calculate_rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())


def calculate_mae(predictions, targets):
    return np.abs(predictions - targets).mean()


def main():
    mileage, actual_prices = load_data(DATA_FILE_PATH)
    theta_0, theta_1, max_mileage, min_mileage = load_trained_model()
    normalized_mileage = normalize_data(mileage, max_mileage, min_mileage)
    
    predicted_prices = [estimate_price(theta_0, theta_1, m, max_mileage, min_mileage) for m in mileage]
    
    # Calculate RMSE
    rmse = calculate_rmse(np.array(predicted_prices), np.array(actual_prices))
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
    # Calculate MAE
    mae = calculate_mae(np.array(predicted_prices), np.array(actual_prices))
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    

if __name__ == "__main__":
    main()
