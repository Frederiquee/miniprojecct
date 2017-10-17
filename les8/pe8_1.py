bruin = {'Deurne', 'Helmond Brouwhuis', 'Helmond', 'Helmond \'t Hout', '27', 'Best', 'Boxtel'}
groen = {'Weert', 'Heeze', 'Geldrop', 'Eindhoven', 'Beukenlaan', '24', 'Boxtel'}

print('Deze plaatsen komen in beide trajecten voor: {}'.format(groen.intersection(bruin)))

print('Deze plaatsen komen niet bij elkaar voor in de trajecten: {}'.format(bruin.difference(groen)))

print('De trajecten komen langs deze plaatsen: {}'.format(groen.union(bruin)))