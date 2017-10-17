import datetime
import csv

bestand = 'inloggers.csv'

#gebruik hier een herhalingslus:
naam = input('Wat is je achternaam? ')
voorl = input('Wat zijn je voorletters? ')
gbdatum = input('Wat is je geboortedatum? ')
email = input('Wat is je e-mail adres? ')

#wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file

with open('inloggers.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow((''))

    while True:
        naam = input('Wat is je achternaam?: ')

        if naam == 'einde':
            break

        voorl = input('Wat zijn je voorletters? ')
        gbdatum = input('Wat is je geboortedatum? ')
        email = input('Wat is je e-mail adres? ')

        writer.writerow((datetime, voorl, naam, gbdatum, email))

with open('inloggers.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    for row in reader:
        print("{};{};{};{};{}".format(datetime,voorl,naam,gbdatum,email))