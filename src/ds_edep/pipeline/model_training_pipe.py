from src.ds_edep.utils.common import main_logger
from src.ds_edep.config.configuration import ConfigManager
from src.ds_edep.components.model_trainning_component import ModelTrainer

STAGE_NAME="Model Training Stage"

class ModelTrainingPipeline:
    def train_model(self):
        config = ConfigManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

if __name__ == "__main__":
    try:
        main_logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj =ModelTrainingPipeline()
        status = obj.train_model()
        main_logger.info(f">>>>>> stage {STAGE_NAME} completed. Validation status {status} <<<<<<\n\nx==========x")
    except Exception as e:
        main_logger.exception(e)
        raise e