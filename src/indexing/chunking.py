from langchain_text_splitters import Language, RecursiveCharacterTextSplitter


class PythonChunking:
    def __init__(self, files, chunk_size) -> None:
        self.files = files
        self.splitter = RecursiveCharacterTextSplitter.from_language(
            language=Language.PYTHON, chunk_size=chunk_size, chunk_overlap=0
        )

    def read_files(self):
        self.data = dict()
        for file in self.files:
            try:
                with open(file, "r") as f:
                    data = f.read()
                self.data.update({"path": file, "text": data})
            except OSError:
                continue
        for data in self.splitter.create_documents(
            [list(self.data.values())[1]]
        ):
            print(data)
