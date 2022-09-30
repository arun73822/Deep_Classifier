from deep_classifier import logger
from deep_classifier.entity.config_entity import Model_Training_Config
from deep_classifier.utility.common import read_yaml_file
from deep_classifier.constants import *
from pathlib import Path
import tensorflow as tf

class Model_Training:

    def __init__(self,model_training_config:Model_Training_Config):
        try:
            self.model_training_config=model_training_config
            self.params_info=read_yaml_file(file_path=PARAMETERS_FILE_PATH)
        except Exception as e:
            raise e
    
    def load_base_model(self):
        try:
            updated_base_model_path=self.model_training_config.updated_base_model_path
            self.model=tf.keras.models.load_model(updated_base_model_path)
        except Exception as e:
            raise e
    
    def training_validaton_generator(self):
        try:
            training_data_path=self.model_training_config.training_data_path

            data_generator_kwargs=dict(
                rescale=1./255,
                validation_split=0.2)

            dataflow_kwargs=dict(
                target_size=self.model_training_config.params_image_size[:-1],
                batch_size=self.model_training_config.params_batch_size,
                interpolation="bilinear")

            validation_generator = tf.keras.preprocessing.image.ImageDataGenerator(data_generator_kwargs)

            self.validation_generator=validation_generator.flow_from_directory(
                                                                    directory=training_data_path,
                                                                    subset="validation",
                                                                    shuffle=False,
                                                                    **dataflow_kwargs)
            if self.model_training_config.params_agumentation:
                train_data_generator=tf.keras.preprocessing.image.ImageDataGenerator(
                    rotation_range=40,
                    horizontal_flip=True,
                    width_shift_range=0.2,
                    height_shift_range=0.2,
                    shear_range=0.2,
                    zoom_range=0.2,
                    **data_generator_kwargs)
            else:
                train_data_generator=validation_generator
            self.train_data_generator=train_data_generator.flow_from_directory(
                                                    directory=training_data_path,
                                                    subset="training",
                                                    shuffle=True,
                                                    **dataflow_kwargs)
        except Exception as e:
            raise e

    def initiate_training(self,callbacks_list:list):
        try:
            self.load_base_model()
            self.training_validaton_generator()
            trained_model_path=os.path.join(self.model_training_config.model_training_dir,
                                            self.model_training_config.model_training_file_name)

            self.steps_per_epoch=self.train_data_generator.samples//self.train_data_generator.batch_size
            self.validation_steps= self.validation_generator.samples//self.validation_generator.batch_size

            self.model.fit(
                self.train_data_generator,
                epochs=self.model_training_config.params_epochs,
                steps_per_epoch=self.steps_per_epoch,
                validation_steps=self.validation_steps,
                validation_data=self.validation_generator,
                callbacks=callbacks_list)

            self.save_model(path=Path(trained_model_path),model=self.model)
        except Exception as e:
            raise e
    
    @staticmethod
    def save_model(path:Path, model:tf.keras.Model):
        try:
            model.save(path)
        except Exception as e:
            raise e
