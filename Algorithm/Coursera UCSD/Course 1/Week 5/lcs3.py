#Uses python3
import sys

def lcs3(a, b, c):
    rec = [[[0 for _ in range(len(c) + 1)] for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1, len(c) + 1):
                if a[i - 1] == b[j - 1] and a[i - 1] == c[k - 1]:
                    rec[i][j][k] = rec[i - 1][j - 1][k - 1] + 1
                else:
                    x = rec[i - 1][j][k]
                    y = rec[i][j - 1][k]
                    z = rec[i][j][k - 1]
                    d = rec[i - 1][j - 1][k]
                    e = rec[i - 1][j][k - 1]
                    f = rec[i][j - 1][k - 1]
                    g = rec[i - 1][j - 1][k - 1]
                    rec[i][j][k] = max(x, y, z, d, e, f, g)
    return rec[len(a)][len(b)][len(c)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    # print(a)
    # print(type(a))
    print(lcs3(a, b, c))
