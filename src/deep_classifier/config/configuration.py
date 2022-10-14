import tensorboard
from deep_classifier import logger
from deep_classifier.constants import *
from deep_classifier.utility.common import read_yaml_file
from deep_classifier.entity.config_entity import (Training_Pipeline_Config,Data_Ingestion_Config,
                                                  Prepare_Base_Model_Config,Prepare_Callbacks_Config,
                                                  Model_Training_Config,Model_Evaluation_Config,
                                                  Model_Prediction_Service_Config)
from pathlib import Path
import os


class Configuration:
    def __init__(
        self, config_file_path=CONFIG_FILE_PATH,params_file_path=PARAMETERS_FILE_PATH,
        timestamp: str = CURRENT_TIMESTAMP
    ):
        try:
            self.config_info = read_yaml_file(file_path=Path(config_file_path))
            self.traning_pipeline_config = self.get_traning_pipeline_config()
            self.params_file_info=read_yaml_file(file_path=Path(params_file_path))
            self.time_stamp = timestamp
        except Exception as e:
            raise e

    def get_traning_pipeline_config(self) -> Training_Pipeline_Config:
        try:
            training_pipeline_config_info = self.config_info.training_pipeline_config
            artifact_dir = os.path.join(
                ROOT_DIR,
                training_pipeline_config_info.pipeline_name,
                training_pipeline_config_info.artifact_dir,
            )
            training_pipeline_config = Training_Pipeline_Config(
                artifact_dir=artifact_dir
            )
            logger.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise e

    def get_data_ingestion_config(self) -> Data_Ingestion_Config:
        try:
            data_ingestion_config_info = self.config_info.data_ingestion_config
            artifact_dir = self.traning_pipeline_config.artifact_dir
            data_ingestion_artifact_dir = os.path.join(
                artifact_dir, data_ingestion_config_info.data_ingestion_dir
            )
            dataset_download_url = data_ingestion_config_info.dataset_download_url
            raw_data_dir = os.path.join(
                data_ingestion_artifact_dir, data_ingestion_config_info.raw_data_dir
            )
            extracted_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_config_info.extracted_data_dir,
            )
            traning_data_dir = os.path.join(
                extracted_data_dir,"PetImages"
            )
            testing_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_config_info.ingested_test_dir,
            )

            data_ingestion_config = Data_Ingestion_Config(
                data_ingestion_dir=data_ingestion_artifact_dir,
                dataset_download_url=dataset_download_url,
                raw_data_dir=raw_data_dir,
                extracted_data_dir=extracted_data_dir,
                ingested_train_dir=traning_data_dir,
                ingested_test_dir=testing_data_dir,
            )
            logger.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise e

    def get_prepare_base_model_config(self)->Prepare_Base_Model_Config:
        try:
            artifact_dir=self.traning_pipeline_config.artifact_dir
            prepare_base_model_config_info=self.config_info.prepare_base_model_config
            prepare_base_model_config_dir=os.path.join(artifact_dir,
                                            prepare_base_model_config_info.prepare_base_model_dir)
            base_model_dir=os.path.join(prepare_base_model_config_dir,
                                        prepare_base_model_config_info.base_model_dir)
            base_model_file_name=prepare_base_model_config_info.base_model_file_name
            updated_model_dir=os.path.join(prepare_base_model_config_dir,
                                           prepare_base_model_config_info.updated_model_dir)
            updated_model_file_name=prepare_base_model_config_info.updated_model_file_name
            updated_model_file_path=os.path.join(updated_model_dir,updated_model_file_name)
            params_image_size=self.params_file_info.params_image_size
            params_include_top=self.params_file_info.include_top
            params_weights=self.params_file_info.weights
            params_classes=self.params_file_info.classes
            params_learning_rate=self.params_file_info.learning_rate
            prepare_base_model_config=Prepare_Base_Model_Config(
                                                    prepare_base_model_dir=prepare_base_model_config_dir,
                                                    base_model_dir=base_model_dir,
                                                    base_model_file_name=base_model_file_name,
                                                    updated_model_dir=updated_model_dir,
                                                    updated_model_file_name=updated_model_file_name,
                                                    updated_model_file_path=updated_model_file_path,
                                                    params_image_size=params_image_size,
                                                    params_include_top=params_include_top,
                                                    params_classes=params_classes,
                                                    params_weights=params_weights,
                                                    params_learning_rate=params_learning_rate)
            logger.info(f"Prepare Model Config: {prepare_base_model_config}")
            return prepare_base_model_config
        except Exception as e:
            raise e
    
    def get_prepare_callbacks(self)->Prepare_Callbacks_Config:
        try:
            artifact_dir=self.traning_pipeline_config.artifact_dir
            prepare_callbacks_config_info=self.config_info.prepare_callbacks_config
            prepare_callbacks_dir=os.path.join(artifact_dir,
                                    prepare_callbacks_config_info.prepare_callbacks_dir)
            tensorboard_log_dir=os.path.join(prepare_callbacks_dir,
                                    prepare_callbacks_config_info.tensorboard_log_dir)
            model_checkpoint_dir=os.path.join(prepare_callbacks_dir,
                                    prepare_callbacks_config_info.model_checkpoint_dir)
            model_checkpoint_file_name=prepare_callbacks_config_info.model_checkpoint_file_name
            prepare_callbacks_config=Prepare_Callbacks_Config(
                                                    prepare_callbacks_dir=prepare_callbacks_dir,
                                                    tensorboard_log_dir=tensorboard_log_dir,
                                                    model_checkpoint_dir=model_checkpoint_dir,
                                                    model_checkpoint_file_name=model_checkpoint_file_name)
            logger.info(f"Prepare Callbacks Config: {prepare_callbacks_config}")
            return prepare_callbacks_config
        except Exception as e:
            raise e
    
    def get_model_training_config(self)->Model_Training_Config:
        try:
            artifact_dir = self.traning_pipeline_config.artifact_dir
            data_ingestion_config_info = self.config_info.data_ingestion_config
            data_ingestion_artifact_dir = os.path.join(artifact_dir, 
                                                       data_ingestion_config_info.data_ingestion_dir)
            extracted_data_dir = os.path.join(data_ingestion_artifact_dir,
                                              data_ingestion_config_info.extracted_data_dir)
            prepare_base_model_config_info=self.config_info.prepare_base_model_config
            prepare_base_model_config_dir=os.path.join(artifact_dir,
                                            prepare_base_model_config_info.prepare_base_model_dir)
            updated_model_dir=os.path.join(prepare_base_model_config_dir,
                                           prepare_base_model_config_info.updated_model_dir)
            updated_model_file_name=prepare_base_model_config_info.updated_model_file_name
            updated_model_file_path=os.path.join(updated_model_dir,updated_model_file_name)
            model_training_config_info=self.config_info.model_training_config
            model_training_dir=os.path.join(artifact_dir,model_training_config_info.model_training_dir)
            model_training_file_name=model_training_config_info.model_file_name
            params_agumentation=self.params_file_info.agumentation
            params_image_size=self.params_file_info.params_image_size
            params_batch_size=self.params_file_info.batch_size
            params_epochs=self.params_file_info.epochs
            training_data_path=os.path.join(extracted_data_dir,"PetImages")
            model_training_config=Model_Training_Config(model_training_dir=model_training_dir,
                                                        model_training_file_name=model_training_file_name,
                                                        params_agumentation=params_agumentation,
                                                        params_batch_size=params_batch_size,
                                                        params_epochs=params_epochs,
                                                        params_image_size=params_image_size,
                                                        updated_base_model_path=updated_model_file_path,
                                                        training_data_path=training_data_path)
            logger.info(f"Model Training Config: {model_training_config}")
            return model_training_config
        except Exception as e:
            raise e
    
    def get_model_evaluation_config(self)->Model_Evaluation_Config:
        try:
            model_evaluation_config_info=self.config_info.model_evaluation.config
            model_training_path=model_evaluation_config_info.trained_model_path
            training_data_file_path=model_evaluation_config_info.training_data_file_path
            model_evaluation_config=Model_Evaluation_Config(
                                                trained_model_path=model_training_path,
                                                training_data_file_path=training_data_file_path,
                                                params_image_size=self.params_file_info.params_image_size,
                                                params_batch_size=self.params_file_info.params_batch_size)
            return model_evaluation_config
        except Exception as e:
            raise e
    
    def get_model_prediction_service(self)->Model_Prediction_Service_Config:
        try:
            model_prediction_service_config_info=self.config_info.model_prediction_service_config
            trained_model_file_path=model_prediction_service_config_info.trained_model_path
            model_prediction_service_config=Model_Prediction_Service_Config(
                                                  trained_model_path=trained_model_file_path)
            return model_prediction_service_config
        except Exception as e:
            raise e