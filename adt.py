class Date:
    def __init__(self, a, b, c):
        self.d = a
        self.m = b
        self.y = c

    def day(self):
        print("day =", self.d)

    def month(self):
        print("month =", self.m)

    def year(self):
        print("year =", self.y)

def month_name(self):
    months = ["unknown", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    print("month name:", months[self.m - 1])

    def is_leap_year(self):
        if (self.y % 4 == 0 and self.y % 100 != 0) or (self.y % 400 == 0):
            print("This is a leap year")
        else:
            print("This is not a leap year")


d = Date(3, 20, 2000)

d.day()
d.month()
d.year()
d.month_name()
d.is_leap_year()
