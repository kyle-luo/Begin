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
        pivot = A[l]
        j = l
        for i in range(l + 1, r + 1):
            if A[i] <= pivot:
                j += 1
                A[i], A[j] = A[j], A[i]
        A[l], A[j] = A[j], A[l]

        return j


quick = QuickSort()

a = [100,564,7,9,79,50,4567,2,31,7,977,98]
quick.sort(a)
print(a)


b = [random.randint(1, 10000) for x in range(1000000)]
start = time.time()
quick.sort(b)
end = time.time()
print("Quick sort time: " + str(end - start))

b = [random.randint(1, 10000) for x in range(1000000)]
start = time.time()
b.sort()
end = time.time()
print("Tim sort time:   " + str(end - start))