woord = input('Geef een string van vier letters: ')
aantal_letters = len(woord)


while aantal_letters == 4:
    input('Inlezen van correcte string: {} is geslaagd'.format(woord))
    print(aantal_letters)
else:
    woord = input('Geef een string van vier letters: ')
    print('{} heeft {} letters'.format(woord, aantal_letters))