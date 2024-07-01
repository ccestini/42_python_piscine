class calculator:
    """
    Perform calculations (dot product, addition, subtraction) on vectors.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Computes the dot product of two vectors and prints the result.
        """
        result_list = [(x * y) for x, y in zip(V1, V2)]
        result = sum(result_list)
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds two vectors element-wise and prints the result.
        """
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts the second from the first vector and prints the result.
        """
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")


"""
@staticmethod makes it clear that the methods do not depend on the class or
 instance state and are purely utility functions that operate only on
 their input arguments.

The dot product, also called scalar product, is a measure of how closely
 two vectors align, in terms of the directions they point.

zip() function:
Takes 2 iterables and returns an iterator of tuples.
Each tuple contains elems from the iterables that are at the same position.
V1 = [5, 10, 2]
V2 = [2, 4, 3]
list(zip(V1, V2))  # [(5, 2), (10, 4), (2, 3)]
List Comprehension:
The list comprehension iterates over the tuples produced by zip(V1, V2).
For each tuple (x, y), where x is from V1 and y is from V2, it computes x + y.
The results from each iteration are collected into a new list.
The new list [7, 14, 5].
"""


def main():
    try:
        a = [2, 2, 2.0, 3, 5]
        b = [1, 1, 1, 2, 3]

        calculator.dotproduct(a, b)
        print("---")

        calculator.add_vec(a, b)
        print("---")

        calculator.sous_vec(a, b)

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
