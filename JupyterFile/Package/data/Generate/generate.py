def Generasiya(n):
    generator = (i for i in range(n))
    generator = iter(generator)
    while True:
        try:
            print (next(generator))
        except StopIteration:
            break



