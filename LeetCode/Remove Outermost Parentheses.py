# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
#
# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
#
# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
#
# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
#
#
#
# Example 1:
#
# Input: "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:
#
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation:
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:
#
# Input: "()()"
# Output: ""
# Explanation:
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".


def removeOuterParentheses(S):
    mark1, mark2, mark3, delList = 0, 0, 0, []
    for x in range(len(S)):
        if S[x] == '(':
            if mark1 == 0:
                mark3 = x
            mark1 += 1
        else:
            mark2 += 1
        if mark1 == mark2:
                delList.append(mark3)
                delList.append(x)
                mark1, mark2 = 0, 0
    for x in reversed(delList):
        S = S[:x] + S[x+1:]
    return S

print(removeOuterParentheses("(()())(())(()(()))"))

def removeOuterParentheses(S):
    mark1, mark2, mark3, delList, SS = 0, 0, 0, [], list(S)
    for x in range(len(S)):
        if S[x] == '(':
            if mark1 == 0:
                mark3 = x
            mark1 += 1
        else:
            mark2 += 1
        if mark1 == mark2:
                delList.append(mark3)
                delList.append(x)
                mark1, mark2 = 0, 0
    for x in reversed(delList):
        SS.pop(x)
    return str(''.join(SS))

print(removeOuterParentheses("(()())(())(()(()))"))

def removeOuterParentheses(S):
    count, newList = 0, ''
    for x in range(len(S)):
        if S[x] == '(':
            if count > 0:
                newList += S[x]
            count += 1
        else:
            count -= 1
            if count != 0:
                newList += S[x]
    return newList

print(removeOuterParentheses("(()())(())(()(()))"))

def removeOuterParentheses(S):
    count, newList = 0, ''
    for x in range(len(S)):
        if S[x] == '(':
            if count > 0:
                newList += S[x]
            count += 1
        else:
            count -= 1
            if count != 0:
                newList += S[x]
    return newList

print(removeOuterParentheses("(()())(())(()(()))"))

def removeOuterParentheses(S):
    count, newList = 0, []
    for x in range(len(S)):
        if S[x] == '(':
            if count > 0:
                newList.append(S[x])
            count += 1
        else:
            count -= 1
            if count != 0:
                newList.append(S[x])
    return ''.join(newList)

print(removeOuterParentheses("(()())(())(()(()))"))