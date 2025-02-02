import os
import pandas as pd
import matplotlib.pyplot as plt


def load_files(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file {path} was not found.")
    
    if path == './data.csv':
        dataset = pd.read_csv(path)
        if 'km' not in dataset.columns or 'price' not in dataset.columns:
            raise ValueError("The file data.csv must contain 'km' and 'price' columns.")
        mileage = dataset['km'].astype(float).tolist()
        price = dataset['price'].astype(float).tolist()
        if not mileage or not price:
            raise ValueError("Dataset is empty.")
        return mileage, price  

    elif path == './trained_model.txt':
        with open(path, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 3:
                theta_0 = float(lines[0].strip())
                theta_1 = float(lines[1].strip())
                max_mileage = float(lines[2].strip())
                return theta_0, theta_1, max_mileage
            else:
                raise ValueError("trained_model.txt file is incomplete.")
    
    else:
        raise ValueError("To plot the graph a data.csv and a trained_model.txt files are required.")
    

def plot(mileage, price, theta_0, theta_1, max_mileage):
    plt.scatter(mileage, price, color='blue', label='Data points')
    mileage_normalized = [m / max_mileage for m in mileage]
    predicted_prices = [theta_0 + theta_1 * m for m in mileage_normalized]
    plt.plot(mileage, predicted_prices, color='red', label='Regression Line')
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Linear Regression: Price vs Kilometers')
    plt.show()


def main():
    try:
        path_data = './data.csv'
        mileage, price = load_files(path_data)     
        path_model = './trained_model.txt'
        theta_0, theta_1, max_mileage = load_files(path_model)
        plot(mileage, price, theta_0, theta_1, max_mileage)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

