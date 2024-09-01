# from gpt_index import SimpleDirectoryReader, LLMPredictor, PromptHelper, GPTSimpleVectorIndex
# from langchain import OpenAI
# from Ipython.display import Markdown, display
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
import openai
import os


load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


loader = DirectoryLoader("/home/sharp/Documents/accounting/journals", glob="*", loader_cls=TextLoader)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
split_documents = text_splitter.split_documents(documents)


def get_embedding(text):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response['data'][0]['embedding']


knowledge_embeddings = {doc.metadata['source']: get_embedding(doc.page_content) for doc in split_documents if doc.page_content}

#
# vectorstore_from_docs = PineconeVectorStore.from_documents(
#     docs,
#     index_name=index_name,
#     embedding=embeddings
# )
#
#
# def construct_index(directory_path):
#     max_input_size = 4096
#     num_outputs = 300
#     max_chunk_overlap = 20
#     chunk_size_limit = 600
#
#     llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="gpt-4o", max_tokens=num_outputs))
#     prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
#
#     documents = SimpleDirectoryReader(directory_path).load_data()
#
#     index = GPTSimpleVectorIndex(
#         documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
#     )
#
#     index.save_to_disk('index.json')
#
#     return index
#
#
# def ask_ai():
#     index = GPTSimpleVectorIndex.load_from_disk('index.json')
#     while True:
#         query = input("What do you want to ask?")
#         response = index.query(query, response_mode="compact")
#         display(Markdown(f"Response: <b>{response.response}</b>"))
#
#
# construct_index('/home/sharp/Documents/accounting/journals')
