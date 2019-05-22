import random
import time


class QuickSort:
    def sort(self, A):
        self._sort(A, 0, len(A) - 1)

    def _sort(self, A, l, r):
        if l > r:
            return
        m = self._partition(A, l, r)
        self._sort(A, l, m - 1)
        self._sort(A, m + 1, r)

    def _partition(self, A, l, r):
        pivot = A[r]
        j = r
        for i in reversed(range(l, r)):
            if A[i] >= pivot:
                j -= 1
                A[i], A[j] = A[j], A[i]
        A[r], A[j] = A[j], A[r]
        return j


quick = QuickSort()


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

# a = [76, 92, 41, 29, 91, 9, 6, 99, 90, 89]
# quick.sort(a)
# print(a)


# b = [random.randint(1, 10000) for x in range(1000000)]
# start = time.time()
# quick.sort(b)
# end = time.time()
# print("Quick sort time: " + str(end - start))
#
# b = [random.randint(1, 10000) for x in range(1000000)]
# start = time.time()
# b.sort()
# end = time.time()
# print("Tim sort time:   " + str(end - start))