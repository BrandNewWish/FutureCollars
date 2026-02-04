import pickle

from DataFile import DataFile


class PickleFile(DataFile):
    def load(self, src):
        with open(self.path, "rb") as f:
            self.data = pickle.load(f)

    def save(self, dst, data):
        with open(dst, "wb") as f:
            pickle.dump(data, f)
