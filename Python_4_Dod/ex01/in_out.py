def square(x: int | float) -> int | float:
    """Returns the square of the input number x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns the power of the input number x to itself."""
    return x ** x  # exponentiation of x by itself


def outer(x: int | float, function) -> object:
    """
    Returns an object that when called, computes the result of function(x).
    """
    result = x  # keep track of the result of the function

    def inner() -> float:  # define function
        nonlocal result
        # nonlocal is used to declare that result refers var defined in the
        # enclosing scope (outer function), not a local variable (like global)
        result = function(result)  # update the result
        return result

    return inner


"""
-> The outer function is designed to return a nested function (inner) that,
 when called, applies a given function (function) to an initial value (x)
 and keeps track of the result. Each subsequent call to the inner function
 will use the result of the previous call as the new input.
-> Each call to outer updates result by applying function (square or pow)
 to the current value.
"""


def main():
    """Main function to test."""
    try:
        print(square(4))  # 16
        print("-----")
        print(pow(4))  # 256
        print("-----")

        counter = outer(2, square)
        print(counter())  # First call: square(2) = 4
        print(counter())  # Second call: square(4) = 16
        print(counter())  # Third call: square(16) = 256
        print("-----")

        counter2 = outer(2, pow)
        print(counter2())
        print(counter2())

    except Exception as msg:
        print(f"An error occurred: {msg}")


if __name__ == "__main__":
    main()
