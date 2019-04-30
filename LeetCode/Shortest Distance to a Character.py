# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.
#
# Example 1:
#
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

def shortestToChar(S, C):
    output = []
    last_C = -len(S)
    for i in range(len(S)):
        if S[i] == C:
            output.append(0)
            last_C = i
        else:
            next_dis = S[i:].find(C)
            if i - last_C < next_dis or next_dis < 0:
                output.append(i - last_C)
            else:
                output.append(next_dis)
    return output

print(shortestToChar("aaba","b"))