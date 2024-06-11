from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Loads an image, prints its format and pixel content in RGB format.

    Args:
    path (str): The path to the image file.

    Returns:
    np.array: The image data in RGB format.
    """
    try:

        # Open the image file, with a context manager, which is a way to
        # ensure that resources are properly managed and cleaned up after use
        # not having to use img.close().
        with Image.open(path) as img:
            # Check if the image format is supported, not all formats
            # are supported by pillow package so I left only required in subj
            if img.format not in ['JPEG', 'JPG']:
                raise ValueError(f"Unsupported image format: {img.format}")

            # Convert image to RGB format
            img_rgb = img.convert('RGB')

            # Convert the image data to a NumPy array
            img_array = np.array(img_rgb)

            # Print the shape of the image
            print(f"The shape of image is: {img_array.shape}")

            # Return the image data
            return img_array

    except FileNotFoundError:
        raise ValueError(f"File not found: {path}")
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")
