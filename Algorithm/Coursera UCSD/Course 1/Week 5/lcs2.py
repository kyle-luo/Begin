#Uses python3

import sys

def lcs2(s, t):
    rec = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                rec[i][j] = rec[i - 1][j - 1] + 1
            else:
                a = rec[i - 1][j]
                b = rec[i][j - 1]
                c = rec[i - 1][j - 1]
                rec[i][j] = max(a, b, c)
    return rec[len(s)][len(t)]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
