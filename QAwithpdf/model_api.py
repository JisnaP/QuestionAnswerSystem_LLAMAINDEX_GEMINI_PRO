from llama_index.llms import Gemini
import google.generativeai as genai
from logger import logging
import sys

from Exception import customexception

def load_model():

    logging.info(f"Model is loading...")
    google_api_key=genai.configure(api_key=google_api_key)
    model=Gemini(model="gemini_pro",api_key=google_api_key)
