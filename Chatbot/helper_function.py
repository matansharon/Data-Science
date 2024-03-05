import os
import pandas as pd
import PyPDF2
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
def extract_text_from_pdf(file_path:str):
    # pdf_file=open(file_path,'r')
    pdf_reader=PyPDF2.PdfReader(file_path)
    text=''
    for page in pdf_reader.pages:
        text+=page.extract_text()
    return text