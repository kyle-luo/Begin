# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.


def hammingDistance(x,y):
    x = bin(x).replace('0b','')
    y = bin(y).replace('0b','')
    count = 0
    if len(x) < len(y):
        for i in range(len(x)):
            if x[-1] != y[-1]:
                count +=1
                x = x[0:-1]
                y = y[0:-1]
            else:
                x = x[0:-1]
                y = y[0:-1]
        count += y.count('1')
    else:
        for i in range(len(y)):
            if x[-1] != y[-1]:
                count +=1
                x = x[0:-1]
                y = y[0:-1]
            else:
                x = x[0:-1]
                y = y[0:-1]
        count += x.count('1')
    return count


print(hammingDistance(93,73))