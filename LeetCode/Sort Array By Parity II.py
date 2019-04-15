# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
#
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
#
# You may return any answer array that satisfies this condition.
#
#
#
# Example 1:
#
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

def sortArrayByParityII(A):
    odd = []
    even = []
    result = []
    for x in A:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    for x in range(int((len(A)+1)/2)):
        result.append(even[x])
        result.append(odd[x])
    return result

print(sortArrayByParityII([2,3]))
print(sortArrayByParityII([4,1,1,0,1,0]))

def sortArrayByParityII(A):
    odd = []
    even = []
    for x in A:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    ziped = zip(even , odd)
    result = []
    for x in ziped:
        result += x
    return result

print(sortArrayByParityII([2,3]))
print(sortArrayByParityII([4,1,1,0,1,0]))

def sortArrayByParityII(A):
    odd = 1
    even = 0
    result = [None]*len(A)
    for x in A:
        if x % 2 == 0:
            result[even] = x
            even += 2
        else:
            result[odd] = x
            odd += 2
    return result

print(sortArrayByParityII([2,3]))
print(sortArrayByParityII([4,1,1,0,1,0]))

def sortArrayByParityII(A):
    odd = []
    even = []
    for x in A:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    ziped = zip(even, odd)
    result = []
    for x in ziped:
        for y in x:
            result.append(y)
    return result

print(sortArrayByParityII([2,3]))
print(sortArrayByParityII([4,1,1,0,1,0]))