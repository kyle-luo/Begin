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