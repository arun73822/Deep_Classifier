from deep_classifier import logger
from deep_classifier.config.configuration import Configuration
from deep_classifier.components.prepare_base_model import Prepare_Base_Model

STAGE_NAME="Prepare Base Model Stage"

def main():
    config=Configuration()
    prepare_base_model_config=config.get_prepare_base_model_config()
    prepare_base_model=Prepare_Base_Model(prepare_base_model_config=prepare_base_model_config)
    prepare_base_model.initiate_prepare_base_model()

if __name__=="__main__":
    try:
        logger.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    