from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def zoom_image(image: np.array, x_start: int, x_end: int,
               y_start: int, y_end: int) -> np.array:
    """
    Zooms in on a portion of the image in grayscale.

    Args:
    image (np.array): The image data.
    x_start (int): The starting x coordinate.
    x_end (int): The ending x coordinate.
    y_start (int): The starting y coordinate.
    y_end (int): The ending y coordinate.

    Returns:
    np.array: The zoomed-in image data.
    """
    try:
        zoomed_image = image[y_start:y_end, x_start:x_end, 0:1]
        # slicing row:col
        # Height (y-axis) corresponds to rows and Width (x-axis) to columns
        # Param 0:1, indicates that it is selecting only first channel (red),
        # it produce an image that resembles a grayscale representation.
        print(f"New shape after slicing: {zoomed_image.shape}")
        return zoomed_image
    except Exception as e:
        raise ValueError(f"An error occurred during zooming: {e}")


def display_image(image: np.array, title: str):
    """
    Displays the image with the given title in grayscale.

    Args:
    image (np.array): The image data.
    title (str): The title of the displayed image.
    """
    # cmap is colormap and cmap='gray' displays the image in grayscale.
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('on')
    plt.show()


def main():
    try:
        image = ft_load("../animal.jpeg")
        print(image)

        zoomed_image = zoom_image(image, 450, 850, 100, 500)
        print(zoomed_image)
        display_image(zoomed_image, "Zoomed Image")

    except Exception as message:
        print(f"{type(message).__name__}: {message}")


if __name__ == "__main__":
    main()


"""
**RGB image shape (height, width, color channels).
Subject output expects shape (400, 400, 1),
Height and Width: The first two numbers, 400 and 400, indicate that the image
is 400 pixels tall and 400 pixels wide.
Single Channel: The last number, 1, indicates that there is only one channel,
which corresponds to the grayscale values.
There is also Four Channels: Red, Green, Blue, and Alpha (transparency).

** Modes in PIL/Pillow:
'L' Mode: luminance. In this mode, the image is converted to grayscale,
which means that each pixel is represented by a single byte (8 bits)
indicating the light intensity. The value ranges from 0 (black) to 255 (white).
"""
