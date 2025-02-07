from logger import logging
from Exception import customexception
import sys
from llama_index.embeddings.gemini import GeminiEmbedding
from QAwithpdf.data_ingestion import load_data
from llama_index.core import Settings,VectorStoreIndex
from QAwithpdf.model_api import load_model
def download_gemini_embedding(model,documents):
    try:
       logging.info(f"downloading gemini embedding...")
                 
       embedding=GeminiEmbedding(model_name="models/embedding-001")
       logging.info(f"embedding downloaded successfully")
       Settings.embed_model= embedding
       Settings.llm=model
       index = VectorStoreIndex.from_documents(documents,llm=Settings.llm,embed_model=Settings.embed_model,chunk_size=200,chunk_overlap=20)
       logging.info(f"Index created successfully")
       query_engine=index.as_query_engine()
       return query_engine
    except Exception as e:
        logging.info(f"execption in downloading embedding model")
        raise customexception(e,sys)



