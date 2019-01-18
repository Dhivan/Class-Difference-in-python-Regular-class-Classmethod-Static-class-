# TIME PACKAGE - NOT MANDATORY
import time
# DATE & TIME PACKAGE FOR DATE FORMAT
import datetime


class regular:

    # CONSTRUCTOR CLASS
    def __init__(self):
        self.first = input("Enter first name")
        self.second = input("Enter Second name")
        self.pay = input("Enter the salary")

    # REGULAR CLASS FUNCTION
    def employe(self):
        print("{} {} has {} Salary".format(self.first, self.second, self.pay))
        return

    # CLASS-METHOD WITH FUNCTION
    @classmethod
    def details(cls, new_str):
        first, second, pay = new_str.split('-', 3)
        return print("Salary of {} is getting by {} {}".format(first, second, pay))

    # STATIC METHOD WITH FUNCTION
    @staticmethod
    def is_working(day):
        if day.weekday() == 5 or day.weekday() == 6:
            print("Weekend")
        else:
            print("Working Day")


while True:
    print("1: Regular class call")
    print("2: Class-method call")
    print("3: Staticmethod call")
    opt = int(input("Enter your choice"))
    if opt == 1:
        call_regular = regular()
        regular.employe(call_regular)
        time.sleep(2)
    elif opt == 2:
        str1 = input("Enter the String in format of Firstname-Secondname-salary")
        regular.details(str1)
        time.sleep(2)
    else:
        y = int(input("Enter the year"))
        m = int(input("Enter the month"))
        d = int(input("Enter the date"))
        working_day = datetime.date(y, m, d)
        print(regular.is_working(working_day))
