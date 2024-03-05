import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from helper_function import get_all_files_in_directory, read_data_file,extract_text_from_pdf
from io import StringIO
import PyPDF2





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
    st.header('Chatbot')
    
    st.write('### Hello, I am a chatbot. How can I help you today?')
    files=get_all_files_in_directory('data')
    st.write(f"files in the data directory are: {files}")
    
    
    file=st.file_uploader('Upload a file', type=['pdf','xlsx','csv'])
    
    if file:
        if file.name.endswith('.pdf'):
            pdf_reader=PyPDF2.PdfReader(file)
            text=''
            for page in pdf_reader.pages:
                text+=page.extract_text()
            st.write(text)
        
    
        
    res=st.chat_input('Ask me anything')
    if res:
        st.write(res)
       


if __name__ == '__main__':
    main()
