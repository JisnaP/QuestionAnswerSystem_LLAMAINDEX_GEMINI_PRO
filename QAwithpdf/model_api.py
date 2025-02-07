from llama_index.llms.gemini import Gemini
import google.generativeai as genai
from logger import logging
import sys
from dotenv import load_dotenv
import os

from Exception import customexception

def load_model():
    load_dotenv()
    google_api_key=os.getenv("GOOGLE_API_KEY")
    logging.info(f"Model is loading...")
    model=Gemini(models="models/gemini-1.5-pro",api_key=google_api_key)
    return model