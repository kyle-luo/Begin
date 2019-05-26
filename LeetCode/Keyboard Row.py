import re

# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
#
# Example:
#
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]

class Solution:
    def findWords(self, words):
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        output = []
        for word in words:
            check = True
            if word[0].lower() in row1:
                cur = 1
                while check is True and cur < len(word):
                    if word[cur].lower() not in row1:
                        check = False
                    cur += 1
            elif word[0].lower() in row2:
                cur = 1
                while check is True and cur < len(word):
                    if word[cur].lower() not in row2:
                        check = False
                    cur += 1
            elif word[0].lower() in row3:
                cur = 1
                while check is True and cur < len(word):
                    if word[cur].lower() not in row3:
                        check = False
                    cur += 1
            if check == True:
                output.append(word)
        return output


class Solution2:
    def findWords(self, words):
        rows = re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$')
        return list(filter(rows.match, words))


class Solution3:
    def findWords(self, words):
        self.rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        self.output = []
        return list(filter(self.check, words))

    def check(self, word):
        output = []
        row = 0
        while row < len(self.rows):
            if word[0].lower() in self.rows[row]:
                cur = 1
                check = True
                while check is True and cur < len(word):
                    if word[cur].lower() not in self.rows[row]:
                        check = False
                    cur += 1
                if check == True:
                    output.append(word)
            row += 1
        return output