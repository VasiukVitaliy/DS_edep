from src.ds_edep import main_logger
from src.ds_edep.pipeline.data_ingestion_pipe import DataIngestionTrainingPipeline
from src.ds_edep.pipeline.data_validation_pipe import DataValidationPipeline
from src.ds_edep.pipeline.data_transform_pipe import DataTransformtionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    main_logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    main_logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        main_logger.exception(e)
        raise e
    
STAGE_NAME="Data Validation Stage"
try:
    main_logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj =DataValidationPipeline()
    status = obj.validate_data_schema()
    main_logger.info(f">>>>>> stage {STAGE_NAME} completed. Validation status {status} <<<<<<\n\nx==========x")
except Exception as e:
    main_logger.exception(e)
    raise e

STAGE_NAME="Data Transform Stage"
try:
    main_logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformtionTrainingPipeline()
    obj.transform_data()
    main_logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    main_logger.exception(e)
    raise e