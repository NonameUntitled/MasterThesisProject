import torch

from utils import MetaParent


class BaseModel(metaclass=MetaParent):
    pass


class TorchModel(BaseModel, torch.nn.Module):
    pass
