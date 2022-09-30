from deep_classifier import logger
from deep_classifier.config.configuration import Configuration
from deep_classifier.components.prepare_callbacks import Prepare_Callbacks
from deep_classifier.components.model_training import Model_Training

STAGE_NAME="Model_Training_Phase"

def main():

    config=Configuration()
    prepare_callbacks_config=config.get_prepare_callbacks()
    prepare_callbacks=Prepare_Callbacks(prepare_callbacks_config=prepare_callbacks_config)
    callbacks_list=prepare_callbacks.initiate_prepare_callbacks()

    training_pipeline_config=config.get_model_training_config()
    model_training=Model_Training(model_training_config=training_pipeline_config)
    model_training.initiate_training(callbacks_list=callbacks_list)

if __name__=="__main__":
    try:
        logger.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise e
