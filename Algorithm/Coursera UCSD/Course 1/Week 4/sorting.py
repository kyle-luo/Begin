# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    p = a[l]
    j = l
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

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    # if l >= r:
    #     return
    # k = random.randint(l, r)
    # a[l], a[k] = a[k], a[l]
    # #use partition3
    # m = partition2(a, l, r)

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
    m1, m2 = partition3(a, l, r)

    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')


# BELOW ARE TESTS

# def sortchange(a):
#     randomized_quick_sort(a, 0, len(a) - 1)
#
# while True:
#     a = [random.randint(1, 10000) for x in range(1000)]
#     b = a
#     c = a
#     sortchange(b)
#     c.sort()
#     if b == c:
#         print("ok")
#     else:
#         print("failed")
#         print(b)
#         print(c)
#         break