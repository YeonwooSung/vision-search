from concurrent.futures import ThreadPoolExecutor
import numpy as np

# custom module
from .feature_extractor import FeatureExtractor

class ThreadPoolEngine:
    def __init__(self, model: str = "resnet34", device: str = "cpu", img_size: int = 224) -> None:
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.feature_extractor = FeatureExtractor(model_path=model, device=device, img_size=img_size)

    def run_engine(self, image: np.ndarray) -> np.ndarray:
        return self.executor.submit(self.feature_extractor.get_image_features, image).result()

    async def arun_engine(self, images: np.ndarray) -> np.ndarray:
        return await self.executor.submit(self.feature_extractor.get_image_features, images)
