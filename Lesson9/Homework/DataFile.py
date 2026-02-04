from abc import ABC, abstractmethod


class DataFile(ABC):
    def __init__(self, path):
        self.path = path
        self.data = []

    @abstractmethod
    def load(self, src):
        pass

    @abstractmethod
    def save(self, dst, data):
        pass

    def apply_changes(self, changes):
        for change in changes:
            try:
                x, y, value = change.split(",",2)
                x = int(x)
                y = int(y)
                self.data[x][y] = value
            except (ValueError, IndexError):
                print(f"Skipping invalid change: {change}")

    def display(self):
        for row in self.data:
            print(",".join(row))

    def get_data(self):
        return self.data

