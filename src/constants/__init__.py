import os
from datetime import date
from urllib.parse import quote_plus
import certifi


PIPELINE_NAME: str = "llama_3.1_8b_bengali_empathetic_ft"
ADAPTER_DIR: str = "adapter"

# MODEL_FILE_NAME = "model.pkl"


TARGET_COLUMN = "num"
CURRENT_YEAR = date.today().year
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"

FILE_NAME: str = "BengaliEmpatheticConversationsCorpus .csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
# SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")


"""
Data Processing related constant start with DATA_PROCESSOR VAR NAME
"""
DATA_PROCESSOR_COLLECTION_NAME: str = "bangli_empathy_data"
DATA_PROCESSOR_DIR_NAME: str = "data_processor"
DATA_PROCESSOR_FEATURE_STORE_DIR: str = "feature_store"
DATA_PROCESSOR_INGESTED_DIR: str = "processing"
DATA_PROCESSOR_TRAIN_TEST_SPLIT_RATIO: float = 0.2



"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")



MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_BLOB_NAME = "cvd-uploads"
MODEL_PUSHER_BLOB_PATH = "model-registry"


APP_HOST = "0.0.0.0"
APP_PORT = 8080