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
    rec = [[None for _ in range(len(t))]for _ in range(len(s))]
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == s[j]:
            s




if __name__ == "__main__":
    # print(edit_distance(input(), input()))
    s, t = input(), input()
    s = [None] + [x for x in s]
    t = [None] + [x for x in t]
    print(edit_rec(s, t, len(s) - 1, len(t) - 1))