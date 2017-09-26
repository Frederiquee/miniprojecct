#Schrijf een functie seizoen(maand) die als parameter maandnummer meekrijgt. Het functie-resultaat
#is het seizoen die bij die maand hoort. Nummers 3 t/m 5 horen bij lente, 9 t/m 11 ‘herfst’ etc.
def seizoen_():
    print("Het is winter!")

def seizoen():
    print("Het is lente!")

def seizoen__():
    print("Het is zomer!")

def seizoen4():
    print("Het is herfst!")

print("Maanden 12, 1 en 2 zijn winter. ")
print("Maanden 3, 4 en 5 zijn lente. ")
print("Maanden 6, 7 en 8 zijn zomer. ")
print("Maanden 9, 10 en 11 zijn herfst. ")

optie = input("Naar welk seizoen bent u op zoek, geef dit aan door een maand aan te geven: ")

if optie == '12':
    print("U heeft uw maand gekozen!")
    seizoen_()
if optie == '1':
    print("U heeft uw maand gekozen!")
    seizoen_()
if optie == '2':
    print("U heeft uw maand gekozen!")
    seizoen_()
if optie == '3':
    print("U heeft uw maand gekozen!")
    seizoen()
if optie == '4':
    print("U heeft uw maand gekozen!")
    seizoen()
if optie == '5':
    print("U heeft uw maand gekozen!")
    seizoen()
if optie == '6':
    print("U heeft uw maand gekozen!")
    seizoen__()
if optie == '7':
    print("U heeft uw maand gekozen!")
    seizoen__()
if optie == '8':
    print("U heeft uw maand gekozen!")
    seizoen__()
if optie == '9':
    print("U heeft uw maand gekozen!")
    seizoen4()
if optie == '10':
    print("U heeft uw maand gekozen!")
    seizoen4()
if optie == '11':
    print("U heeft uw maand gekozen!")
    seizoen4()