import csv

def gamers():
    with open('gamers.csv', 'r') as MyCSVFile:
        reader = csv.reader(MyCSVFile, delimiter=';')

        for row in reader:
            print("De hoogste score is: {} behaald door {} op {}".format(row[2], row[0], row[1]))

gamers()
