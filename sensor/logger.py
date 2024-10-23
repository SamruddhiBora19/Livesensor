import logging
import os
import sys
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"  #creates logfile name using current date and time

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #logs is folder
os.makedirs(logs_path,exist_ok=True) #makes logs_path only if doesnot exist
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
  filename=LOG_FILE_PATH,
  format="[%(asctime)s] %(lineno)d  %(name)s - %(levelname)s- %(message)s",
  level=logging.INFO,)