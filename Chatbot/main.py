import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import helper_functions as hf
from dotenv import load_dotenv


#sidebar


def main():
    st.title('Chatbot')
    load_dotenv()
    docs=hf.get_all_files_in_directory('/Users/matansharon/python/Data_science/Chatbot/data')
    # os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')
    st.header('Chatbot')
    
    st.write("### Hello, I am a chatbot that can help you to talk to you documents.")
    st.write("#### on the side you can see the list of all the  documents that I can help you with.")
    st.write("#### Please choose one of the documents and start asking me questions.")
    
    with st.sidebar:

        add_vertical_space(10)
        st.write('Made By Matan Sharon')
        for i in docs:
            st.markdown("- " + i)
    ans=st.chat_input("Ask me a question")
    if ans:
        st.write("You: ",ans)
        st.write("Chatbot: ",ans)
    
    
    


if __name__ == '__main__':
    main()
