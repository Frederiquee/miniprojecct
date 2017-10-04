cijfers = {'Joost':9, 'Kevin':8, 'Michelle':10, 'Marvin': 9, 'Melle':7, 'Bas':10, 'Kris':6, 'Floor':7}

for item in cijfers.items():
    if item[1] > 9:
        print(item[0], item[1])