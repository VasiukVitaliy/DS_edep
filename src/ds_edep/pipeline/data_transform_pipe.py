from src.ds_edep.config.configuration import ConfigManager
from src.ds_edep.components.data_transformation_component import DataTranform
from src.ds_edep.utils.common import main_logger

STAGE_NAME="Data Transformtion Stage"

class DataTransformtionTrainingPipeline:
    def __init__(self):
        pass
    
    def transform_data(self):
        manager = ConfigManager()
        cfg = manager.get_data_transformation_config()
        transformer = DataTranform(cfg)
        transformer.splitting_data()
        
if __name__ == "__main__":
    try:
        main_logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformtionTrainingPipeline()
        obj.transform_data()
        main_logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        main_logger.exception(e)
        raise e