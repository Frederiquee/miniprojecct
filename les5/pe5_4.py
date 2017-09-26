
import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y %H:%M:%S")
print(s)

infile = open('hardlopers.txt')
regels = infile.readlines()
infile.close()

print(regels)

file2 = open('hardlopers.txt', 'a')
tijd = time.strftime('a %d %b %Y %H:%M:%S')
naam = input("Wat is je naam?: ")
hardloper = tijd + naam

file2.write(hardloper)
file2.write('\n')
print()