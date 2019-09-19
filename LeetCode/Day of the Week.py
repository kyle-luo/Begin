# Given a date, return the corresponding day of the week for that date.
#
# The input is given as three integers representing the day, month and year respectively.
#
# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
#
#
#
# Example 1:
#
# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"
# Example 2:
#
# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"
# Example 3:
#
# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def year_type(y):
            yt = 0
            if y % 4 == 0:
                if y % 100 == 0:
                    if y % 400 == 0:
                        yt = 1
                else:
                    yt = 1
            return yt

        month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        week_day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        days = 365 * (year - 1971)
        for y in range(1971, year):
            if year_type(y) == 1: days += 1
        for m in range(month):
            days += month_day[m]
        if year_type(year) == 1 and month > 2:
            days += 1
        days += day
        final = (days + 5 - 1) % 7
        return week_day[final]

