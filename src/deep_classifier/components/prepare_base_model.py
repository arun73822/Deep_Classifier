from keras.saving.save import save_model
from deep_classifier import logger
from deep_classifier.entity.config_entity import Prepare_Base_Model_Config
from pathlib import Path
import tensorflow as tf
import os

class Prepare_Base_Model:

    def __init__(self,prepare_base_model_config:Prepare_Base_Model_Config):
        try:
            self.prepare_base_model_config=prepare_base_model_config
        except Exception as e:
            raise e
    
    def get_base_model(self):
        try:
            base_model_dir=self.prepare_base_model_config.base_model_dir
            base_model_name=self.prepare_base_model_config.base_model_file_name
            base_model_path=os.path.join(base_model_dir,base_model_name)
            image_size=self.prepare_base_model_config.params_image_size
            include_top=self.prepare_base_model_config.params_include_top
            weights=self.prepare_base_model_config.params_weights

            self.base_model=tf.keras.applications.vgg16.VGG16(input_shape=image_size,
                                                              include_top=include_top,
                                                              weights=weights)
            self.save_model(path=base_model_path,model=self.base_model)
        except Exception as e:
            raise e
    def update_base_model(self):
        try:
            classes=self.prepare_base_model_config.params_classes
            learning_rate=self.prepare_base_model_config.params_learning_rate
            self.full_model=self._prepare_full_model(model=self.base_model,classes=classes,
                                                     freeze_all=True,freeze_till=None,
                                                     learning_rate=learning_rate)
            updated_base_model_dir=self.prepare_base_model_config.updated_model_dir
            updated_base_model_name=self.prepare_base_model_config.updated_model_file_name
            updated_base_path=os.path.join(updated_base_model_dir,updated_base_model_name)
            self.save_model(path=updated_base_path,model=self.full_model)
        except Exception as e:
            raise e
    
    @staticmethod
    def _prepare_full_model(model,classes:int,freeze_all:bool,freeze_till,learning_rate:float):
        try:
            if freeze_all:
                for layer in model.layers:
                    model.trainable=False
                logger.info(f"")
            elif (freeze_all is not None) and (freeze_till > 0):
                for layer in model.layers[:-freeze_till]:
                    model.trainable=False
            flatten_in=tf.keras.layers.Flatten()(model.output)
            prediction=tf.keras.layers.Dense(units=classes,activation="softmax")(flatten_in)
            full_model=tf.keras.models.Model(inputs=model.input,outputs=prediction)
            full_model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
                               loss=tf.keras.losses.CategoricalCrossentropy(),
                               metrics=["accuracy"])
            full_model_summary=full_model.summary()
            logger.info(f"Model summary is \n {full_model_summary} ")
            return full_model
        except Exception as e:
            raise e

    @staticmethod
    def save_model(path:Path,model:tf.keras.Model):
        try:
            model.save(path)
            logger.info(f"Successfully saved the model and path is {path}")
        except Exception as e:
            raise e
    
    def initiate_prepare_base_model(self):
        try:
            self.get_base_model()
            return self.update_base_model()
        except Exception as e:
            raise e
            