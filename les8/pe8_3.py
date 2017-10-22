def code(invoerstring):
    resultaat = ''

    for resultaat in invoerstring:
        resultaat += chr(ord(resultaat)+3)

    return resultaat

print(code(input('Geef uw naam, beginstation en eindstation: ')))