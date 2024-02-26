import csv

with open('temp.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['Zineb', 'Lahraoui'])

