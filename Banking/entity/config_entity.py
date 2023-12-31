import os,sys
import pandas as pd 
from collections import namedtuple


DataIngestionConfig =namedtuple("DataIngestionConfig",
                               ["dataset_download_url",
                                 "ingested_data_dir",
                                 "raw_data_dir",
                               "ingested_train_dir","ingested_test_dir"])


DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path"])                               

TrainingPipelineConfig= namedtuple("TrainingPipelineConfig",
                                  ["artifact_dir"])