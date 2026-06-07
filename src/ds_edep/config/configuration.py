from src.ds_edep.constants import *
from src.ds_edep.utils.common import read_yaml, create_directories
from src.ds_edep.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformConfig

class ConfigManager:
    def __init__(self,
                 config_path = CONFIG_FILE_PATH,
                 params_path = PARAMS_FILE_PATH,
                 schema_path = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        self.schema = read_yaml(schema_path)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self):
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir

        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dir])
        
        class_conf = DataValidationConfig(
            root_dir = Path(config.root_dir),
            STATUS_FILE = Path(config.STATUS_FILE),
            unzip_data = Path(config.unzip_data_dir),
            schema = schema  
        )
        
        return class_conf
    
    def get_data_transformation_config(self) -> DataTransformConfig:
        cfg = self.config.data_transformation
        create_directories([cfg.root_dir])
        
        obj_config = DataTransformConfig(root_dir= cfg.root_dir,
                                         data_path = cfg.data_path)
        
        return obj_config
        