import pandas as pd
import os
from sklearn.model_selection import train_test_split
from src.ds_edep.utils.common import main_logger
class DataTranform:
    def __init__(self, config):
        self.config = config
    
    def splitting_data(self):
        data = pd.read_csv(self.config.data_path)
        
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)
        
        main_logger.info("Splited data into training and test sets")
        main_logger.info(train.shape)
        main_logger.info(test.shape)

        print(train.shape)
        print(test.shape)