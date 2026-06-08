import pandas as pd
from sklearn.linear_model import ElasticNet
import os
import joblib

class ModelTrainer:
    def __init__(self, config):
        self.config = config
        
    def train(self):
        train_data = pd.read_csv(self.config.train_data)
        
        X_train = train_data.drop(columns=[self.config.target_column])
        y_train = train_data[self.config.target_column]
        
        model = ElasticNet(l1_ratio= self.config.l1_ratio, alpha=self.config.alpha)
        model.fit(X_train, y_train)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))