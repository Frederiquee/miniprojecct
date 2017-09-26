#Schrijf functie gemiddelde(), die de gebruiker vraagt om een willekeurige zin in te voeren. De functie
#berekent vervolgens de gemiddelde lengte van de woorden in de zin en print dit uit.
willekeurige_zin = input("Vul een willekeurige zin in: ")
print(len(willekeurige_zin))

gemiddelde = len(willekeurige_zin) * 2 /len(willekeurige_zin)
print(gemiddelde)
