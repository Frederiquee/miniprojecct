def toon_aantal_kluizen_vrij():
    print('Er zijn nog 8 kluizen beschikbaar!')

def nieuwe_kluis():
    kluisnummers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]

    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    infile.close()

    for regel in regels:
        kluisinfo = regel.split(';')
        kluisnummer = int(kluisinfo[0])
        kluisnummers.remove(kluisnummer)

    if (len(kluisnummers) > 0):
        nieuwe_code = input("Geef een kluiscode op: ")
        nieuwe_nummer = kluisnummers[0]

        outfile = open('kluizen.txt', 'a')
        outfile.write(str(nieuwe_nummer) + ";" + nieuwe_code + '\n')

def kluis_openen():
    kluisnummer = input("Wat is het kluisnummer van uw kluisje: ")
    code = input("Wat is de code van uw kluisje: ")

    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    infile.close()

    if 'code' == 'kluisnummer':
        print("Uw kluisje gaat open!")
    else:
        print("U heeft het verkeerde wachtwoord ingevoerd, het kluisje gaat niet open.")

def kluis_teruggeven():
    kluisnummer = input("Wat is het kluisnummer van uw kluisje: ")
    code = input("Wat is de code van uw kluisje: ")

    if code and kluisnummer == 'kluizen.txt':
        print("Uw kluis is vrijgegeven! ")
    else:
        print("Dit is niet het juiste wachtwoord")


print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
print("2: Ik wil een nieuwe kluis")
print("3: Ik wil even iets uit mijn kluis halen")
print("4: Ik geef mijn kluis terug")
print()
optie = input("Welkom, voer uw keuze in: ")

if optie == '1':
    print('Uw keuze is 1')
    toon_aantal_kluizen_vrij()
elif optie == '2':
    print('Uw keuze is 2')
    nieuwe_kluis()
elif optie == '3':
    print('Uw keuze is 3')
    kluis_openen()
elif optie == '4':
    print('Uw keuze is 4')
    kluis_teruggeven()
else:
    print('Foute invoer, programma stopt!')
