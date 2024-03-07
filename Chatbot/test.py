# from dotenv import load_dotenv
# import os
# from langchain_community.document_loaders import TextLoader
# from langchain_community.vectorstores import FAISS
# from langchain_openai import OpenAIEmbeddings
# from langchain_text_splitters import CharacterTextSplitter
# load_dotenv()
# loader = TextLoader("/Users/matansharon/python/Data_science/transcript.txt")
# documents = loader.load()
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# docs = text_splitter.split_documents(documents)
# embeddings = OpenAIEmbeddings()
# db = FAISS.from_documents(docs, embeddings)
# query = "What did the president say about Ketanji Brown Jackson"
# docs = db.similarity_search(query)
# print(docs)




# import PyPDF2
# import os
# files= os.listdir('/Users/matansharon/Downloads/papers')#in the mackbook
# for file in files:
#     if file.endswith('.pdf'):
#         pdf_reader=PyPDF2.PdfReader(f'/Users/matansharon/Downloads/papers/{file}')
#         text=''
#         for page in pdf_reader.pages:
#             text+=page.extract_text()
#             text+="\n\n"
#         with open(f'/Users/matansharon/python/Data_science/Chatbot/data/{file[:-4]}.txt','w') as f:
#             f.write(text)
        