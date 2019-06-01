# Uses python3
import sys
import time

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def optimal_sequence_rec(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    else:
        a = b = n
        if n % 3 == 0:
            a = optimal_sequence_rec(n // 3) + 1
        if n % 2 == 0:
            b = optimal_sequence_rec(n // 2) + 1
        c = optimal_sequence_rec(n - 1) + 1
        return min(a, b, c)

def optimal_sequence_dp(n):
    rec = [None for _ in range(n + 1)]
    rec[1] = [0, [1]]
    rec[2] = [1, [1, 2]]
    rec[3] = [1, [1, 3]]
    for i in range(4, n + 1):
        a = b = i
        if i % 3 == 0:
            a = rec[a // 3][0] + 1
        if i % 2 == 0:
            b = rec[b // 2][0] + 1
        c = rec[i - 1][0] + 1
        s = min(a, b, c)
        if s == a:
            rec1 = rec[i // 3][1] + [i]
        elif s == b:
            rec1 = rec[i // 2][1] + [i]
        else:
            rec1 = rec[i - 1][1] + [i]
        rec[i] = [s, rec1]
    return rec[n]

def optimal_sequence_dp2(n):
    rec = [None for _ in range(n + 1)]
    rec[1] = 0
    if n > 1:
        rec[2] = 1
    if n > 2:
        rec[3] = 1
    if n > 3:
        for i in range(4, n + 1):
            a = b = i
            if i % 3 == 0:
                a = rec[i // 3] + 1
            if i % 2 == 0:
                b = rec[i // 2] + 1
            c = rec[i - 1] + 1
            rec[i] = min(a, b, c)
    seq = []
    num = n
    while num > 1:
        if n == 2:
            seq.append(2)
            break
        elif n == 3:
            seq.append(3)
            break
        seq.append(num)
        if num % 3 == 0:
            a = rec[num // 3] + 1
        if num % 2 == 0:
            b = rec[num // 2] + 1
        c = rec[num - 1] + 1
        s = min(a, b, c)
        if s == a:
            num = num // 3
        elif s == b:
            num = num // 2
        else:
            num = num - 1
    seq.append(1)
    return rec[n], reversed(seq)


input = sys.stdin.read()
n = int(input)

# sequence = list(optimal_sequence(n))
# print(len(sequence) - 1)
#
# for x in sequence:
#     print(x, end=' ')
#
# print("\n")

# print(optimal_sequence_rec(n))
#
# print("\n")

# start = time.time()
# final = optimal_sequence_dp(n)
# print(final[0])
# for x in final[1]:
#     print(x, end=' ')
# end = time.time()
# print(end - start)
# print("\n")

final = optimal_sequence_dp2(n)
print(final[0])
for x in final[1]:
    print(x, end=' ')

# print(time.time() - end)

