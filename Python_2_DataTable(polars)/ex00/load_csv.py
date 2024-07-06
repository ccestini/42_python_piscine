import polars as pl


def load(path: str) -> pl.DataFrame:
    """
    Loads a CSV dataset from the given path and prints its dimensions.

    Args:
    path (str): The path to the CSV file.

    Returns:
    The loaded dataset (polars.DataFrame) or None if an error occurs.
    """
    try:
        dataset = pl.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


def main():
    try:
        test_path = '../life_expectancy_years.csv'
        dataset = load(test_path)
        if dataset is not None:
            print(dataset.head())  # Print first few rows, default is 5 rows.
    # to catch any unexpected errors that might occur outside load function.
    except Exception as message:
        print(f"{type(message).__name__}: {message}")


if __name__ == "__main__":
    main()
