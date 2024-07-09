from typing import Any


def callLimit(limit: int):
    """
    A decorator to limit the number of times a function can be called.
    """
    count = 0

    def callLimiter(function):
        """
        Inner decorator function to apply the call limit.
        """
        def limit_function(*args: Any, **kwargs: Any):
            """
            Function to check the call limit and execute the function.
            """
            nonlocal count  # indicates that count is not local variable
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter


"""
Create a decorator callLimit that restricts the number of times a function
 can be called. The decorator will count the number of calls to the
 decorated function and raise an error if the limit is exceeded.

Wrapper generally refers to a design pattern where one function or class
 method modifies the behavior of another function or method. This is
 achieved using decorators or by wrapping one function within another.
"""


def main():
    """Main function to test."""
    try:
        @callLimit(2)
        def example_function():
            print("Example function")

        for i in range(5):
            example_function()

    except Exception as msg:
        print(f"An error occurred: {msg}")


if __name__ == "__main__":
    main()
