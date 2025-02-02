import os


def load_trained_model():
    try:
        with open('trained_model.txt', 'r') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]  # Ignore empty lines
            if not lines or len(lines) != 3:
                print("Error: trained_model.txt must contain: theta_0, theta_1 and max_mileage.\nUsing thetas = 0.")
                return 0, 0, 1  # Default values to prevent errors
            theta_0 = float(lines[0].strip())  # Used for normalization
            theta_1 = float(lines[1].strip())
            max_mileage = float(lines[2].strip()) 
            if max_mileage <= 0:
                print("Error: Invalid max_mileage in trained_model.txt (must be > 0).\nUsing thetas = 0.")
                return 0, 0, 1 
            return theta_0, theta_1, max_mileage

    except FileNotFoundError:
        print("Trained_model.txt not found.\nUsing thetas = 0.")
        return 0, 0, 1  # max_mileage=1 simply to avoid division by zero
    except ValueError:
        print("Trained_model.txt contains invalid data.\nUsing thetas = 0.")
        return 0, 0, 1
    except Exception as e:
        print(f"Error: {e}. Using thetas = 0.")
        return 0, 0, 1


def estimatePrice(theta_0, theta_1, mileage, max_mileage):
    normalized_mileage = mileage / max_mileage
    return theta_0 + (theta_1 * normalized_mileage)


def main():
    theta_0, theta_1, max_mileage = load_trained_model()
    try:
        mileage_input = input("Enter the mileage of the car (in km): ")
        mileage = float(mileage_input)
        if mileage < 0:
            print("Error: Invalid input, use only positive numbers.\nExiting...")
            return
        if mileage > 900000:
            print("If km is greater than 900000 km, then scrap the car.\nExiting...")
            return
        predicted_price = estimatePrice(theta_0, theta_1, mileage, max_mileage)
        print(f"Estimated price for a car with {mileage:.2f} km is ${predicted_price:.2f}")
    except ValueError:
        print("Error: Try again using a valid number between 0 to 900000 km.\nExiting...")


if __name__ == "__main__":
    main()
