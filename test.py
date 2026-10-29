from langchain_text_splitters import RecursiveCharacterTextSplitter
import BM25


text = "Hello my name is Yoo. I am the goat."
splitter = RecursiveCharacterTextSplitter(chunk_size=10, chunk_overlap=0)
chunks = splitter.split_text(text)
retrieval = BM25.index(chunks)
print(retrieval.search(["hello"], k=1))
