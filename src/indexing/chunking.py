class PythonChunking:
    def __init__(self, files) -> None:
        self.files = files

    def read_files(self):
        self.data = dict()
        for file in self.files:
            try:
                with open(file, "r") as f:
                    data = f.read()
                self.data.update({"path": file, "text": data})
            except OSError:
                continue
        print(list(self.data.values())[1])
