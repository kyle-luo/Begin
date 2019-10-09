# python3
import collections

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

def max_sliding_window(sequence, m):
    track = collections.deque()
    output = []
    for i in range(len(sequence)):
        if track and track[0] < i - m + 1:
            track.popleft()
        while track and sequence[track[-1]] < sequence[i]:
            track.pop()
        track.append(i)
        if i >= m - 1:
            output.append(sequence[track[0]])
    return output



if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))

