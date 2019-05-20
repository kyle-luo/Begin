import random
import time

class QuickSort:
    def sort(self, A, l, r):
        if l > r:
            return
        m = self._partition(A, l, r)
        self.sort(A, l, m - 1)
        self.sort(A, m + 1, r)

    def _partition(self, A, l, r):
        # pivot = A[l]
        # j = l
        mid = int((r - l) / 2)
        print(mid)
        if A[l] <= A[mid] <= A[r] or A[r] <= A[mid] <= A[l]:
            j = mid
        elif A[mid] <= A[l] <= A[r] or A[r] <= A[l] <= A[mid]:
            j = l
        else:
            j = r
        print(j)
        pivot = A[j]
        for i in range(l + 1, r + 1):
            if A[i] <= pivot:
                j += 1
                A[i], A[j] = A[j], A[i]
        A[l], A[j] = A[j], A[l]
        return j


quick = QuickSort()

a = [100,564,7,9,79,50,4567,2,31,7,977,98]
quick.sort(a, 0, len(a) - 1)
print(a)


b = []
for x in range(1000000):
    b.append(random.randint(1, 10000))
start = time.time()
quick.sort(b, 0, len(b) - 1)
end = time.time()
print("Quick sort time: " + str(end - start))

b = []
for x in range(1000000):
    b.append(random.randint(1, 10000))65.L,L
start = time.time()
b.sort()
end = time.time()
print("Tim sort time: " + str(end - start))