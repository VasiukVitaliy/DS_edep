import joblib
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self, path: Path):
        self.model = joblib.load(path)
        
    def predict(self, data):
        return self.model.predict(data)