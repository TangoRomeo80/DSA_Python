class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        if month == 1:
            return day
        if month == 2:
            return day + 31
        if month == 3:
            return day + 59 + self.isLeapYear(year)
        if month == 4:
            return day + 90 + self.isLeapYear(year)
        if month == 5:
            return day + 120 + self.isLeapYear(year)
        if month == 6:
            return day + 151 + self.isLeapYear(year)
        if month == 7:
            return day + 181 + self.isLeapYear(year)
        if month == 8:
            return day + 212 + self.isLeapYear(year)
        if month == 9:
            return day + 243 + self.isLeapYear(year)
        if month == 10:
            return day + 273 + self.isLeapYear(year)
        if month == 11:
            return day + 304 + self.isLeapYear(year)
        if month == 12:
            return day + 334 + self.isLeapYear(year)

    def isLeapYear(self, year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        return False

