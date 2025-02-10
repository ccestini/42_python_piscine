from train import load_data
from predict import load_trained_model, estimate_price

# Constants
DATA_FILE_PATH = './data.csv'
MODEL_FILE_PATH = './model.txt'

# Colors
MAGENTA = '\033[95m'
RED = '\033[91m'
ENDC = '\033[0m'


def calculate_mae(predictions, targets):
    """
    Calculate the Mean Absolute Error (MAE).
    Args:
        predictions: List of predicted values.
        targets: List of actual values.
    Return:
        Mean Absolute Error.
    """
    n = len(predictions)
    mae = sum(abs(predictions[i] - targets[i]) for i in range(n)) / n
    return mae


def main():
    try:
        mileage, actual_prices = load_data(DATA_FILE_PATH)
        theta_0, theta_1 = load_trained_model()
        if not theta_0 and not theta_1:
            raise ValueError("Model not found. Please train the model first.")
        predicted_prices = [estimate_price(theta_0, theta_1, m)
                            for m in mileage]
        mae = calculate_mae(predicted_prices, actual_prices)
        mean_actual_price = sum(actual_prices) / len(actual_prices)
        mae_percentage = (mae / mean_actual_price) * 100
        accuracy = 100 - mae_percentage

        print(f"\n{MAGENTA}Model Evaluation Results:{ENDC}")
        print(f"{MAGENTA}------------------------------------------{ENDC}")
        print(f"Mean Absolute Error (MAE): ${mae:.2f}")
        print(f"Accuracy of the Model: {accuracy:.2f}%")
        print(f"{MAGENTA}------------------------------------------{ENDC}")

    except Exception as e:
        print(f"\n{RED}Error in precision: {ENDC}{e}")


if __name__ == "__main__":
    main()
