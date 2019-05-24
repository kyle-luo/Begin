# Uses python3
import sys


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right <= left:
        return number_of_inversions
    ave = left + (right - left) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave + 1, right)
    number_of_inversions += merge(a, b, ave, left, right)
    return number_of_inversions


def merge(a, b, m, l, r):
    count = 0
    i = l
    j = m + 1
    cur = l
    while i <= m and j <= r:
        if a[i] < a[j]:
            b[cur] = a[i]
            i += 1
        else:
            b[cur] = a[j]
            j += 1
            count += 1
        cur += 1
    while i <= m:
        b[cur] = a[i]
        i += 1
        cur += 1
    while j <= r:
        b[cur] = a[j]
        j += 1
        cur += 1
        count += 1
    return count


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a) - 1))

