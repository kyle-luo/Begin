import random
import time

class QuickSortP3:
    def sort(self, a):
        self._sort(a, 0, len(a) - 1)

    def _sort(self, a, l, r):
        mid = int((r - l) / 2)
        if l > r:
            return
        if a[l] <= a[mid] <= a[r] or a[r] <= a[mid] <= a[l]:
            k = mid
        elif a[mid] <= a[l] <= a[r] or a[r] <= a[l] <= a[mid]:
            k = l
        else:
            k = r
        a[l], a[k] = a[k], a[l]
        m1, m2 = self._partition(a, l, r)
        self._sort(a, l, m1 - 1)
        self._sort(a, m2 + 1, r)

        # m = self._partition(a, l, r)
        # self._sort(a, l, m - 1)
        # self._sort(a, m + 1, r)

    def _partition(self, a, l, r):
        p = a[l]
        j = l

        # for i in range(l + 1, r + 1):
        #     if a[i] <= p:
        #         j += 1
        #         a[i], a[j] = a[j], a[i]
        # a[l], a[j] = a[j], a[l]

        while j <= r:
            if a[j] < p:
                a[j], a[l] = a[l], a[j]
                j += 1
                l += 1
            elif a[j] > p:
                a[j], a[r] = a[r], a[j]
                r -= 1
            else:
                j += 1
        return [l, r]


quick = QuickSortP3()

# BELOW ARE TESTS CODE

while True:
    a = [random.randint(1, 1000) for x in range(10)]
    b = a
    c = a
    quick.sort(b)
    c.sort()
    if b == c:
        print("ok")
    else:
        print("failed")
        print(b)
        print(c)
        break

# a = [100,564,7,9,79,99,4567,2,31,7,977,98]
# quick.sort(a)
# print(a)

# a = [random.randint(1, 100) for x in range(10)]
# print(a)
# quick.sort(a)
# print(a)

# b = [random.randint(1, 10000) for x in range(100000)]
# start = time.time()
# quick.sort(b)
# end = time.time()
# print("Quick sort time: " + str(end - start))
#
# b = [random.randint(1, 10000) for x in range(100000)]
# start = time.time()
# b.sort()
# end = time.time()
# print("Tim sort time: " + str(end - start))