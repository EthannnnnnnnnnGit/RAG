from src.indexing.indexing import Indexing
import fire


class Pipeline:
    def default(self):
        self.index()
        self.search()
        self.search_dataset()
        self.answer()
        self.answer_dataset()
        self.evaluate()

    def index(self, max_chunk_size: int = 2000):
        self.index = Indexing()
        max_chunk_size

    def search(self, k: int = 5):
        k

    def search_dataset(self):
        pass

    def answer(self):
        pass

    def answer_dataset(self):
        pass

    def evaluate(self):
        pass


if __name__ == "__main__":
    fire.Fire(component=Pipeline)
