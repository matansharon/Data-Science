from langchain_community.document_loaders import TextLoader,DirectoryLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os


def get_all_files_in_directory(directory: str):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
def load_and_split_docs():
    

# load the document and split it into chunks
    loader=DirectoryLoader('/Users/matansharon/python/Data_science/Chatbot/data')
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    return docs
# load the document and split it into chunks
    

# split it into chunks
    
def run__openSource_embedding(docs):
# create the open-source embedding function
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    docs=docs
# load it into Chroma
    db = Chroma.from_documents(docs, embedding_function)
    return db
def create_llm_chain(llm_name:str='gpt-3.5-turbo',temperture: float=0):
    llm=ChatOpenAI(model="gpt-3.5-turbo")
    template = """
        you are a helpful assitant,
        Question: {question}

        Answer: Let's think step by step."""

    prompt = PromptTemplate.from_template(template)
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain
def run():
    docs=load_and_split_docs()
    db=run__openSource_embedding(docs)
    llm_chain=create_llm_chain('gpt-3.5-turbo')
    return llm_chain,db