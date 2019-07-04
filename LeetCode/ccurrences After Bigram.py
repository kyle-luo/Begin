# Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.
#
# For each such occurrence, add "third" to the answer, and return the answer.
#
# Example 1:
# Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
# Output: ["girl","student"]
#
# Example 2:
# Input: text = "we will we will rock you", first = "we", second = "will"
# Output: ["we","rock"]

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        output = []
        for i in range(len(text) - 2):
            if text[i] == first and text[i + 1] == second:
                output.append(text[i + 2])
        return output