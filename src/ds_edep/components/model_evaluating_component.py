import numpy as np
import pandas as pd
import joblib
import mlflow
from urllib.parse import urlparse
from pathlib import Path
from src.ds_edep.entity.config_entity import ModelEvaluatingConfig
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.ds_edep.utils.common import save_json

class ModelEvaluating:
    def __init__(self, config: ModelEvaluatingConfig):
        self.config = config
        
    def evaluate_model(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_metrics_mlflow(self):
        cfg = self.config
        test_data = pd.read_csv(cfg.test_data_path)
        model = joblib.load(cfg.model_path)
        
        X_test = test_data.drop(columns= [cfg.target_column])
        y_test = test_data[cfg.target_column]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            predict_vals = model.predict(X_test)
            rmse, mae, r2 = self.evaluate_model(y_test, predict_vals)
            
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)
            
            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)
            
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticModel")
            else:
                mlflow.sklearn.log_model(model, "model")