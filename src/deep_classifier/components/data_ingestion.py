from urllib import request
from deep_classifier import logger
from deep_classifier.entity.config_entity import Data_Ingestion_Config
from deep_classifier.utility.common import create_directories,get_size
from tqdm import tqdm
from zipfile import ZipFile
from pathlib import Path
import urllib.request as request
import requests
import os

class Data_Ingestion:
    def __init__(self,data_ingestion_config:Data_Ingestion_Config):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise e
    
    def download_the_data(self):
        try:
            download_url=self.data_ingestion_config.dataset_download_url
            raw_data_dir=self.data_ingestion_config.raw_data_dir
            raw_data_file_name=os.path.basename(download_url)
            raw_data_file_path=os.path.join(raw_data_dir,raw_data_file_name)
            create_directories([raw_data_dir])
            logger.info(f"Downloading file from :[{download_url}] into :[{raw_data_file_path}]")
            if not os.path.exists(raw_data_file_path):
                chunk_size=1024
                response=requests.get(url=download_url,stream=True)
                total_size=int(response.headers.get('content-length'))
                with open(raw_data_file_path,"wb") as file:
                    for data in tqdm(iterable=response.iter_content(chunk_size=chunk_size),
                                                                total=total_size/chunk_size,
                                                                unit="KB"):
                        file.write(data)

                #request.urlretrieve(download_url,raw_data_file_path)
                logger.info(f"File :[{raw_data_file_path}] has been downloaded successfully.")
            return raw_data_file_path
        except Exception as e:
            raise e
    
    def extract_the_files_and_clean(self,raw_data_dir_path:str):
        try:
            extracted_data_dir=self.data_ingestion_config.extracted_data_dir
            create_directories([extracted_data_dir])
            with ZipFile(raw_data_dir_path,"r") as zip_file:
                list_of_files=zip_file.namelist()
                updated_list_of_files=self._get_updated_list_of_files(list_of_files)
                for f in tqdm(updated_list_of_files):
                    self._preprocess(raw_data=zip_file,file_name=f,extracted_dir=extracted_data_dir)
        except Exception as e:
            raise e
    
    def _get_updated_list_of_files(self,list_of_files):
        try:
            return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or"Dog" in f)]
        except Exception as e:
            raise e
    def _preprocess(self,raw_data:ZipFile,file_name,extracted_dir):
        try:
            extracted_dir_path=os.path.join(extracted_dir,file_name)
            if not os.path.exists(extracted_dir_path):
                raw_data.extract(file_name,extracted_dir)
            
            if os.path.getsize(extracted_dir_path) == 0:
                logger.info(f"removing file:{extracted_dir_path} of size: {get_size(Path(extracted_dir_path))}")
                os.remove(extracted_dir_path)
        except Exception as e:
            raise e
    
    def initiate_data_ingestion(self):
        try:
            raw_data_file_path=self.download_the_data()
            return self.extract_the_files_and_clean(raw_data_dir_path=raw_data_file_path)
        except Exception as e:
            raise e