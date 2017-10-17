def inlezen_beginstation(stationslijst):
    while True:
        begin = input('Wat is je beginstation?: ')
        if begin in stationslijst:
            break
        else:
            print('Dit station staat niet in het systeem.')
    return begin

def inlezen_eindstation(stationslijst, beginstation):
    while True:
        eind = input('Wat is je eindstation?: ')
        if eind in stationslijst and stationslijst.index(beginstation) >= stationslijst.index(eind):
            print('De trein komt niet langs dit station.')
        elif eind not in stationslijst:
            print('De trein komt niet langs {}'.format(eind))
        elif eind in stationslijst and stationslijst.index(beginstation) < stationslijst.index(eind):
            break
    return eind

def omroepen_reis(stationslijst, beginstation, eindstation):

    print()
    print('Het beginstation {} is het {}e station in het traject.'.format(beginstation, stations.index(beginstation)+1))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindstation, stations.index(eindstation)+1))
    print('De afstand bedraagt {} stations.'.format(stations.index(eindstation)-stations.index(beginstation)))
    prijs = 5
    totale_prijs = prijs * stations.index(eindstation)- stations.index(beginstation)
    print('De prijs van het kaartje is {} euro.'.format(totale_prijs))
    print()
    print('Jij stapt in de trein in: {}'.format(beginstation))
    for regel in range(stations.index(beginstation)+1,stations.index(eindstation)):
        print('- {}'.format(stations[regel]))
    print('Jij stapt uit in: {}'.format(eindstation))


#Jouw functies komen hier!!
stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'AmsterdamSloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert','Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)

