from src.ds_edep.config.configuration import ConfigManager
from src.ds_edep.components.data_ingestion_component import DataIngestion
from src.ds_edep.utils.common import main_logger

STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_ingestion(self):
        config=ConfigManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_zip_file()
    
    
if __name__ == "__main__":
    try:
        main_logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        main_logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        main_logger.exception(e)
        raise e