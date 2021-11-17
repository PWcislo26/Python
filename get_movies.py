import csv


def get_movies():
    with open('movies.csv', newline='', encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile, delimiter =',')
        data = list(reader)
    return data




