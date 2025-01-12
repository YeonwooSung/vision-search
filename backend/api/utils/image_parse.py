import tempfile
from PIL import Image
import smart_open
from io import BytesIO
import numpy as np


def save_as_tempfile(image):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    temp_file.write(image.read())
    temp_file.close()
    return temp_file.name


def load_image_into_numpy_array(data):
    return np.array(Image.open(BytesIO(data)))

def pil_loader(image_file):
    with Image.open(image_file) as image:
        return image.convert("RGB")

def load_image_from_url(image_url):
    with smart_open.open(image_url, "rb") as image_file:
        return pil_loader(image_file)
