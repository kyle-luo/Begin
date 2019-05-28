# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
# #
# # We repeatedly make duplicate removals on S until we no longer can.
# #
# # Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
# #
# # Example 1:
# #
# # Input: "abbaca"
# # Output: "ca"
# # Explanation:
# # For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".


class Solution:
    def removeDuplicates(self, S: str) -> str:
        S = [char for char in S]
        output = []
        while len(S) > 0:
            if output == []:
                output = [S.pop(0)]
                if len(S) == 0:
                    break
            push = S.pop(0)
            if push == output[-1]:
                output.pop()
            else:
                output += push
        result = ''
        for char in output:
            result += char
        return result


class Solution2:
    def removeDuplicates(self, S: str) -> str:
        S = [char for char in S]
        output = []
        for char in S:
            if output == []:
                output.append(char)
            else:
                if char == output[-1]:
                    output.pop()
                else:
                    output.append(char)
        result = ''
        for char in output:
            result += char
        return result


class Solution3:
    def removeDuplicates(self, S: str) -> str:
        S = list[S]
        output = []
        for char in S:
            if output == []:
                output.append(char)
            else:
                if char == output[-1]:
                    output.pop()
                else:
                    output.append(char)
        return "".join(output)


class Solution4:
    def removeDuplicates(self, S: str) -> str:
        output = ''
        for char in S:
            if output == '':
                output += char
            else:
                if char == output[-1]:
                    output = output[:-1]
                else:
                    output += char
        return output