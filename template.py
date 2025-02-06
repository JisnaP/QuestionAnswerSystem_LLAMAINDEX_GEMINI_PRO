import os
from pathlib import Path
import logging
list_of_files=[
    "QAwithpdf/__init__.py",
    "QAwithpdf/data_ingestion.py",
    "QAwithpdf/embedding.py",
    "QAwithpdf/model_trainer.py",
    "Experiments/experiments.ipynb",
    "logger.py",
    "Exception.py",
    "StreamlitApp.py",
    "setup.py"



]
for filepath in list_of_files:
    filepath=Path(filepath)
    fildir,filname=os.path.split(filepath)

    if fildir !="":
        os.makedirs(fildir,exist_ok=True)
        logging.info(f"Creating directory {fildir} for filename {filname}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open (filepath,"w") as f:
            pass
        logging.info(f"Creating empty file {filepath}")
    else:
        logging.info(f"{filname} already exists")

