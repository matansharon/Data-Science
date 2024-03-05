import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
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
    for i in files:
        df=read_data_file(f"data/{i}")
        st.write(df.head())
    # df=read_data_file("data/amazon.csv")
    # if df is not None:
    #     st.write(df.head())
    file=st.file_uploader('Upload a file', type=['pdf','xlsx','csv'])
    if file:
        st.write('PDF file uploaded')
        st.write(file.type)
        # if file.type=="text/csv":
        #     df=pd.read_csv(file)
        #     st.write(f"the length of the dataframe as a string is: {len(df.to_string())}")
        #     st.write(f"number of rows in the dataframe is: {len(df)}")
        #     df_as_string=df.to_string()
        #     splits=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        #     docs=splits.split_documents(df_as_string)
        #     st.write(f"splits is: {docs}")
def get_all_files_in_directory(directory:str):
    
    files=os.listdir(directory)
    return files
def read_data_file(file_path:str):
    if file_path.endswith('.csv'):
        data_frame=pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        data_frame=pd.read_excel(file_path)
    return data_frame
    return data_frame

if __name__ == '__main__':
    main()
