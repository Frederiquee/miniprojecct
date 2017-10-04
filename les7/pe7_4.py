def ticker(filename):
    infile = open (filename, 'r')
    inhoud = infile.readlines() #dit is een lijst, dus kan je nog niet splitten
    infile.close()

    ticker_dict = {}

    for regel in inhoud:
        tickerinfo_lijst = regel.split(':')
        companyname = tickerinfo_lijst[0]
        symbol = tickerinfo_lijst[1].strip()
        ticker_dict[symbol] = companyname

    return ticker_dict

tickers = ticker('symbols.txt')
name = input('Enter Company name: ')

for item in tickers.items():
    if item[1] == name:
        print('Ticker symbol: ' + item[0])

symbol = input('Enter Ticker symbol: ')
print('Company name: ' + tickers[symbol])
