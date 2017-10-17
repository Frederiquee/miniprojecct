import random

def monopolyworp():
    count = 1
    while True:
        dobbelsteen1 = random.randrange(1,7)
        dobbelsteen2 = random.randrange(1,7)
        totaal = dobbelsteen1 + dobbelsteen2
        if (dobbelsteen1 == dobbelsteen2) and count == 3:
            print('{} + {} = {} (direct naar gevangenis!)'.format(dobbelsteen1, dobbelsteen2, totaal))
            break
        elif dobbelsteen1 == dobbelsteen2:
            print('{} + {} = {} (dubbel)'.format(dobbelsteen1, dobbelsteen2, totaal))
            count += 1
            continue
        else:
            print('{} + {} = {}'.format(dobbelsteen1, dobbelsteen2, totaal))
            break


monopolyworp()
