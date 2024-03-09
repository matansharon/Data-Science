import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import pandas as pd
import os
import helper_functions
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
    
    
    # file=st.file_uploader('Upload a file', type=['pdf'])
    


if __name__ == '__main__':
    main()
