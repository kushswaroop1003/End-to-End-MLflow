import os
from mlproject import logger
from mlproject.entity.__config_entity import DataValidationConfig
import pandas as pd



class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            print("Starting column validation...")

            validation_status = None

            print("CSV File Path:", self.config.unzip_data_dir)

            # Attempt to load the CSV
            data = pd.read_csv(self.config.unzip_data_dir)
            print("Data loaded successfully:\n", data.head())

            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                else:
                    validation_status = True

                # Write status to file
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            print("Error while loading data:", e)
            raise e


