import sys
from logger import logging
from Exception import customexception
from llama_index.core import SimpleDirectoryReader

def load_data(data):
    """
    Loads data from a specified directory
    data:str 
    It is the path to directory containg pdf or text files

    Returns: A list of specific loaded pdf or text documents
    
    """
    try:
      logging.info(f"Data loading started ...")
      loader=SimpleDirectoryReader(data)
      documents=loader().load_data()
      logging.info(f"logging completed")
      return documents
    except Exception as e:
      logging.info(f"exception in loading data")
      raise customexception(e,sys)
      

