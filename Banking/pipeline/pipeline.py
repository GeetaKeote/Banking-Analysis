import os, sys
from datetime import datetime
import pandas as pd
from collections import namedtuple
import uuid

from Banking.config.configuration import Configuration

from Banking.logger import logging
from Banking.exception import CustomException
from threading import Thread
from typing import List
from multiprocessing import Process
from Banking.components.data_ingestion import DataIngestion
from Banking.components.data_validation import DataValidation
from Banking.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact



class Pipeline():
    def __init__(self, config: Configuration = Configuration())->None:
        try:
            self.config = config
        except Exception as e:
            raise CustomException(e,sys) from e  
        
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config= self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise CustomException(e,sys) from e  
   
   ################### Data Validation 

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                             data_ingestion_artifact=data_ingestion_artifact
                                             )
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise CustomException(e, sys) from e
        
        
    def run_pipeline(self):
        try:
            # Data Ingestion
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact = data_ingestion_artifact)
        except Exception as e:
            raise CustomException(e,sys) from e  
            
        
        except Exception as e:
            raise CustomException(e, sys) from e