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
