from Kidney_Disease_Classification import logger
from Kidney_Disease_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Kidney_Disease_Classification.pipeline.stage_02_prepare_base_model import PrepareBaseModeTrainingPipeline


STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try:
    logger.info(f"******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModeTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========")
except Exception as e:
    logger.exception(e)
    raise e