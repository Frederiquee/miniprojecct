import csv

try:
    with open('gamers.csv', 'r'):
        infile = open('gamers.csv', 'r')
        regels = infile.readlines()
        infile.close()




    for row in reader:
        if hoogste_score < ints(row[2]):
            hoogste_score