from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_zoom_image(image: np.array, x_start: int, x_end: int,
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
        print(f"The shape of image is: {zoomed_image.shape}")
        return zoomed_image
    except Exception as e:
        raise ValueError(f"An error occurred during zooming: {e}")


def ft_display_image(image: np.array, title: str):
    """
    Displays the image with the given title in grayscale.

    Args:
    image (np.array): The image data.
    title (str): The title of the displayed image.
    """
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('on')
    plt.show()


def ft_transpose_image(image: np.array) -> np.array:
    """
    Transposes the image.

    Args:
    image (np.array): The image data to transpose.

    Returns:
    np.array: The transposed image data.
    """
    transposed = np.zeros((image.shape[1], image.shape[0]), dtype=int)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            transposed[j, i] = image[i, j, 0]
            # '0'is to access a single value instead of the entire array
    print(f"New shape after Transpose: {transposed.shape}")
    return transposed


def main():
    try:
        image = ft_load("../animal.jpeg")

        zoomed_image = ft_zoom_image(image, 450, 850, 100, 500)
        print(zoomed_image)

        transposed_image = ft_transpose_image(zoomed_image)
        print(transposed_image)
        ft_display_image(transposed_image, "Transposed Image")

        # print("Testing with transpose builtin")
        # t_builtin = zoomed_image.transpose()
        # # the next line is to transform into 2d (400,400) to compare purposes
        # t_builtin = t_builtin.reshape(t_builtin.shape[1], t_builtin.shape[2])
        # print(f"Shape with built-in Transpose: {t_builtin.shape}")
        # print(t_builtin)

    except Exception as message:
        print(f"{type(message).__name__}: {message}")


if __name__ == "__main__":
    main()
