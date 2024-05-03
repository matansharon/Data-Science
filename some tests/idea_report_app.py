import streamlit as st
import pandas as pd
import numpy as np
import anthropic
import os
from dotenv import load_dotenv
load_dotenv()


def analyze_excel(file_path):
    
    df=pd.read_excel(file_path)
    df_as_string=df.to_string()
    client=anthropic.Anthropic(
    )
    
    message = client.messages.create(
        # model='claude-3-haiku-20240307',
        model='claude-3-opus-20240229',
        max_tokens=4096,
        temperature=0.2,
        system="""
        this is an excel file that contains data about the Elcam's medical company.
        each row is an idea came up in a meeting by Elcam's board of directors and management team.
        please analyze the data and provide insights about the data.
        after that create a calculation with a recommendation score for each idea.
        and finally, convert the data into a pandas dataframe and print it out a table format with the recommendation score order by the highest recommendation score .
        
        """,
        messages=[
            {"role": "user", "content": df_as_string}
        ]
    )
    st.write(message.content[0].text)
def main():

    st.title("Idea Report App")
    file_path='/Users/matansharon/python/Data_science/some tests/ideas.xlsx'
    
    if st.button("Analyze"):
        analyze_excel(file_path)
if __name__ == "__main__":
    main()