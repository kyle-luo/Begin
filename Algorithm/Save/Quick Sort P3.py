import random
import time

class QuickSortP3:
    def sort(self, A):
        self._sort(A, 0, len(A) - 1)

    def _sort(self, A, l, r):
        mid = int((r - l) / 2)
        if l > r:
            return
        if A[l] <= A[mid] <= A[r] or A[r] <= A[mid] <= A[l]:
            k = mid
        elif A[mid] <= A[l] <= A[r] or A[r] <= A[l] <= A[mid]:
            k = l
        else:
            k = r
        A[l], A[k] = A[k], A[l]
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


quick = QuickSortP3()

# while True:
#     a = [random.randint(1, 1000) for x in range(10)]
#     b = a
#     c = a
#     quick.sort(b)
#     c.sort()
#     if b == c:
#         print("ok")
#     else:
#         print("failed")
#         print(b)
#         print(c)
#         break

# a = [100,564,7,9,79,99,4567,2,31,7,977,98]
# quick.sort(a)
# print(a)

# a = [random.randint(1, 100) for x in range(10)]
# print(a)
# quick.sort(a)
# print(a)

b = [random.randint(1, 10000) for x in range(1000000)]
start = time.time()
quick.sort(b)
end = time.time()
print("Quick sort time: " + str(end - start))

b = [random.randint(1, 10000) for x in range(1000000)]
start = time.time()
b.sort()
end = time.time()
print("Tim sort time: " + str(end - start))