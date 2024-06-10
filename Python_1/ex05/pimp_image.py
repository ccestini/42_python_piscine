from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array) -> array:
#your code here
def ft_red(array) -> array:
#your code here
def ft_green(array) -> array:
#your code here
def ft_blue(array) -> array:
#your code here
def ft_grey(array) -> array:
#your code here

def main():
    try:
        image = ft_load("../animal.jpeg")


    except Exception as message:
        print(f"{type(message).__name__}: {message}")


if __name__ == "__main__":
    main()
