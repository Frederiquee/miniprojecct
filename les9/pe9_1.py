#aantal_personen = int(input('Met hoeveel personen gaat u op reis?: '))
#prijs = 4356

#kosten_per_persoon = prijs / aantal_personen
#print(kosten_per_persoon )


try:
    Aantal_personen = input('Met hoeveel personen gaat u op reis?: ')
    intAantal_personen = int(Aantal_personen)
    if intAantal_personen > 0:
        print('U gaat met {} personen op reis!'.format(intAantal_personen))
    if intAantal_personen == 0:
        print('Delen door nul kan niet!')
    if intAantal_personen < 0:
        print('Negatieve getallen zijn niet toegestaan!')
except:
    print('Vul het aantal personen in door de getallen 0-9 te gebruiken!')

prijs = 4356
kosten_per_persoon = prijs / intAantal_personen
print('De kosten per persoon bedragen {} euro'.format(kosten_per_persoon))

