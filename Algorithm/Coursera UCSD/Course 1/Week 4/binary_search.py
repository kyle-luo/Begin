# Uses python3
import sys
import random


def binary_search(a, x):
    left, right = 0, len(a) - 1
    # write your code here
    while left <= right:
        mid = left + int((right - left)/2)
        # print(a[mid], end=": a mid \n")
        # print(x, end=": key \n")
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end=' ')
        print(binary_search(a, x), end=' ')

# BELOW ARE TESTS

# r1 = [random.randint(0, 10000) for x in range(100)]
# r2 = random.randint(0, 10000)
#
# while True:
#     if binary_search(r1, r2) == linear_search(r1, r2):
#         print("ok")
#     else:
#         print(r1)
#         print(r2)
#         print(linear_search(r1, r2))
#         print(binary_search(r1, r2))
#         break
