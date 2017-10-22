from collections import Counter

def namen():
    naamlst = []
    while True:
        xnaam = str(input("Volgende naam: "))
        if xnaam != "":
            naamlst.append(xnaam)
        elif xnaam == "":
            naamdict = Counter(naamlst)
            for item in naamdict.items():
                if item [1] == 1:
                    print("Er is " + str(item[1]) + " student met de naam " + str(item[0]))
                else:
                    print("Er zijn " + str(item[1]) + " studenten met de naam " + str(item[0]))
            break

namen()