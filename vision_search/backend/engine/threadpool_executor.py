from concurrent.futures import ThreadPoolExecutor
import numpy as np

# custom module
from .feature_extractor import CLIPFeatureExtractor


class MultimodalThreadPoolEngine:
    def __init__(self, model: str = "openai/clip-vit-large-patch14", device: str = "cpu", img_size: int = 224) -> None:
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.feature_extractor = CLIPFeatureExtractor(model_path=model, device=device, img_size=img_size)

    def run_engine_img(self, image: np.ndarray) -> np.ndarray:
        return self.executor.submit(self.feature_extractor.get_image_features, image).result()

    def run_engine_text(self, text: str) -> np.ndarray:
        return self.executor.submit(self.feature_extractor.get_text_features, text).result()

    async def arun_engine_img(self, images: np.ndarray) -> np.ndarray:
        return await self.executor.submit(self.feature_extractor.get_image_features, images)

    async def arun_engine_text(self, texts: str) -> np.ndarray:
        return await self.executor.submit(self.feature_extractor.get_text_features, texts)
