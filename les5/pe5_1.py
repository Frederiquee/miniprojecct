def convert (Celsius):
    frah = Celsius * 1.8 + 32

    return frah

def table():
    print(' F       C')
    for i in range (-30, 41, 10):
        print('{:5} {:7}'.format(convert(i), float(i)))

table()