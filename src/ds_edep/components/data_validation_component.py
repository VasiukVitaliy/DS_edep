import pandas as pd
from src.ds_edep.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_column(self) -> bool:
        try:
            validation_status = True
            data = pd.read_csv(self.config.unzip_data)

            current_schema = {col: str(dtype) for col, dtype in data.dtypes.to_dict().items()}
            expected_schema = self.config.schema

            if current_schema != expected_schema:
                validation_status = False

            with open(self.config.STATUS_FILE, 'w', encoding="utf-8") as f:
                f.write(f"Validation status: {validation_status}")
                
            return validation_status
            
        except Exception as e:
            raise e