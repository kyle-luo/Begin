import random

def merge_sort(a):
    if len(a) == 1:
        return a
    m = int(len(a)/2)
    b = merge_sort(a[:m])
    c = merge_sort(a[m:])
    new_a = merge(b, c)
    return new_a


def merge(b, c):
    output = []
    while b != [] and c != []:
        B = b[0]
        C = c[0]
        if B < C:
            output.append(b.pop(0))
        else:
            output.append(c.pop(0))
    output += c + b
    return output


a = [1,564,7,9,79,7,4567,2,31,7,977,98,]
a = merge_sort(a)
print(a)

b = []
for x in range(10000):
    b.append(random.randint(1, 10000))
b = merge_sort(b)
print(b)