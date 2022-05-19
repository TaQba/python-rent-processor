import csv


class Loader:
    a_list = []

    def __init__(self, path):
        self.path = path
        self.fill_list()

    def fill_list(self, mode='r'):
        with open(self.path, mode=mode) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            self.a_list = ([dict(row) for row in csv_reader])

    def get_list(self):
        return self.a_list
