import timm
import torch
import numpy as np
from PIL import Image

# custom module
from backend.utils import Singleton


class FeatureExtractor(metaclass=Singleton):
    def __init__(self, model_path:str="resnet34", device:str="cpu", img_size:int=224):
        self.model_path = model_path
        self.device = torch.device(device)
        self.model = timm.create_model(model_path, pretrained=True)
        self.model.to(self.device)
        self.model.eval()
        self.img_size = img_size

    @torch.no_grad()
    def get_image_features(self, image:np.ndarray, normalize:bool=True):
        # resize the image
        image = np.array(Image.fromarray(image).resize((self.img_size, self.img_size)))

        # extract features from the image
        image = torch.from_numpy(image).unsqueeze(0).to(self.device)
        features = self.model(image)
        features = features.squeeze().cpu().numpy()

        # normalize the features
        if normalize:
            features = features / np.linalg.norm(features)
        return features
