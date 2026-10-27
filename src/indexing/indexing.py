from pathlib import Path
from src.indexing.chunking import PythonChunking


class Indexing:
    def __init__(self):
        self.path = Path("data/raw")
        self.get_files()
        self.py_chunk = PythonChunking(self.python_files)
        self.py_chunk.read_files()

    def get_files(self):
        self.python_files = list(self.path.rglob("*.py"))
        self.markdown_files = list(self.path.rglob("*.md"))
