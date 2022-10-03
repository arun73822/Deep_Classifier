from dataclasses import dataclass
from pathlib import Path

from attr import frozen

@dataclass(frozen=True)
class Training_Pipeline_Config:
    artifact_dir: Path

@dataclass(frozen=True)
class Data_Ingestion_Config:
    data_ingestion_dir: Path
    dataset_download_url: str
    raw_data_dir: Path
    extracted_data_dir: Path
    ingested_train_dir: Path
    ingested_test_dir: Path

@dataclass(frozen=True)
class Prepare_Base_Model_Config:
    prepare_base_model_dir: Path
    base_model_dir: Path
    base_model_file_name: str
    updated_model_dir: Path
    updated_model_file_name: str
    updated_model_file_path: Path
    params_image_size: list
    params_include_top: bool
    params_classes: int
    params_weights: str
    params_learning_rate: float

@dataclass(frozen=True)
class Prepare_Callbacks_Config:
    prepare_callbacks_dir: Path
    tensorboard_log_dir: Path
    model_checkpoint_dir: Path
    model_checkpoint_file_name: str

@dataclass(frozen=True)
class Model_Training_Config:
    model_training_dir: Path
    model_training_file_name: str
    updated_base_model_path: Path
    
    training_data_path: Path
    params_image_size: list
    params_agumentation: bool
    params_batch_size: int
    params_epochs: int

@dataclass(frozen=True)
class Model_Evaluation_Config:
    trained_model_path: Path
    training_data_file_path: Path
    params_image_size: list
    params_batch_size: int
    