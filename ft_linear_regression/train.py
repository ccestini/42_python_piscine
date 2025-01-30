from prediction import estimatePrice
import os
import pandas as pd

def load(path: str):
    """
    Loads a CSV dataset from the given path.

    Args:
    path (str): The path to the CSV file.

    Returns:
    tuple: (mileage, price) lists or (None, None) if an error occurs.
    """
    try:
        dataset = pd.read_csv(path)
        if 'km' not in dataset.columns or 'price' not in dataset.columns:
            raise ValueError("Dataset must contain 'km' and 'price' columns.")
        mileage = dataset['km'].astype(float).tolist()
        price = dataset['price'].astype(float).tolist()
        if not mileage or not price:
            raise ValueError("Dataset is empty.")
        return mileage, price
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None, None


def main():
    try:
        path = './data.csv'
        mileage, price = load(path)
        if mileage and price:
            print(f"Loaded mileage list: {mileage}")
            print(f"Loaded price list: {price}")
        
        # Example usage of estimatePrice (replace with actual training logic later)
            theta_0, theta_1 = 0, 0  # Placeholder values
            example_mileage = mileage[0]
            estimated_price = estimatePrice(theta_0, theta_1, example_mileage)
            print(f"Estimated price for {example_mileage} km: ${estimated_price:.2f}")
   
    except Exception as message:
        print(f"{type(message).__name__}: {message}")

if __name__ == "__main__":
    main()
