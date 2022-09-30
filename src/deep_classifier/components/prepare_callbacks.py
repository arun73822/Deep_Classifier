import tensorboard
from tensorflow.python.ops.gen_math_ops import log
from deep_classifier import logger
from deep_classifier.entity.config_entity import Prepare_Callbacks_Config
from deep_classifier.utility.common import create_directories
from deep_classifier.constants import *
from pathlib import Path
import tensorflow as tf

class Prepare_Callbacks:

    def __init__(self,prepare_callbacks_config:Prepare_Callbacks_Config,timestamp=CURRENT_TIMESTAMP):
        try:
            self.prepare_callbacks_config=prepare_callbacks_config
            self.timestamp=timestamp
        except Exception as e:
            raise e
    
    def get_tb_ckpt_callbacks(self):
        try:
            return [self._create_tb_ckpt_callbacks,
                    self._create_ckpt_callbacks]
        except Exception as e:
            raise e
    
    @property
    def _create_tb_ckpt_callbacks(self):
        try:
            tensorboard_log=f"tb_log_at_{self.timestamp}.log"
            tensorboard_dir=self.prepare_callbacks_config.tensorboard_log_dir
            tensorboard_dir_path=os.path.join(tensorboard_dir,tensorboard_log)
            create_directories([Path(tensorboard_dir)])
            return tf.keras.callbacks.TensorBoard(log_dir=tensorboard_dir_path)
        except Exception as e:
            raise e
    
    @property
    def _create_ckpt_callbacks(self):
        try:
            checkpoint_dir=self.prepare_callbacks_config.model_checkpoint_dir
            checkpoint_file_name=self.prepare_callbacks_config.model_checkpoint_file_name
            checkpoint_dir_path=os.path.join(checkpoint_dir,checkpoint_file_name)
            create_directories([Path(checkpoint_dir)])
            return tf.keras.callbacks.ModelCheckpoint(checkpoint_dir_path,save_best_only=True)
        except Exception as e:
            raise e
    
    def initiate_prepare_callbacks(self):
        try:
            callbacks_list=self.get_tb_ckpt_callbacks()
            return callbacks_list
        except Exception as e:
            raise e
