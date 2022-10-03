from deep_classifier import logger
from deep_classifier.components.model_evaluation import Model_Evaluation
from deep_classifier.config.configuration import Configuration

STAGE_NAME="Model Evaluation Phase"

def main():
    config=Configuration()
    model_evaluation_config=config.get_model_evaluation()
    model_evaluation=Model_Evaluation(model_evaluation_config=model_evaluation_config)
    model_evaluation.initiate_model_evaluation()

if __name__=="__main__":
    try:
        logger.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise e
