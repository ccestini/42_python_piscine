from PIL import Image
import numpy as np
from pimp_image import ft_display_image


def ft_load(path: str) -> np.array:
    """
    Loads an image, prints its format and pixel content.
    Args:
    path (str): The path to the image file.
    Returns:
    np.array: The image data array in RGB format.
    """
    try:
        with Image.open(path) as img:
            if img.format not in ['JPEG', 'JPG']:
                raise ValueError(f"Unsupported image format: {img.format}")
            img_rgb = img.convert('RGB')
            img_array = np.array(img_rgb)
            print(f"The shape of image is: {img_array.shape}")
            print(img_array)
            ft_display_image(img_array, "Original")
            return img_array
    except FileNotFoundError:
        raise ValueError(f"File not found: {path}")
    except Exception as e:
        raise ValueError(f"An error occurred during loading the image: {e}")
