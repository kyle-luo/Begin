from random import *

number = randint(1,10)

def guess():

    print('please guess an integer from 1 - 10')
    x = input()
    while x != number:

        if x > number:
            print('too large')
            print('guess again')
            x = input()
        elif x < number:
            print('too small')
            print('guess again')
            x = input()
    print('correct')


guess()