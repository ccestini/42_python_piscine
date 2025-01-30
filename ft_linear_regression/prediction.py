import os

def estimatePrice(theta_0, theta_1, mileage):
    """
    Estimate the price based on the linear regression model: 
    estimatePrice = theta_0 + (theta_1 * mileage).

    Args:
    - theta_0 (float): Intercept term (bias).
    - theta_1 (float): Slope term (coefficient).
    - mileage (float): Mileage of the car.

    Returns:
    - predicted_price (float): Predicted price of the car.
    """
    return theta_0 + (theta_1 * mileage)

def load_trained_model():
    """
    Loads the trained parameters (theta_0, theta_1) from a saved file.
    
    Returns:
        tuple: (theta_0, theta_1)
        Trained parameters or (0, 0) if no model file is found.
    """
    try:
        if os.path.exists('trained_model.txt'):
            with open('trained_model.txt', 'r') as file:
                theta_0, theta_1 = map(float, file.readline().split())
            return (theta_0, theta_1)
        else:
            print("Trained model not found. Using default values (theta_0 = 0 and theta_1 = 0).")
            return (0, 0)
    except Exception as e:
        print(f"Error loading trained model: {e}")
        return (0, 0)

def main():
    # Load the trained model (theta_0, theta_1)
    theta_0, theta_1 = load_trained_model()

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
        print(f"Estimated price for a car with {mileage:.2f} km is ${predicted_price:.2f}")
    except ValueError:
        print("Invalid input, accepts only positive numbers. Exiting the program.")

if __name__ == "__main__":
    main()

"""
-> Intercept (θ₀):
This is the starting value of the price when the mileage is 0 km.
It represents the baseline price of a car before considering mileage.
In a graph, it's where the line crosses the y-axis (price-axis).
-> Slope (θ₁):
This represents the rate of change of the price with respect to mileage.
If θ₁ is negative, it means price decreases as mileage increases (which makes sense for a used car).
If θ₁ is positive, it means price increases as mileage increases (not expected in this case).
It determines how steep or flat the line is.
"""
