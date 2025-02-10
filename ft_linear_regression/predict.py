# Constants
MAX_KM_INPUT = 900000
MODEL_FILE_PATH = './model.txt'

# Colors
MAGENTA = '\033[95m'
BLUE = '\033[96m'
RED = '\033[91m'
ENDC = '\033[0m'


def load_trained_model():
    """
    Load the trained model parameters from a file.
    Return: List containing theta_0 and theta_1.
    """
    try:
        with open(MODEL_FILE_PATH, 'r') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
            if not lines or len(lines) != 2:
                raise ValueError("model.txt must contain-> theta 0, "
                                 "theta 1, max mileage, and min mileage.")
            theta_0 = float(lines[0].strip())
            theta_1 = float(lines[1].strip())
            return [theta_0, theta_1]
    except Exception as e:
        print(f"\n{RED}Error in Model:{ENDC} {e}\nUsing theta_0 = 0 "
              f"and theta_1 = 0.")
        return [0, 0]


def estimate_price(theta_0, theta_1, mileage):
    """
    Estimate the price of a car based on its mileage using a linear
    regression model.
    Args:
        theta_0: Intercept of the regression model.
        theta_1: Slope of the regression model.
        mileage: Mileage of the car.
    Return: Estimated price of the car.
    """
    price = theta_0 + (theta_1 * mileage)
    return max(price, 0)  # Ensure the price is not negative


def main():
    theta_0, theta_1 = load_trained_model()
    while True:
        try:
            mileage_input = input("\nEnter the mileage of the car (in km) or "
                                  "type 'exit' to quit: ")
            if mileage_input.lower() == 'exit':
                print(f"\n{BLUE}Goodbye!{ENDC}")
                break
            mileage = float(mileage_input)
            if mileage < 0:
                print(f"\n{RED}Error: {ENDC}Invalid Input. "
                      f"Negative km is not accepted.")
                continue
            if mileage > MAX_KM_INPUT:
                print(f"\n{RED}Error:{ENDC} If mileage is greater than "
                      f"{MAX_KM_INPUT} km, then scrap the car!{ENDC}")
                continue

            predicted_price = estimate_price(theta_0, theta_1, mileage)
            print(f"\n{BLUE}Estimated price for a car")
            print(f"{BLUE}------------------------------------------{ENDC}")
            print(f"With {mileage:.0f} km price is $ {predicted_price:.2f}")
            print(f"{BLUE}------------------------------------------{ENDC}")
            break

        except ValueError:
            print(f"\n{RED}Error: {ENDC}Invalid Input. Use a valid number "
                  f"between 0 to {MAX_KM_INPUT} km.")
        except Exception as e:
            print(f"\n{RED}Error in predicting price: {ENDC}{e}")


if __name__ == "__main__":
    main()
