# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# #
# # Example 1:
# # Input: "Let's take LeetCode contest"
# # Output: "s'teL ekat edoCteeL tsetnoc"

def reverseWords(s):
    list = s.split(' ')
    newstring = ''
    for x in list:
        newstring += x[::-1] + ' '
    return newstring[:-1]

print(reverseWords("Let's take LeetCode contest"))

def reverseWords(s):
    list = s.split(' ')
    newstring = ''
    for x in list:
        for y in 
        newstring += x[::-1] + ' '
    return newstring[:-1]