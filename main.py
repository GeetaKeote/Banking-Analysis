import os, sys
import pandas as pd
import numpy as np
from Banking.constant import *
from Banking.logger import logging
from Banking.exception import CustomException
from Banking.pipeline.pipeline import Pipeline 


def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()
    
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()