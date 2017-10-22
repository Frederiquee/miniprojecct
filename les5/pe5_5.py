#Schrijf functie gemiddelde(), die de gebruiker vraagt om een willekeurige zin in te voeren. De functie
#berekent vervolgens de gemiddelde lengte van de woorden in de zin en print dit uit.

def gemiddelde():
    willekeurige_zin = input("Vul een willekeurige zin in: ")
    lengte = (len(willekeurige_zin))
    gemiddelde_lengte = lengte / 2
    print(gemiddelde_lengte)

(gemiddelde())