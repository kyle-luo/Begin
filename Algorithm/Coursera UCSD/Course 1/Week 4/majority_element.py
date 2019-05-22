# Uses python3
import sys

def get_majority_element(a):
    count = {}
    for x in a:
        count[x] = count.get(x, 0) + 1
    for key in count.keys():
        if count[key] > len(a)/2:
            return key
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
