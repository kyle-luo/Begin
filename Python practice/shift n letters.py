# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    if ord('a') <= ord(letter) + n  <=  ord('z'):
        return chr(ord(letter) + n)
    elif ord(letter) + n  >  ord('z'):
        order = ord(letter) + n
        while order > ord('z'):
            order -= 26
        return chr(order)
    else:
        order = ord(letter) + n
        while order < ord('a'):
            order += 26
        return chr(order)



print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i