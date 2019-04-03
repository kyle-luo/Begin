# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
#
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#
# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]
#
#
# Example 1:
#
# Input: "IDID"
# Output: [0,4,1,3,2]
# Example 2:
#
# Input: "III"
# Output: [0,1,2,3]
# Example 3:
#
# Input: "DDI"
# Output: [3,2,0,1]

def diStringMatch(S):
    output = []
    input = list(range(len(S)+1))
    for s in S:
        if s == 'I':
            output.append(input[0])
            input = input[1:]
        else:
            output.append(input[-1])
            input = input[:-1]
    return output + input

print(diStringMatch("IDID"))


def diStringMatchh(S):
    output = []
    sup = 0
    for s in S:
        if s == 'D':
            output.append(len(S))
            S = S[1:]
        else:
            output.append(sup)
            sup += 1
    return output + [sup]

print(diStringMatchh('IDID'))


def diStringMatchhh(S):
    output = []
    high = len(S)
    low = 0
    for s in S:
        if s == 'D':
            output.append(high)
            high -= 1
        else:
            output.append(low)
            low += 1
    return output + [low]

print(diStringMatchhh('IDID'))


def diStringMatchhhh(S):
    l = 0
    r = len(S)
    for ch in S:
        if ch == 'I':
            yield l
            l += 1
        else:
            yield r
            r -= 1
    yield l

print(diStringMatchhhh('IDID'))