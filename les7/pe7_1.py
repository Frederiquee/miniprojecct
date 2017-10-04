getal = eval(input('Geef een getal: '))
aantal_getallen = 0
som = getal
while getal != 0:
    getal = eval(input('Geef een getal: '))
    som += getal
    aantal_getallen += 1
else:
    print('Er zijn {} getallen ingevoerd, de som is {}'.format(aantal_getallen, som))
