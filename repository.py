import csv


class Repository:
    def __init__(self, clients):
        self.clients = clients

    @staticmethod
    def add(row):
        with open('clients.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(row)
