# Uses python3
import sys

def optimal_weight(capacity, weights):
    # write your code here
    dp = [0 for _ in range(capacity + 1)]

    for i in range(len(weights)):
        for j in reversed(range(capacity + 1)):
            if weights[i] <= j:
                dp[j] = max(dp[j], weights[i] + dp[j - weights[i]])
        # print(dp)
    return dp[capacity]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
