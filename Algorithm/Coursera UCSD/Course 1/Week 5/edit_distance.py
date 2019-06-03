# Uses python3
def edit_distance(s, t):
    s = [None] + [x for x in s]
    t = [None] + [x for x in t]

def edit_rec(s, t, i, j):
    if i == 0 and j == 0:
        return 0
    a = b = c = d = max(len(s), len(t))
    if s[i] == t[j] and i > 0 and j > 0:
        a = edit_rec(s, t, i - 1, j - 1)
    if s[i] == t[j - 1] and j > 0:
        b = edit_rec(s, t, i, j - 1) + 1
    if s[i - 1] == t[j] and i > 0:
        c = edit_rec(s, t, i - 1, j) + 1
    # if s[i - 1] != t[j - 1] and i > 0 and j > 0:
    if i > 0 and j > 0:
     d = edit_rec(s, t, i - 1, j - 1) + 1
    return min(a, b, c, d)


def edit_dp(s, t):
    rec = [[None for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    for i in range(len(t) + 1):
        rec[0][i] = i
    for i in range(len(s) + 1):
        rec[i][0] = i
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                rec[i][j] = rec[i - 1][j - 1]
            else:
                a = rec[i - 1][j] + 1
                b = rec[i][j - 1] + 1
                c = rec[i - 1][j - 1] + 1
                rec[i][j] = min(a, b, c)
    return rec[len(s)][len(t)]


if __name__ == "__main__":
    # print(edit_distance(input(), input()))
    s, t = input(), input()
    # s = [None] + [x for x in s]
    # t = [None] + [x for x in t]
    s = [x for x in s]
    t = [x for x in t]
    # print(edit_rec(s, t, len(s) - 1, len(t) - 1))
    print(edit_dp(s, t))