from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def zoom_image(image: np.array, x_start: int, x_end: int,
               y_start: int, y_end: int) -> np.array:
    """
    Zooms in on a portion of the image.

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
        zoomed_image = image[y_start:y_end, x_start:x_end]
        zoomed_image = zoomed_image[..., np.newaxis]
        print(f"The shape of image is: {zoomed_image.shape}")
        return zoomed_image
    except Exception as e:
        raise ValueError(f"An error occurred during zooming: {e}")


def display_image(image: np.array, title: str):
    """
    Displays the image with the given title.

    Args:
    image (np.array): The image data.
    title (str): The title of the displayed image.
    """
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('on')
    plt.show()


def transpose_image(image: np.array) -> np.array:
    """
    Transposes the image.

    Args:
    image (np.array): The image data to transpose.

    Returns:
    np.array: The transposed image data.
    """
    transposed = np.zeros((image.shape[1], image.shape[0]), dtype=image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            transposed[j, i] = image[i, j, 0]
    print(f"New shape after Transpose: {transposed.shape}")
    return transposed


def main():
    try:
        image = ft_load("../animal.jpeg")
        image = Image.fromarray(image).convert('L')
        image = np.array(image)

        zoomed_image = zoom_image(image, 450, 850, 100, 500)
        print(zoomed_image)

        transposed_image = transpose_image(zoomed_image)
        print(transposed_image)
        display_image(transposed_image, "Transposed Image")

        # print("Testing with transpose builtin")
        # transpose_builtin = zoomed_image.transpose()
        # print(transpose_builtin)

    except Exception as message:
        print(f"{type(message).__name__}: {message}")


if __name__ == "__main__":
    main()
