from deep_classifier import logger
from deep_classifier.entity.config_entity import Model_Evaluation_Config
from deep_classifier.utility.common import save_json
from pathlib import Path
import tensorflow as tf


class Model_Evaluation:
    def __init__(self,model_evaluation_config:Model_Evaluation_Config):
        try:
            self.model_evaluation_config=model_evaluation_config
        except Exception as e:
            raise e
    
    def initiate_model_evaluation(self):
        try:
            model=self.load_model(path=self.model_evaluation_config.trained_model_path)
            self._valid_generator()
            self.score=model.evaluate(self.valid_datagenerator)
        except Exception as e:
            raise e
    
    @staticmethod
    def load_model(path:Path)->tf.keras.Model:
        try:
            return tf.keras.models.load_model(path)
        except Exception as e:
            raise e

    def _valid_generator(self):
        try:
            datagenerator_kwargs=dict(
                rescale = 1./255,
                validation_split=0.30)
            
            dataflow_kwargs=dict(
                target_size=self.config.params_image_size[:-1],
                batch_size=self.config.params_batch_size,
                interpolation="bilinear")
            
            valid_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)

            self.valid_datagenerator=valid_datagenerator.flow_from_directory(
                                        directory=self.model_evaluation_config_info.training_data_file_path,
                                        subset="validation",
                                        shuffle=False,
                                        **dataflow_kwargs)
        except Exception as e:
            raise e
    
    def save_score(self):
        try:
            scores={"loss": self.score[0],"accuracy": self.score[1]}
            save_json(path=Path("scores.json"),data=scores)
        except Exception as e:
            raise e
