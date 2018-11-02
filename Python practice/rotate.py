# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.
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

def rotate(a,b):
    result = ''
    for char in a:
        if char != ' ':
            result += shift_n_letters(char, b)
        else:
            result += ' '
    return result


print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???