
# custom module
from .threadpool_executor import ThreadPoolEngine

def get_engine(model: str = "resnet34", device: str = "cpu", img_size: int = 224):
    return ThreadPoolEngine(model=model, device=device, img_size=img_size)
