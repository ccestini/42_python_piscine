# Constants
MAX_KM_INPUT = 900000
MODEL_FILE_PATH = './model.txt'


def load_trained_model():
    """
    Load the trained model parameters from a file.
    Return: List containing theta_0, theta_1, max_mileage, and min_mileage.
    """
    try:
        with open(MODEL_FILE_PATH, 'r') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
            if not lines or len(lines) != 4:
                raise ValueError("model.txt must contain: theta 0, "
                                 "theta 1, max mileage, and min mileage.")
            theta_0 = float(lines[0].strip())
            theta_1 = float(lines[1].strip())
            max_mileage = float(lines[2].strip())
            min_mileage = float(lines[3].strip())
            if max_mileage <= 0 or min_mileage < 0 or \
               max_mileage <= min_mileage:
                raise ValueError("Invalid max_mileage and/or min_mileage in "
                                 "model.txt.")
            return [theta_0, theta_1, max_mileage, min_mileage]
    except Exception as e:
        print(f"Error in Model: {e}\nUsing theta_0 = 0 and theta_1 = 0.")
        return [0, 0, 1, 0]  # Default values, max km=1 to avoid division by 0


def estimate_price(theta_0, theta_1, mileage, max_mileage, min_mileage):
    """
    Estimate the price of a car based on its mileage using a linear
    regression model.
    Args:
        theta_0: Intercept of the regression model.
        theta_1: Slope of the regression model.
        mileage: Mileage of the car.
        max_mileage: Maximum mileage used for normalization.
        min_mileage: Minimum mileage used for normalization.
    Return: Estimated price of the car.
    """
    normalized_mileage = (mileage - min_mileage) / (max_mileage - min_mileage)
    price = theta_0 + (theta_1 * normalized_mileage)
    return max(price, 0)  # Ensure the price is not negative


def main():
    theta_0, theta_1, max_mileage, min_mileage = load_trained_model()
    while True:
        try:
            mileage_input = input("Enter the mileage of the car (in km) or "
                                  "type 'exit' to quit: ")
            if mileage_input.lower() == 'exit':
                print("Exiting the program.")
                break
            mileage = float(mileage_input)
            if mileage < 0:
                print("Error: Invalid Input. Negative km is not accepted.")
                continue
            if mileage > MAX_KM_INPUT:
                print(f"If km is greater than {MAX_KM_INPUT} km, then "
                      f"scrap the car!")
                continue
            predicted_price = estimate_price(theta_0, theta_1, mileage,
                                             max_mileage, min_mileage)
            print(f"Estimated price for a car with {mileage:.0f} km is "
                  f"${predicted_price:.2f}")
            break
        except ValueError:
            print(f"Error: Invalid Input. Use a valid number between 0 to "
                  f"{MAX_KM_INPUT} km.")
        except Exception as e:
            print(f"Error in predicting price: {e}")


if __name__ == "__main__":
    main()
