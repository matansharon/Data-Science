import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import pandas as pd
import os
from helper_function import  read_data_files,extract_text_from_pdf
from io import StringIO
import PyPDF2
import pickle
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

import getpass
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
    # os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')
    st.header('Chatbot')
    
    st.write('### Hello, I am a chatbot. How can I help you today?')
    
    
    # files=read_data_files('data')
    # if files:
    #     st.write('### Data files')
    #     for file in files:
    #         st.write(str(file),'\n\n\n')
    
    file=st.file_uploader('Upload a file', type=['pdf'])
    
    if file:
        # if file.name.endswith('.pdf'):
            pdf_reader=PyPDF2.PdfReader(file)
            text=''
            for page in pdf_reader.pages:
                text+=page.extract_text()
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            documents = text_splitter.split_text(text)
            
            vectorstore = Chroma('langchain_store', OpenAIEmbeddings())
            query = "Summerize the document"
            vectorstore.add_texts(text)
            st.write(vectorstore.similarity_search(query="Summerize the document"))
            # st.write(docs)
            # print(docs[0].page_content) 
    #         text_splitter=RecursiveCharacterTextSplitter(
    #             chunk_size=500,
    #             chunk_overlap=100,
    #             length_function=len
    #         )
    #         chunks=text_splitter.split_text(text)
            
    #         #embeddings

    #         store_name=file.name[:-4]
    #         st.write(store_name)
    #         if os.path.exists(f'{store_name}.pkl'):
    #             st.write('Loading from store')
    #             with open(f'{store_name}.pkl','rb') as f:
    #                 vector_store = load(f'{store_name}.joblib')
    #         else:
    #             st.write('Creating store')
    #             embedding=OpenAIEmbeddings()
    #             vector_store = FAISS.from_texts(chunks, embedding=embedding)
    #             with open(f'{store_name}.pkl','wb') as f:
    #                 dump(vector_store, f'{store_name}.joblib')
            
    #         # st.write(chunks[:5])
            
        
    
        
    # res=st.chat_input('Ask me anything')
    # if res:
    #     st.write(res)
       


if __name__ == '__main__':
    main()
