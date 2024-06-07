import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D array based on start and end indices.

    Args:
    family (list): A 2D list representing the array.
    start (int): The start index for slicing.
    end (int): The end index for slicing.

    Returns:
    list: The truncated 2D array.
    """

    # Exceptions
    if not isinstance(family, list) or not all(isinstance(row, list)
                                               for row in family):
        raise ValueError("First param must be a 2D list (list of lists).")
    if not all(len(row) == len(family[0]) for row in family):
        raise ValueError("All sublists must be of the same size.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Second and Third params must be integers.")

    # Convert the list to a NumPy array
    family_array = np.array(family)
    # Print the shape of the original array
    print(f"My shape is : {family_array.shape}")
    # Perform the slicing
    truncated_array = family_array[start:end]
    # Print the shape of the truncated array
    print(f"My new shape is : {truncated_array.shape}")
    # Convert the truncated array back to a list and return it
    return truncated_array.tolist()


"""
** shape is an attribute of a NumPy array that returns a
tuple representing the dimensions of the array.
For example, if family_array is a 4x2 array,
family_array.shape would return (4, 2), indicating 4 rows and 2 columns.

** Slicing in NumPy: syntax family_array[start:end]
slices the array along its first axis (rows in a 2D array).
start is the index where slicing begins,
and end is the index where slicing ends (not inclusive).
Negative indices count from the end of the array,
so -2 refers to the second last element, and -1 the last elem.
"""
