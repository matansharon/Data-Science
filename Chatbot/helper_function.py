import os
import pandas as pd
import PyPDF2

def read_data_files(directory:str):
    files=os.listdir(directory)
    
    data_files=[]
    for file in files:
        if file.endswith('.csv'):
            data_files.append(pd.read_csv(f'data/{file}'))
        elif file.endswith('.xlsx'):
            data_files.append(pd.read_excel(f'data/{file}'))
        # elif file.endswith('.pdf'):
        #     data_files.append(extract_text_from_pdf(f'data/{file}'))
    return data_files
    
    
def extract_text_from_pdf(file_path:str):
    # pdf_file=open(file_path,'r')
    pdf_reader=PyPDF2.PdfReader(file_path)
    text=''
    for page in pdf_reader.pages:
        text+=page.extract_text()
    return text

