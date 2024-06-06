import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculates the BMI for a list of heights and weights.
    Body Mass Index (BMI) is one way to measure body size.
    
    Args:
    height (list[int | float]): List of heights.
    weight (list[int | float]): List of weights.
    
    Returns:
    list[int | float]: List of BMI values.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same size.")
    if not all(isinstance(h, (int, float)) for h in height):
        raise ValueError("Height list must contain only integers or floats.")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise ValueError("Weight list must contain only integers or floats.")
    
    height_array = np.array(height)
    weight_array = np.array(weight)
    
    bmi_array = weight_array / (height_array ** 2)
    return bmi_array.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if each BMI value is above a given limit.
    
    Args:
    bmi (list[float]): List of BMI values.
    limit (int): Limit to compare BMI values against.
    
    Returns:
    list[bool]: List of booleans where True indicates BMI is above the limit.
    """
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise ValueError("BMI list must contain only integers or floats.")
    
    return [b > limit for b in bmi]
