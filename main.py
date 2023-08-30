import os
from Banking.config.configuration import Configuration
from Banking.logger import logging
from Banking.exception import CustomException
from Banking.pipeline.pipeline import Pipeline
from Banking.entity.artifact_entity import DataIngestionArtifact
from Banking.components.data_ingestion import DataIngestion

def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()
    
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()