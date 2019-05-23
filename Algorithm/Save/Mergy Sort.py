import random


class MergeSort:
    def sort(self, a):
        if len(a) == 1:
            return a
        m = int(len(a)/2)
        b = self.sort(a[:m])
        c = self.sort(a[m:])
        new_a = self.merge(b, c)
        return new_a

    def merge(self, b, c):
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


merge = MergeSort()

a = [1,564,7,9,79,7,4567,2,31,7,977,98]
a = merge.sort(a)
print(a)

b = []
for x in range(100000):
    b.append(random.randint(1, 10000))
b = merge.sort(b)
print(b)