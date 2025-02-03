import os
import pandas as pd
import matplotlib.pyplot as plt

# Constants
DATA_FILE_PATH = './data.csv'
MODEL_FILE_PATH = './trained_model.txt'
LEARNING_RATE = 0.1  # Learning rate for gradient descent
ITERATIONS = 10000  # Number of iterations for gradient descent

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

def normalize_data(mileage):
    max_mileage = max(mileage)
    min_mileage = min(mileage)
    normalized_mileage = [(m - min_mileage) / (max_mileage - min_mileage) for m in mileage]
    return normalized_mileage, max_mileage, min_mileage

def gradient_descent(mileage, price, learning_rate, iterations):
    m = len(mileage)
    theta_0, theta_1 = 0, 0
    for _ in range(iterations):
        estimated_prices = [theta_0 + theta_1 * x for x in mileage]
        error = [estimated_prices[i] - price[i] for i in range(m)]
        tmp_theta0 = learning_rate * sum(error) / m
        tmp_theta1 = learning_rate * sum([error[i] * mileage[i] for i in range(m)]) / m
        theta_0 -= tmp_theta0
        theta_1 -= tmp_theta1
    return theta_0, theta_1

def save_model(theta_0, theta_1, max_mileage, min_mileage, path=MODEL_FILE_PATH):
    with open(path, 'w') as file:
        file.write(f"{theta_0}\n{theta_1}\n{max_mileage}\n{min_mileage}\n")

def plot(mileage, price, theta_0, theta_1, max_mileage, min_mileage):
    plt.scatter(mileage, price, color='blue', label='Data points')
    mileage_normalized = [(m - min_mileage) / (max_mileage - min_mileage) for m in mileage]
    predicted_prices = [theta_0 + theta_1 * m for m in mileage_normalized]
    plt.plot(mileage, predicted_prices, color='red', label='Custom Regression Line')
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Linear Regression: Price vs Kilometers')
    plt.legend()
    plt.show()

def main():
    mileage, price = load_data(DATA_FILE_PATH)
    mileage_normalized, max_mileage, min_mileage = normalize_data(mileage)
    theta_0, theta_1 = gradient_descent(mileage_normalized, price, LEARNING_RATE, ITERATIONS)
    save_model(theta_0, theta_1, max_mileage, min_mileage, MODEL_FILE_PATH)
    plot(mileage, price, theta_0, theta_1, max_mileage, min_mileage)

if __name__ == "__main__":
    main()
    