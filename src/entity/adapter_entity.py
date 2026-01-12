from dataclasses import dataclass


@dataclass
class DatasetProcessorAdapter:
    trained_file_path:str 
    test_file_path:str 

@dataclass
class DataValidationAdapter:
    validation_status:bool
    message: str
    drift_report_file_path: str

@dataclass
class DataTransformationAdapter:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str

@dataclass
class ClassificationMetricAdapter: 
    f1_score:float
    precision_score:float
    recall_score:float



@dataclass
class ModelTrainerAdapter:
    trained_model_file_path:str 
    metric_artifact:ClassificationMetricAdapter


@dataclass
class ModelEvaluationAdapter:
    is_model_accepted:bool
    changed_accuracy:float
    blob_model_path:str 
    trained_model_path:str



@dataclass
class ModelPusherAdapter:
    blob_name:str
    blob_model_path:str