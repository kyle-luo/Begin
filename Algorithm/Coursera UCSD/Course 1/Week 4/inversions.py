# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions

def check(a):
    count = 0
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            check = i - 1
            while check >= 0:
                if a[check] > a[i]:
                    count += 1
                check -= 1
    return count



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    # print(get_number_of_inversions(a, b, 0, len(a)))
    print(check(a))


