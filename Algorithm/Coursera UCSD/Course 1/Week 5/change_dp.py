# Uses python3
import sys
import time

def get_change(m):
    if 1 < m < 4:
        if m == 2:
            return 2
        else:
            return 1
    else:
        s = [m for _ in range(m)]
        s[0] = 1
        s[1] = 2
        s[2] = 1
        s[3] = 1
        for i in range(4, m):
            a = s[i - 1] + 1
            b = s[i - 3] + 1
            c = s[i - 4] + 1
            s[i] = min(a, b, c)
        return s[m - 1]

def get_change_rec(m):
    if m == 1 or m == 2:
        return m
    elif m == 3:
        return 1
    elif m == 4:
        return 1
    else:
        a = get_change_rec(m - 1) + 1
        b = get_change_rec(m - 3) + 1
        c = get_change_rec(m - 4) + 1
        return min(a, b, c)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

    # start = time.time()
    # print(get_change_rec(m))
    # end1 = time.time()
    # print(end1 - start)
    # print(get_change(m))
    # print(time.time() - end1)
