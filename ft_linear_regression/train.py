import os
import pandas as pd
import matplotlib.pyplot as plt

# Constants
DATA_FILE_PATH = './data.csv'
MODEL_FILE_PATH = './model.txt'
LEARNING_RATE = 0.1
ITERATIONS = 1000

# Colors
BLUE = '\033[96m'
RED = '\033[91m'
ENDC = '\033[0m'


def load_data(path):
    """
    Load the dataset from a CSV file.
    Args:
        path: The file path to the dataset.
    Return:
        A list containing two lists: mileage and price.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file {path} was not found.")
    dataset = pd.read_csv(path)
    if 'km' not in dataset.columns or 'price' not in dataset.columns:
        raise ValueError("The dataset must contain 'km' and 'price' columns.")
    mileage = dataset['km'].astype(float).tolist()
    price = dataset['price'].astype(float).tolist()
    if not mileage or not price:
        raise ValueError("Dataset is empty.")
    return [mileage, price]


def normalize_data(mileage):
    """
    Normalize the mileage data, using Min-Max normalization technique.
    Args:
        mileage: List of mileage values.
    Return:
        A list containing the normalized mileage list, max and min mileage.
    """
    max_mileage = max(mileage)
    min_mileage = min(mileage)
    if max_mileage <= 0 or min_mileage < 0 or max_mileage == min_mileage:
        raise ValueError("Invalid max and/or min mileage in dataset.")
    normalized_mileage = [(m - min_mileage) / (max_mileage - min_mileage)
                          for m in mileage]
    return [normalized_mileage, max_mileage, min_mileage]


def gradient_descent(mileage_normalized, price, learning_rate, iterations):
    """
    Perform gradient descent to find the optimal parameters.
    Args:
        mileage: List of normalized mileage values.
        price: List of price values.
        learning_rate: The learning rate for gradient descent.
        iterations: Number of iterations for gradient descent.
    Return:
        A list containing the parameters theta_0 and theta_1.
    """
    m = len(mileage_normalized)  # Number of data points
    theta_0, theta_1 = 0, 0
    for i in range(iterations):
        estimated_prices = [theta_0 + (theta_1 * x)
                            for x in mileage_normalized]
        error_t0 = [estimated_prices[i] - price[i] for i in range(m)]
        error_t1 = [(estimated_prices[i] - price[i]) * mileage_normalized[i]
                    for i in range(m)]
        tmp_theta0 = learning_rate * sum(error_t0) / m  # Gradient for theta
        tmp_theta1 = learning_rate * sum(error_t1) / m
        theta_0 -= tmp_theta0  # Updating params
        theta_1 -= tmp_theta1
        if i >= iterations - 3:  # print last 3 iterations
            print(f"Iteration {i}: theta_0 = {theta_0:.1f}, "
                  f"theta_1 = {theta_1:.1f}, tmp_theta0 = {tmp_theta0:.1f}, "
                  f"tmp_theta1 = {tmp_theta1:.1f}\n")
    return [theta_0, theta_1]


def save_model(theta_0, theta_1, max_mileage, min_mileage, path):
    """
    Save the trained model parameters to a file.
    Args:
        theta_0: Parameter theta 0.
        theta_1: Parameter theta 1.
        max_mileage: Max mileage in dataset used for normalization.
        min_mileage: Min mileage in dataset used for normalization.
        path: The file path to save the model.
    Return:
        List of adjusted theta 0 and theta 1 per km.
    """
    # Denormalize theta1
    theta_1 = theta_1 / (max_mileage - min_mileage)
    # Adjust theta0 to fit the denormalized scale
    theta_0 = theta_0 - (theta_1 * min_mileage)
    with open(path, 'w') as file:
        file.write(f"{theta_0}\n{theta_1}\n")
    print(f"\n{BLUE}Model Ready!{ENDC}")
    print(f"{BLUE}----------------------------------------------------{ENDC}")
    print("Values of theta 0 and theta 1 are saved in model.txt.")
    print(f"If the car is new: $ {theta_0:.2f}")
    print(f"Change in Price per KM: $ {theta_1:.5f}")
    print(f"{BLUE}----------------------------------------------------{ENDC}")
    return [theta_0, theta_1]


def plot(mileages, prices, theta_0, theta_1):
    """
    Plot the data points and the regression line.
    Args:
        mileage: List of mileage values.
        price: List of price values.
        theta_0: Calculated parameter theta 0.
        theta_1: Calculated parameter theta 1.
    """
    plt.scatter(mileages, prices, color='blue', label='Actual Prices')
    predicted_prices = [theta_0 + theta_1 * m for m in mileages]
    plt.plot(mileages, predicted_prices, color='magenta',
             label='Predicted Prices')
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Linear Regression Model')
    plt.legend()
    plt.show()


def main():
    try:
        mileages, prices = load_data(DATA_FILE_PATH)
        mileage_normalized, max_mileage, min_mileage = normalize_data(mileages)
        theta_0, theta_1 = gradient_descent(mileage_normalized, prices,
                                            LEARNING_RATE, ITERATIONS)
        theta0_km, theta1_km = save_model(theta_0, theta_1, max_mileage,
                                          min_mileage, MODEL_FILE_PATH)
        plot(mileages, prices, theta0_km, theta1_km)
    except Exception as e:
        print(f"\n{RED}Error: {ENDC}{e}")


if __name__ == "__main__":
    main()
