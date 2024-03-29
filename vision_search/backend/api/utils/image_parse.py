import tempfile
from PIL import Image
from io import BytesIO
import numpy as np


def save_as_tempfile(image):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    temp_file.write(image.read())
    temp_file.close()
    return temp_file.name


def load_image_into_numpy_array(data):
    return np.array(Image.open(BytesIO(data)))
