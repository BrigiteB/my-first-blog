import itertools

def generator(a):
    my_gen = ((str(a) + ' x ' + str(i) + ' = ' + str(a*i)) for i in itertools.count())
    return(my_gen)


g = generator(1)
while k print(next(g))


# >>> list(itertools.islice(  generator(5)    , 0, 10))
# ['5 x 1 = 5', '5 x 2 = 10', '5 x 3 = 15', '5 x 4 = 20', '5 x 5 = 25', '5 x 6 = 30', '5 x 7 = 35', '5 x 8 = 40', '5 x 9 = 45', '5 x 10 = 50']
