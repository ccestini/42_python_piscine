from typing import Any


def ft_mean(data: list[float]) -> float:
    """Calculate the mean of a list of numbers."""
    mean = sum(data) / len(data)
    return mean


def ft_median(data: list[float]) -> float:
    """Calculate the median of a list of numbers."""
    n = len(data)
    sorted_data = sorted(data)
    if n % 2 == 1:  # if odd take the middle value
        median = sorted_data[n // 2]
    else:  # if even take 2 middles
        mid1 = sorted_data[(n // 2) - 1]
        mid2 = sorted_data[n // 2]  # // to result int and round down
        median = (mid1 + mid2) / 2
    return median


def ft_quartiles(data: list[float]) -> list[float]:
    """Calculate the first and third quartiles of a list of numbers."""
    n = len(data)
    sorted_data = sorted(data)
    q1 = sorted_data[int(n * 0.25)]  # access elem at index corresp to 25%
    q3 = sorted_data[int(n * 0.75)]
    return [q1, q3]


def ft_variance(data: list[float]) -> float:
    """Calculate the variance of a list of numbers."""
    n = len(data)
    data_mean = ft_mean(data)
    var = sum((value - data_mean) ** 2 for value in data) / n
    return var


def ft_std_deviation(data: list[float]) -> float:
    """Calculate the standard deviation of a list of numbers."""
    variance_value = ft_variance(data)
    std = variance_value ** 0.5  # square root (** 0.5) of variance
    return std


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate and print statistics based on provided *args and **kwargs.

    *args: A variable number of arguments containing numerical data.
    **kwargs: Keyword arguments specifying the statistics to calculate.
        Supported keys: 'mean', 'median', 'quartile', 'std', 'var'.
    """
    try:
        if not args or not kwargs:  # if any arg passed
            raise ValueError()
        data = [float(arg) for arg in args]  # if all numbers

        for calculation in kwargs.values():
            if calculation == 'mean':
                print(f"mean : {ft_mean(data)}")
            elif calculation == 'median':
                print(f"median : {ft_median(data)}")
            elif calculation == 'quartile':
                print(f"quartile : {ft_quartiles(data)}")
            elif calculation == 'std':
                print(f"std : {ft_std_deviation(data)}")
            elif calculation == 'var':
                print(f"var : {ft_variance(data)}")
            else:
                print("ERROR")

    except Exception:  # all expeptions print this
        print("ERROR")


"""
Statistics:
-> Mean: Represents the average of a set of numbers.
-> Median: Is the middle value in a sorted list of numbers.
-> Quartile: Divides a dataset into four equal parts, with the first quartile
 (Q1) being the value at the 25th percentile and the third quartile (Q3)
 being the value at the 75th percentile.
-> Standard Deviation (std): Measures the spread of data around the mean.
 A lower standard deviation indicates that the data points tend to be close
 to the mean, while a higher standard deviation indicates that they are
 spread out over a wider range of values.
-> Variance (var): Measures how far each number in a dataset is from the mean.
 It is the average of the squared differences from the mean.

In Python, 'Any' is a special type hint provided by the typing module,
 indicating that a variable can be of any type. It is part of type hinting
 and type checking mechanisms to help developers specify and understand the
 expected types of variables in functions, classes, etc.
On the other hand, 'any' is a built-in Python function that returns True
 if at least one element of the iterable is true. If the iterable is empty,
 it returns False.
"""


def main():
    ft_statistics(1, 42, 36, 11, 64, 71, 90, 100, x="mean",
                  y="median", z="quartile", i="std", j="var")
    print("-----")
    ft_statistics(x="mean", y="median", z="quartile")
    print("-----")
    ft_statistics(2, 4, 6)


if __name__ == "__main__":
    main()
