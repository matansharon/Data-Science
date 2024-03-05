import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from helper_function import  read_data_files,extract_text_from_pdf
from io import StringIO
import PyPDF2
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import pickle
from dotenv import load_dotenv
#sidebar
with st.sidebar:
    st.title('Chatbot')
    st.markdown("""
                ##About
                - This is a simple chatbot that uses the `chatterbot` library to generate responses.
                - The chatbot is trained on a small dataset and may not be able to answer all questions.
                - The chatbot is not perfect and may generate incorrect responses.
                - The chatbot is not a substitute for professional advice.
                """)
    add_vertical_space(10)
    st.write('Made By Matan Sharon')

def main():
    load_dotenv()
    st.header('Chatbot')
    
    st.write('### Hello, I am a chatbot. How can I help you today?')

    
    # files=read_data_files('data')
    # if files:
    #     st.write('### Data files')
    #     for file in files:
    #         st.write(str(file),'\n\n\n')
    
    file=st.file_uploader('Upload a file', type=['pdf','xlsx','csv'])
    
    if file:
        if file.name.endswith('.pdf'):
            pdf_reader=PyPDF2.PdfReader(file)
            text=''
            for page in pdf_reader.pages:
                text+=page.extract_text()
            text_splitter=RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            chunks=text_splitter.split_text(text)
            
            #embeddings
            embedding=OpenAIEmbeddings()
            vector_store = FAISS.from_texts(chunks, embedding=embedding)
            store_name=file.name[:-4]
            with open(f'{store_name}.pkl','wb') as f:
                pickle.dump(vector_store,f)
            
            st.write(chunks[:5])
            
        
    
        
    res=st.chat_input('Ask me anything')
    if res:
        st.write(res)
       


if __name__ == '__main__':
    main()
