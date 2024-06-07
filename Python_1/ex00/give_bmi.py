import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
      -> list[int | float]:
    """
    Calculates the Body Mass Index (BMI) using a list of heights and weights.

    Args:
    height (list[int | float]): List of heights in meters.
    weight (list[int | float]): List of weights in kilograms.

    Returns:
    list[int | float]: List of BMI values.
    """
    # exceptions
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same size.")
    if not all(isinstance(h, (int, float)) for h in height):
        raise ValueError("Height list must contain only integers or floats.")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise ValueError("Weight list must contain only integers or floats.")
    # convert the lists into NumPy arrays
    height_array = np.array(height)
    weight_array = np.array(weight)
    # perform the operation on the entire array
    bmi_array = weight_array / (height_array ** 2)
    # transforming the array back into list
    return bmi_array.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if each BMI value is above a given limit.

    Args:
    bmi (list[int or float]): List of BMI values.
    limit (int): Limit to compare BMI values against.

    Returns:
    list[bool]: List of booleans where True indicates BMI is above the limit.
    """
    # exceptions
    if not all(isinstance(elem, (int, float)) for elem in bmi):
        raise ValueError("BMI list must contain only integers or floats.")
    # return a list by using List Comprehension (concise way to create lists)
    # compares each element in the bmi list with the limit given
    return [elem > limit for elem in bmi]
