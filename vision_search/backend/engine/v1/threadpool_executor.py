from concurrent.futures import ThreadPoolExecutor
import numpy as np

# custom module
from .feature_extractor import FeatureExtractor


class ThreadPoolEngine:
    def __init__(self, model: str = "resnet34", device: str = "cpu", img_size: int = 224) -> None:
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.feature_extractor = FeatureExtractor(model_path=model, device=device, img_size=img_size)

    def run_engine(self, image: np.ndarray) -> np.ndarray:
        return self.feature_extractor.get_image_features(image)

    async def arun_engine(self, images: np.ndarray) -> np.ndarray:
        return await self.executor.submit(self.feature_extractor.get_image_features, images)


    def run_engine_with_query(self, image: np.ndarray, query: str) -> np.ndarray:
        image_features = self.feature_extractor.get_image_features(image)
        text_features = self.feature_extractor.get_text_features(query)
        return np.concatenate((image_features, text_features), axis=1)
    
    async def arun_engine_with_query(self, image: np.ndarray, query: str) -> np.ndarray:
        image_features = await self.executor.submit(self.feature_extractor.get_image_features, image)
        text_features = await self.executor.submit(self.feature_extractor.get_text_features, query)
        return np.concatenate((image_features, text_features), axis=1)
