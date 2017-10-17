def verdubbelB(b):
    b = b + b
    return b

b = 7
verdubbelB(7)
print(verdubbelB(7))

import time
print(time.strftime(("%H:%M:%S")))

def f(y):
    return 2*y + 1

def g(x):
    x = 5 + x + 10
    return x
print(f(3) + g(3))