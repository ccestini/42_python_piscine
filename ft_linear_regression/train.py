import os
import pandas as pd
import matplotlib.pyplot as plt

# Constants
DATA_FILE_PATH = './data.csv'
MODEL_FILE_PATH = './trained_model.txt'
LEARNING_RATE = 0.1  # Learning rate for gradient descent
ITERATIONS = 1000  # Number of iterations for gradient descent


def load_data(path: str):
    """
    Load the dataset from a CSV file.
    Args:
        path: The file path to the dataset.
    Returns:
        A tuple containing two lists: mileage and price.
    """
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
    """
    Normalize the mileage data.
    Args:
        mileage: List of mileage values.
    Returns:
        A tuple containing the normalized mileage list, max mileage, and min mileage.
    """
    max_mileage = max(mileage)
    min_mileage = min(mileage)
    normalized_mileage = [(m - min_mileage) / (max_mileage - min_mileage) for m in mileage]
    print(f"\nData normalized: {normalized_mileage} and qtde of kms normalized = {len(normalized_mileage)}\n")
    return normalized_mileage, max_mileage, min_mileage


def gradient_descent(mileage, price, learning_rate, iterations):
    """
    Perform gradient descent to find the optimal parameters.
    Args:
        mileage: List of normalized mileage values.
        price: List of price values.
        learning_rate: The learning rate for gradient descent.
        iterations: Number of iterations for gradient descent.
    Returns:
        A tuple containing the parameters theta_0 and theta_1.
    """
    m = len(mileage)
    theta_0, theta_1 = 0, 0
    for i in range(iterations):
        estimated_prices = [theta_0 + theta_1 * x for x in mileage]
        error = [estimated_prices[i] - price[i] for i in range(m)]
        tmp_theta0 = learning_rate * sum(error) / m
        tmp_theta1 = learning_rate * sum([error[i] * mileage[i] for i in range(m)]) / m
        theta_0 -= tmp_theta0
        theta_1 -= tmp_theta1
        # Print first and last 3 values at every iteration for Debug
        if i < 3 or i >= iterations - 3:
            print(f"Iteration {i}: theta_0 = {theta_0:.1f}, theta_1 = {theta_1:.1f}, tmp_theta0 = {tmp_theta0:.1f}, tmp_theta1 = {tmp_theta1:.1f}")
    return theta_0, theta_1


def save_model(theta_0, theta_1, max_mileage, min_mileage, path=MODEL_FILE_PATH):
    """
    Save the trained model parameters to a file.
    Args:
        theta_0: Parameter theta 0.
        theta_1: Parameter theta 1.
        max_mileage: Max mileage used for normalization.
        min_mileage: Min mileage used for normalization.
        path: The file path to save the model.
    """
    with open(path, 'w') as file:
        file.write(f"{theta_0}\n{theta_1}\n{max_mileage}\n{min_mileage}\n")
    print("\nModel Ready! Values of theta 0 and theta 1 are saved in trained_model.txt.")


def plot(mileage, price, theta_0, theta_1, max_mileage, min_mileage, mileage_normalized):
    """
    Plot the data points and the regression line.
    Args:
        mileage: List of mileage values.
        price: List of price values.
        theta_0: Parameter theta 0.
        theta_1: Parameter theta 1.
        max_mileage: Max mileage used for normalization.
        min_mileage: Min mileage used for normalization.
        mileage_normalized: List of normalized mileage values.
    """
    plt.scatter(mileage, price, color='blue', label='Actual Prices')
    predicted_prices = [theta_0 + theta_1 * m for m in mileage_normalized]
    print(f"\nPredicted Prices: {predicted_prices}\n")
    plt.plot(mileage, predicted_prices, color='red', label='Predicted Prices')
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Linear Regression: Price vs Kilometers')
    plt.legend()
    plt.show()


def main():
    try:
        mileage, price = load_data(DATA_FILE_PATH)
        mileage_normalized, max_mileage, min_mileage = normalize_data(mileage)
        theta_0, theta_1 = gradient_descent(mileage_normalized, price, LEARNING_RATE, ITERATIONS)
        save_model(theta_0, theta_1, max_mileage, min_mileage, MODEL_FILE_PATH)
        plot(mileage, price, theta_0, theta_1, max_mileage, min_mileage, mileage_normalized)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
