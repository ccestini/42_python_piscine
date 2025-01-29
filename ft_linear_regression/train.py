import csv
import pandas as pd
import numpy as np


def load_data():
    """
    Loads a CSV dataset.

    Returns: The loaded dataset (pandas.DataFrame) or None if an error occurs.
    """
    try:
        dataset = pd.read_csv('data.csv')
        return dataset
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


def main():
    try:
        dataset = load_data()
        if dataset is not None:
            print(dataset)
        else:
            print("Failed to load dataset.")
    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()

