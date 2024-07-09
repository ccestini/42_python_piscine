from typing import Any


def callLimit(limit: int):
    """
    A decorator to limit the number of times a function can be called.

    Args:
        limit (int): The maximum number of allowed calls.

    Returns:
        function: The decorated function with a call limit.
    """
    count = 0

    def callLimiter(function):
        """
        Inner decorator function to apply the call limit.

        Args:
            function: The function to be limited.

        Returns:
            function: The wrapped function with call limit logic.
        """
        def limit_function(*args: Any, **kwargs: Any):
            """
            Function to check the call limit and execute the function.

            Args:
                *args: Positional arguments for the wrapped function.
                **kwargs: Keyword arguments for the wrapped function.

            Returns:
                Any: The return value of the wrapped function.
            """
            nonlocal count
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
"""


def main():
    """Main function to test."""
    try:
        @callLimit(3)
        def f():
            print("f()")

        @callLimit(1)
        def g():
            print("g()")

        for i in range(3):
            f()
            g()

    except Exception as msg:
        print(f"An error occurred: {msg}")


if __name__ == "__main__":
    main()
