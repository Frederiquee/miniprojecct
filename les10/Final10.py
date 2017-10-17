import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

Stationsdict = processXML('stations.xml')
Stations = Stationsdict['Stations']['Station']

#stap 1
print('Dit zijn de codes en types van de 4 stations:')
for Station in Stations:
    print('{} - {}'.format(Station['Code'], Station['Type']))

#stap2
print()
print('Dit zijn alle stations met één of meer synoniemen:')
for Station in Stations:
    if Station['Synoniemen'] != None:
        print('{} - {}'.format(Station['Code'],Station['Synoniemen']))

# stap3
print()
print('Dit is de lange naam van elk station:')
for Station in Stations:
    print('{} - {}'.format(Station['Code'],Station['Namen']['Lang']))