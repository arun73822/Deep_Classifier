from deep_classifier import logger
from deep_classifier.config.configuration import Configuration
from deep_classifier.components.data_ingestion import Data_Ingestion


STAGE_NAME = "Data Ingestion stage"

def main():
    config = Configuration()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = Data_Ingestion(data_ingestion_config=data_ingestion_config)
    data_ingestion.initiate_data_ingestion()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e