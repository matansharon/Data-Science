import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import helper_functions as hf
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
    # os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')
    st.header('Chatbot')
    
    st.write('### Hello, I am a chatbot. How can I help you today?')
    
    
    
    


if __name__ == '__main__':
    main()
