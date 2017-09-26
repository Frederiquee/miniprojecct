def kaartnummer():
    infile = open('kaartnummers.txt')
    kaartlezen = infile.readlines()
    infile.close()

    kaartlijst = kaartlezen

    for name in kaartlijst:
        fl = name.split(',')
        print('{} heeft kaartnummer : {}'.format(fl[1].strip(), fl[0]))

kaartnummer()