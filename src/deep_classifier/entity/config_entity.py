from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Training_Pipeline_Config:
    artifacr_dir: Path

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
    params_image_size: list
    params_agumentation: bool
    params_batch_size: int
    params_include_top: bool
    params_epochs: int
    params_classes: int
    params_weights: str
    params_learning_rate: float
    