import json

from DataFile import DataFile


class JSONFile(DataFile):
    def load(self, src):
        with open(self.path) as f:
            self.data = json.load(f)

    def save(self, dst, data):
        with open(dst, "w") as f:
            json.dump(data, f)

