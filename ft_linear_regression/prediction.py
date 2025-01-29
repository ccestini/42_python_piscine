import os

def estimatePrice(theta_0, theta_1, mileage):
    """
    Estimate the price based on the linear regression model: 
    estimatePrice = theta_0 + (theta_1 * mileage).

    Args:
    - theta_0 (float): Intercept term.
    - theta_1 (float): Slope term.
    - mileage (float): Mileage of the car.

    Returns:
    - predicted_price (float): Predicted price of the car.
    """
    predicted_price = theta_0 + (theta_1 * mileage)
    return predicted_price

def load_trained_model():
    """
    Loads the trained parameters (theta_0, theta_1) from a saved file.
    
    Returns:
        tuple: (theta_0, theta_1) - Trained parameters or (0, 0) if no model file is found.
    """
    try:
        if os.path.exists('trained_model.txt'):
            with open('trained_model.txt', 'r') as file:
                theta_0, theta_1 = map(float, file.readline().split())
            return (theta_0, theta_1)  # Return as a tuple
        else:
            print("Trained model not found. Using default values (theta_0 = 0 and theta_1 = 0).")
            return (0, 0)  # Default if file doesn't exist
    except Exception as e:
        print(f"Error loading trained model: {e}")
        return (0, 0)  # Return default values if error occurs

def main():
    # Load the trained model (theta_0, theta_1)
    model_params = load_trained_model()
    
    # Extract theta_0 and theta_1 from the tuple
    theta_0, theta_1 = model_params

    # Ask for mileage input and make the prediction
    try:
        mileage_input = input("Enter the mileage of the car (in km): ")
        if not mileage_input:
            print("Mileage cannot be empty. Exiting the program.")
            return
        mileage = float(mileage_input)
        if mileage < 0:
            print("Invalid input, accepts only positive numbers. Exiting the program.")
            return
        predicted_price = estimatePrice(theta_0, theta_1, mileage)
        print(f"Predicted price for a car with {mileage} km: ${predicted_price:.2f}")
    except ValueError:
        print("Invalid input, accepts only positive numbers. Exiting the program.")

if __name__ == "__main__":
    main()
