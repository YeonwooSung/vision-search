import timm
import torch
import numpy as np

# custom module
from backend.utils import Singleton


class FeatureExtractor(metaclass=Singleton):
    def __init__(self, model_path:str="resnet34", device:str="cpu"):
        self.model_path = model_path
        self.device = torch.device(device)
        self.model = timm.create_model(model_path, pretrained=True)
        self.model.to(self.device)
        self.model.eval()

    def extract_features(self, image:np.ndarray, normalize:bool=True):
        # extract features from the image
        with torch.no_grad():
            image = torch.from_numpy(image).unsqueeze(0).to(self.device)
            features = self.model(image)
            features = features.squeeze().cpu().numpy()

        # normalize the features
        if normalize:
            features = features / np.linalg.norm(features)
        return features
