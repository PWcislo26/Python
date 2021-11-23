import csv


def get_data(path):
    with open(path, newline='', encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile, delimiter =',')
        data = list(reader)
    return data



