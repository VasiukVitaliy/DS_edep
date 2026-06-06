from src.ds_edep.constants import *
from src.ds_edep.utils.common import read_yaml, create_directories
from src.ds_edep.entity.config_entity import DataIngestionConfig

class ConfigManager:
    def __init__(self,
                 config_path = CONFIG_FILE_PATH,
                 params_path = PARAMS_FILE_PATH,
                 schema_path = SCHEMA_FILE_PATH):
        self.config_path = read_yaml(config_path)
        self.params_path = read_yaml(params_path)
        schema_path = read_yaml(schema_path)
        
        create_directories([self.config_path.artifacts_root])
        
    def get_data_ingestion_config(self):
        config = self.config_path.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir

        )
        return data_ingestion_config
        