
class calculator:
    """Calculator to perform arithmetic operations (+ - * /) on a vector."""
    def __init__(self, vector):
        """Calculator Constructor"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Adds a scalar (object) to each element of the vector"""
        self.vector = [x + object for x in self.vector]
        # list comprehension that iterates over each element x in vector
        print(self.vector)

    def __mul__(self, object):
        """"Multiplies each elem of the vector by a scalar (object)"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object):
        """Subtracts a scalar (object) from each element of the vector"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object):
        """Divides each element of the vector by a scalar (object)"""
        if object == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        self.vector = [x / object for x in self.vector]
        print(self.vector)


"""
Add a scalar to a vector means adding the scalar to each elem of the vector.
Example: [0.0, 1.0, 2.0] + 5 becomes [5.0, 6.0, 7.0].

Special method names are denoted by double underscores (__) at the beginning
 and end of the method name:
__add__ corresponds to the + operator (object1 + object2)
__sub__ corresponds to the - operator (object1 - object2)
__mul__ corresponds to the * operator (object1 * object2)
__truediv__ corresponds to the / operator (object1 / object2)
"""


def main():
    try:
        v1 = calculator([2, 5, 7])
        v1 + 1
        print("---")

        v2 = calculator([1, 10, 12])
        v2 * 2
        print("---")

        v3 = calculator([9, 99, 102])
        v3 - 1
        print("---")

        v4 = calculator([10, 15, 20.0])
        v4 / 0

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
