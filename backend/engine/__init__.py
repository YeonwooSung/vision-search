
# custom module
from .threadpool_executor import MultimodalThreadPoolEngine


def get_engine(model: str = "openai/clip-vit-large-patch14", device: str = "cpu", img_size: int = 224):
    return MultimodalThreadPoolEngine(model=model, device=device, img_size=img_size)
