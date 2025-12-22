from time import time

def test():
    x1 = time()
    print(2**(2**13) *69)
    x2 = time()
    print(x2-x1)

test() 