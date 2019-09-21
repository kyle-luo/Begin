# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    opening_brackets_indexs = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            opening_brackets_indexs.append(i)
        if next in ")]}":
            last = opening_brackets_stack.pop()
            if last == "(" and next != ")":
                return i + 1
            if last == "[" and next != "]":
                return i + 1
            if last == "{" and next != "}":
                return i + 1
            opening_brackets_indexs.pop()
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_brackets_indexs.pop() + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
