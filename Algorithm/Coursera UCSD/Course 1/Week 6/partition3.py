# Uses python3
import sys
import itertools

def partition3(values):
    t = sum(values)
    if t % 3 != 0 or len(values) < 3:
        return 0

    pp = t // 3
    print(pp)

    dp = [0 for _ in range(t + 1)]
    count = 0

    for i in range(len(values)):
        for j in reversed(range(pp + 1)):
            if values[i] <= j:
                dp[j] = max(dp[j], values[i] + dp[j - values[i]])
                if dp[j] == pp:
                    count += 1
    if count == 3:
        return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

