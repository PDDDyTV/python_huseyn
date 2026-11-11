def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return "31"
    elif month in [4, 6, 9, 11]:
        return "30"
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return "29"
        else:
            return "28"


month = int(input("месяц"))
year = int(input("год"))
print(days_in_month(month, year))
