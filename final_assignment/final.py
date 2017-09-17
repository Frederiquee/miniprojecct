def standaardtarief(afstandKM):
    afstandprijs = 0
    if afstandKM <= 0:
        afstandPrijs = 0
    elif afstandKM > 0 and afstandKM <= 50:
        afstandprijs = afstandKM * 0.8
    elif afstandKM > 50:
        afstandprijs = (afstandKM * 0.6) + 15

    return afstandprijs

def ritprijs(leeftijd, weekendrit, afstandKM):

    if weekendrit == 'ja':
        if 12 <= int (leeftijd) <65:
            weekendkorting = 0.6
        elif int(leeftijd) < 12 or int(leeftijd) >= 65:
            weekendkorting = 0.65
    else:
        if 12 <= int(leeftijd) < 65:
            weekendkorting = 1
        elif int(leeftijd) < 12 or int(leeftijd) >=65:
            weekendkorting = 0.7

    afstandsprijs = standaardtarief(int(afstandKM))

    eindprijs = afstandsprijs + weekendkorting

    return eindprijs

prijs = ritprijs(input('Voer uw leeftijd in: ')), input('is het een weekendrit?'), input('wat is de afstand in kilometers? ')
print(prijs)