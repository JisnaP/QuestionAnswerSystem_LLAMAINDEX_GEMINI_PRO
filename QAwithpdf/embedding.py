from logger import logging
from Exception import customexception
import sys
from llama_index.embeddings.gemini import GeminiEmbeddings
from QAwithpdf.data_ingestion import load_data
from llama_index.core import Settings,VectorStoreIndex
from QAwithpdf.model_api import load_model

def download_gemini_embedding(documents):
    try:
       logging.info(f"downloading gemini embedding...")
       embedding=GeminiEmbeddings(model_name="models/embedding-001")
       logging.info(f"embedding downloaded successfully")
       Settings.embed_model= embedding
       Settings.llm=load_model()
       index = VectorStoreIndex.from_documents(documents,Settings.llm,Settings.embed_model)
       logging.info(f"Index created successfully")
       return index
    except Exception as e:
        logging.info(f"execption in downloading embedding model")
        raise customexception(e,sys)



