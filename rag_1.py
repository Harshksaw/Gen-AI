from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore



pdf_path = Path(__file__).parent / "assets" / "image.pdf"
loader = PyPDFLoader(pdf_path)




# Load the document
loader = PyPDFLoader(pdf_path)
documents = loader.load()
# Print the number of documents loaded
print(f"Number of documents loaded: {len(documents)}")
# Print the first document

# Print the first 500 characters of the first document

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

split_docs = text_splitter.split_documents(documents)

# print(f"Number of documents after splitting: {len(split_docs)}")


embedder = OpenAIEmbeddings(
    api_key="sk-",
    model="text-embedding-3-large",
)


vectorstore = QdrantVectorStore.from_documents(
    documents=[],
    url="http://localhost:6333",
    collection_name="learning_langchain",
embedding=embedder,
)

vector_store.add_documents(documents=split_docs)

retriever = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embedder,
)

search_result = retriever.similarity_search(
    query="What is api",

)