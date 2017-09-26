def kaartnummer():
    infile = open('kaartnummers.txt')
    kaartlezen = infile.readlines()
    infile.close()

    aantal_regels = kaartlezen

for line in lines:
    info = line.split(', ')
    kaartnummers.append(info[0])
    klanten.append(input[1])

print('Deze file telt', len(lines), 'regels.')
print('Het grootste kaartnummer is: ', max(kaartnummers), 'en dat staat op regel', str.lines)