from deep_classifier import logger
from deep_classifier.constants import *
from deep_classifier.utility.common import read_yaml_file
from deep_classifier.entity.config_entity import Training_Pipeline_Config,Data_Ingestion_Config
from pathlib import Path
import os

class Configuration:

    def __init__(self,config_file_path=CONFIG_FILE_PATH,timestamp:str=CURRENT_TIMESTAMP):
        try:
            self.config_info=read_yaml_file(file_path=Path(config_file_path))
            self.traning_pipeline_config=self.get_traning_pipeline_config()
            self.time_stamp=timestamp
        except Exception as e:
            raise e

    def get_traning_pipeline_config(self)->Training_Pipeline_Config:
        try:
            training_pipeline_config_info=self.config_info.training_pipeline_config
            artifact_dir=os.path.join(ROOT_DIR,
                                      training_pipeline_config_info.pipeline_name,
                                      training_pipeline_config_info.artifact_dir)
            training_pipeline_config=Training_Pipeline_Config(artifacr_dir=artifact_dir)
            logger.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise e
    
    def get_data_ingestion_config(self)->Data_Ingestion_Config:
        try:
            data_ingestion_config_info=self.config_info.data_ingestion_config
            artifact_dir=self.traning_pipeline_config.artifacr_dir
            data_ingestion_artifact_dir=os.path.join(artifact_dir,
                                                     data_ingestion_config_info.data_ingestion_dir)
            dataset_download_url=data_ingestion_config_info.dataset_download_url
            raw_data_dir=os.path.join(data_ingestion_artifact_dir,
                                      data_ingestion_config_info.raw_data_dir)
            extracted_data_dir=os.path.join(data_ingestion_artifact_dir,
                                            data_ingestion_config_info.extracted_data_dir)
            traning_data_dir=os.path.join(data_ingestion_artifact_dir,
                                          data_ingestion_config_info.ingested_train_dir)
            testing_data_dir=os.path.join(data_ingestion_artifact_dir,
                                          data_ingestion_config_info.ingested_test_dir)

            data_ingestion_config=Data_Ingestion_Config(data_ingestion_dir=data_ingestion_artifact_dir,
                                                        dataset_download_url=dataset_download_url,
                                                        raw_data_dir=raw_data_dir,
                                                        extracted_data_dir=extracted_data_dir,
                                                        ingested_train_dir=traning_data_dir,
                                                        ingested_test_dir=testing_data_dir)
            logger.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise e
