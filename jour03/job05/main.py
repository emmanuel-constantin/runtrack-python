def premier ():
    for x in range(2, 1000):
        for y in range (2, x):
            if x % y == 0:
                break
        else:
            print(x, " est un nombre premier")
premier()

