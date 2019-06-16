# You have an array of logs.  Each log is a space delimited string of words.
#
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.
#
# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.
#
# Return the final order of the logs.
#
#
#
# Example 1:
#
# Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dlog = []
        llog = []
        llogstr = []
        for log in logs:
            if '0' <= log[-1] <= '9':
                dlog.append(log)
            else:
                id, string = log.split(' ', 1)
                if len(llog) != 0:
                    i = 0
                    while i < len(llog):
                        if string < llogstr[i]:
                            llogstr.insert(i, string)
                            llog.insert(i, log)
                            break
                        elif string == llogstr[i]:
                            if log < llog[i]:
                                llogstr.insert(i, string)
                                llog.insert(i, log)
                            else:
                                llogstr.insert(i + 1, string)
                                llog.insert(i + 1, log)
                            break
                        i += 1
                        if len(llog) == i:
                            llog.append(log)
                            llogstr.append(string)
                            break
                else:
                    llog.append(log)
                    llogstr.append(string)
        return llog + dlog

