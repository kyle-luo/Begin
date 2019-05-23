import random


class MergeSort:
    def msort(self, a):
        b = ['' for x in range(len(a))]
        return self.sort(a, b, 0, len(a) - 1)

    def sort(self, a, b, l, r):
        # print(r, end=" r\n")
        # print(l, end=" l\n")
        # if r <= l:
        #     return #self.sort(a, b, l, r)
        if r > l:
            m = l + (r - l) // 2
            self.sort(a, b, l, m)
            self.sort(a, b, m + 1, r)
            self.merge(a, b, m, l, r)
        return b

    def merge(self, a, b, m, l, r):
        i = l
        j = m + 1
        cur = l
        while i <= m and j <= r:
            if a[i] <= a[j]:
                b[cur] = a[i]
                i += 1
            else:
                b[cur] = a[j]
                j += 1
            cur += 1
        while i <= m:
            b[cur] = a[i]
            i += 1
            cur += 1
        while j <= r:
            b[cur] = a[j]
            j += 1
            cur += 1

merge = MergeSort()

# a = [1,564,7,9,79,7,4567,2,31,7,977,98]

while True:
    a = [random.randint(1, 1000) for x in range(1000)]
    b = a
    c = a
    merge.msort(b)
    c.sort()
    if b == c:
        print("ok")
    else:
        print("failed")
        print(b)
        print(c)
        break

# b = []
# for x in range(100000):
#     b.append(random.randint(1, 10000))
# b = merge.sort(b)
# print(b)