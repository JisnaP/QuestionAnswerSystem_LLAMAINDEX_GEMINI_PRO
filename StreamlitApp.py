import streamlit as st
from QAwithpdf.data_ingestion import load_data
from QAwithpdf.embedding import download_gemini_embedding
from QAwithpdf.model_api import load_model

def processor():
    st.set_page_config(
        page_title="Question & Answering App",
        page_icon="🤔"

    )
    doc=st.file_uploader("Upload your file here",accept_multiple_files=True)
    st.header("QA with documents(Information Retrieval)")
    user_question=st.text_input("Enter your question here")
    
    if st.button("submit and process"):
       with st.spinner("Retieving answer ..."):
         documents=load_data(doc)
         model=load_model()
         query_engine=download_gemini_embedding(model,documents)
         response=query_engine.query(user_question)
         st.write(response.response)
if __name__=="__main__":
 processor()
