import sys
from logger import logging
from Exception import customexception
from llama_index.core import SimpleDirectoryReader
import tempfile
import os
def load_data(uploaded_file):
    """
    Loads data from a specified directory
    data:str 
    It is the path to directory containg pdf or text files

    Returns: A list of specific loaded pdf or text documents
    
    """
    
    try:
        logging.info("Data loading started ...")

        with tempfile.TemporaryDirectory() as tempdir:
            filename = os.path.join(tempdir, uploaded_file.name)
            with open(filename, 'wb') as f:
                f.write(uploaded_file.getbuffer())

            doc = SimpleDirectoryReader(tempdir)
            documents = doc.load_data()

        logging.info("Data loading completed.")
        return documents

    except Exception as e:
        logging.error("Exception in loading data", exc_info=True)
        raise customexception(e, sys)
