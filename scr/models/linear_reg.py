from abc import ABC, abstractmethod
import numpy as np
import numpy.typing as npt

class BaseModel(ABC):
    '''Abstract interface for providing uniformity for all the models in project'''

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass

class LinearRegression(BaseModel):
    '''Realisation of the linear regression model'''

    def __init__(self):
        pass