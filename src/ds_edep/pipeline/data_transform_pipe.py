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
        try:
            with open(cfg.status_data, "r") as file:
                data = file.read()
                status = data.split(" ")[-1]
                if status.strip().lower() == "true":
                    transformer = DataTranform(cfg)
                    transformer.splitting_data()
                else:
                    main_logger.warning("Data didn't pass tests. Kill pipeline")
                    raise Exception("Killed the process: dont pass validation test")
        except FileNotFoundError:
            main_logger.error("Status file not found! Run data validation first or check the status file path in config.")
        
if __name__ == "__main__":
    try:
        main_logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformtionTrainingPipeline()
        obj.transform_data()
        main_logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        main_logger.exception(e)
        raise e