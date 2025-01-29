def load_model(filename="./data.csv"):
    """Load trained model parameters from a file."""
    with open(filename, "r") as file:
        theta0 = float(file.readline().strip())
        theta1 = float(file.readline().strip())
    return theta0, theta1

def estimate_price(mileage, theta0, theta1):
    """Calculate estimated price based on mileage and trained parameters."""
    return theta0 + (theta1 * mileage)

if __name__ == "__main__":
    theta0, theta1 = load_model()
    
    mileage = input("Enter car mileage: ")
    try:
        mileage = float(mileage)
        price = estimate_price(mileage, theta0, theta1)
        print(f"Estimated price: {price:.2f}")
    except ValueError:
        print("Error: Please enter a valid numeric mileage.")
