from train import load_data
from predict import load_trained_model, estimate_price

# Constants
DATA_FILE_PATH = './data.csv'
MODEL_FILE_PATH = './model.txt'


def calculate_mae(predictions, targets):
    """
    Calculate the Mean Absolute Error (MAE).
    Args:
        predictions: List of predicted values.
        targets: List of actual values.
    Returns:
        Mean Absolute Error.
    """
    n = len(predictions)
    if n == 0 or n != len(targets):
        raise ValueError("Predictions and targets must have the same "
                         "non-zero length.")
    mae = sum(abs(predictions[i] - targets[i]) for i in range(n)) / n
    return mae


def main():
    try:
        mileage, actual_prices = load_data(DATA_FILE_PATH)
        theta_0, theta_1, max_mileage, min_mileage = load_trained_model()
        if not theta_0 and not theta_1:
            raise ValueError("Model not found. Please train the model first.")  
        predicted_prices = [estimate_price(theta_0, theta_1, m, max_mileage,
                                           min_mileage) for m in mileage]
        mae = calculate_mae(predicted_prices, actual_prices)
        print(f"The precision metric using the Mean Absolute Error (MAE): "
              f"$ {mae:.2f}")

    except Exception as e:
        print(f"Error in precision: {e}")


if __name__ == "__main__":
    main()
