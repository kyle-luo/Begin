# Uses python3
import sys

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


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)

for x in sequence:
    print(x, end=' ')

print("\n")

print(optimal_sequence_rec(n))
