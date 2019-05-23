# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave + 1, right)
    number_of_inversions += merge(a, b, )
    #write your code here

    return number_of_inversions
    # count = 0
    # if len(a) == 1:
    #     return a
    # m = int(len(a) / 2)
    # b = get_number_of_inversions(a[:m])[0]
    # c = get_number_of_inversions(a[m:])[0]
    # return merge(b, c, count)

def merge(a, b, left, right):
    count = 0
    l, m, r =


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    # print(get_number_of_inversions(a, b, 0, len(a)))
    print(get_number_of_inversions(a)[1])

