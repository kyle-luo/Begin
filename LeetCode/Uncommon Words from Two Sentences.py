# We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
#
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
# Return a list of all uncommon words.
#
# You may return the list in any order.
#
#
# Example 1:
#
# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
#
# Example 2:
#
# Input: A = "apple apple", B = "banana"
# Output: ["banana"]

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a = {}
        b = {}
        output = []
        for x in A.split():
            a[x] = a.get(x, 0) + 1
        for x in B.split():
            b[x] = b.get(x, 0) + 1
        for key, val in a.items():
            if val == 1:
                if key not in b:
                    output.append(key)
        for key, val in b.items():
            if val == 1:
                if key not in a:
                    output.append(key)
        return output


class Solution2:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a = {}
        output = []
        for x in A.split():
            a[x] = a.get(x, 0) + 1
        for x in B.split():
            a[x] = a.get(x, 0) + 1
        for key, val in a.items():
            if val == 1:
                output.append(key)
        return output