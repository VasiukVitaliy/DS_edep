from src.ds_edep.utils.common import main_logger
from src.ds_edep.config.configuration import ConfigManager
from src.ds_edep.components.data_validation_component import DataValidation

STAGE_NAME="Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def validate_data_schema(self):
        config = ConfigManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_column()
        
if __name__ == "__main__":
    try:
        main_logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj =DataValidationPipeline()
        status = obj.validate_data_schema()
        main_logger.info(f">>>>>> stage {STAGE_NAME} completed. Validation status {status} <<<<<<\n\nx==========x")
    except Exception as e:
        main_logger.exception(e)
        raise e