import csv

from DataFile import DataFile

class CSVFile(DataFile):
    def load(self, src):
        with open(self.path, newline="") as f:
            reader = csv.reader(f)
            self.data = list(reader)

    def save(self, dst, data):
        with open(self.path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)

