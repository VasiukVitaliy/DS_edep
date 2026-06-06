import os
import urllib.request as request
import zipfile
from src.ds_edep import main_logger
from src.ds_edep.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            main_logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            main_logger.info(f"File already exists")
            
    def unzip_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_file:
            zip_file.extractall(unzip_path)