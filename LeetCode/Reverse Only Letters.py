# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
#
# Example 1:
#
# Input: "ab-cd"
# Output: "dc-ba"
#
# Example 2:
#
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
#
# Example 3:
#
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        alpha = []
        output = []
        for char in S:
            if char.isalpha():
                alpha.append(char)
        for char in S:
            if char.isalpha():
                output.append(alpha.pop())
            else:
                output.append(char)
        return ''.join(output)

