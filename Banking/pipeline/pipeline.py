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
from Banking.entity.artifact_entity import DataIngestionArtifact



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
   
        
        
    def run_pipeline(self):
        try:
            # Data Ingestion
            data_ingestion_artifact = self.start_data_ingestion()
        
        except Exception as e:
            raise CustomException(e,sys) from e  
            
        
        except Exception as e:
            raise CustomException(e, sys) from e