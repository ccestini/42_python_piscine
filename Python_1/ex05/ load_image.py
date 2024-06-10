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
        with Image.open(path) as img:
            if img.format not in ['JPEG', 'JPG']:
                raise ValueError(f"Unsupported image format: {img.format}")
            img_rgb = img.convert('RGB')
            img_array = np.array(img_rgb)
            return img_array

    except FileNotFoundError:
        raise ValueError(f"File not found: {path}")
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")
