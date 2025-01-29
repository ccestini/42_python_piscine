import csv

def load_data(filename):
    """Load mileage and price data from a CSV file."""
    mileage = []
    price = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if present
        for row in reader:
            mileage.append(float(row[0]))  # Convert mileage to float
            price.append(float(row[1]))    # Convert price to float
    return mileage, price

def estimate_price(mileage, theta0, theta1):
    """Calculate estimated price based on mileage and learned parameters."""
    return theta0 + theta1 * mileage

def train_model(mileage, price, learning_rate=0.01, epochs=1000):
    """Train the model using gradient descent."""
    theta0, theta1 = 0.0, 0.0
    m = len(mileage)

    for _ in range(epochs):
        sum_errors0 = sum(estimate_price(mileage[i], theta0, theta1) - price[i] for i in range(m))
        sum_errors1 = sum((estimate_price(mileage[i], theta0, theta1) - price[i]) * mileage[i] for i in range(m))

        tmp_theta0 = learning_rate * (1/m) * sum_errors0
        tmp_theta1 = learning_rate * (1/m) * sum_errors1

        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

    return theta0, theta1

def save_model(theta0, theta1, filename="model.txt"):
    """Save the trained model parameters to a file."""
    with open(filename, "w") as file:
        file.write(f"{theta0}\n{theta1}")

if __name__ == "__main__":
    mileage, price = load_data("data.csv")  # Update with your actual dataset filename
    theta0, theta1 = train_model(mileage, price)
    save_model(theta0, theta1)
    print(f"Training complete! Model saved with theta0 = {theta0}, theta1 = {theta1}")
