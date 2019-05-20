import random
import time

class QuickSortPlus:
    def sort(self, A):
        self._sort(A, 0, len(A) - 1)

    def _sort(self, A, l, r):
        if l > r:
            return
        m = self._partition(A, l, r)
        self._sort(A, l, m - 1)
        self._sort(A, m + 1, r)

    def _partition(self, A, l, r):
        mid = int((r - l) / 2)
        if A[l] <= A[mid] <= A[r] or A[r] <= A[mid] <= A[l]:
            j = mid
        elif A[mid] <= A[l] <= A[r] or A[r] <= A[l] <= A[mid]:
            j = l
        else:
            j = r
        pivot = A[j]
        small = None
        big = None
        while l != j and r != j:
            while big is None and l != j:
                if A[l] > pivot:
                    big = l
                l += 1
            while small is None and r != j:
                if A[r] < pivot:
                    small = r
                r -= 1
            try:
                A[big], A[small] = A[small], A[big]
            except:
                break
            small = None
            big = None
        if r > j:
            start = j
            for i in range(start + 1, r + 1):
                if A[i] <= pivot:
                    j += 1
                    A[i], A[j] = A[j], A[i]
            A[start], A[j] = A[j], A[start]
        if l > j:
            end = j
            for i in reversed(range(l, end)):
                if A[i] >= pivot:
                    j -= 1
                    A[i], A[j] = A[j], A[i]
            A[end], A[j] = A[j], A[end]
        return j


quick = QuickSortPlus()

# a = [100,564,7,9,79,99,4567,2,31,7,977,98]
# quick.sort(a)
# print(a)

a = [random.randint(1, 100) for x in range(10)]
print(a)
quick.sort(a)
print(a)

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
# print("Tim sort time: " + str(end - start))