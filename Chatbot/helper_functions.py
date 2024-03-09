from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
def load_and_split_docs():

# load the document and split it into chunks
    docs=os.list_dir('/Users/matansharon/python/Data_science/Chatbot/data')
    loader = TextLoader(docs)
    documents = loader.load()

# split it into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
def run__openSource_embedding(docs):
# create the open-source embedding function
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    docs=docs
# load it into Chroma
    db = Chroma.from_documents(docs, embedding_function)
    return db
def create_llm_chain(llm_name):
    llm=ChatOpenAI(model="gpt-3.5-turbo")
    template = """
        you are a helpful assitant,
        Question: {question}

        Answer: Let's think step by step."""

    prompt = PromptTemplate.from_template(template)
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain