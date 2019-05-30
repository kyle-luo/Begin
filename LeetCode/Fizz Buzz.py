# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for x in range(n):
            if (x + 1) % 5 == 0:
                if (x + 1) % 3 == 0:
                    output.append('FizzBuzz')
                else:
                    output.append('Buzz')
            elif (x + 1) % 3 == 0:
                output.append('Fizz')
            else:
                output.append(str(x + 1))
        return output


class Solution2:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for x in range(n):
            if (x + 1) % 5 == 0 and (x + 1) % 3 == 0:
                output.append('FizzBuzz')
            elif (x + 1) % 5 == 0:
                output.append('Buzz')
            elif (x + 1) % 3 == 0:
                output.append('Fizz')
            else:
                output.append(str(x + 1))
        return output