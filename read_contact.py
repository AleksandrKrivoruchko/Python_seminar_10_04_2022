import csv


def read_contact(file_name='contacts.csv'):
    with open(file_name, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            for item in row:
                print(item)

# read_contact()
