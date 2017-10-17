import csv

with open('artikelen.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')

    for row in reader:
        print('Het duurste artikel is{} en die kost{} euro.'.format(row[2],row[4]))
print('Er zijn slechts{} exemplaren in voorraad van het product met nummer{}'.format(row[3],row[0]))
print('In totaal hebben wij 1073 producten in ons magazijn liggen')