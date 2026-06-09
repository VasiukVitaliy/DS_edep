from src.ds_edep.config.configuration import ConfigManager
from src.ds_edep.components.model_evaluating_component import ModelEvaluating
from src.ds_edep.utils.common import main_logger

STAGE_NAME="Model Evaluating Stage"

class ModelEvaluatingPipeline:
    def __init__(self):
        pass
    
    def start_evaluating(self):
        try:
            manager = ConfigManager()
            cfg = manager.get_model_evaluating_config()
            evaluator = ModelEvaluating(cfg)
            evaluator.log_metrics_mlflow()
        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        main_logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj =ModelEvaluatingPipeline()
        status = obj.start_evaluating()
        main_logger.info(f">>>>>> stage {STAGE_NAME} completed. Validation status {status} <<<<<<\n\nx==========x")
    except Exception as e:
        main_logger.exception(e)
        raise e