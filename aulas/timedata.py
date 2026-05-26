import datetime

date_actually = datetime.datetime.now()
formato = "%d/%m/%Y %H:%M:%S"
date_formated = date_actually.strftime(formato)

print("Actual Date: ", date_formated)

print("\n=== FIRST DATE ===\n")

try:
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))

    data1 = datetime.date(year, month, day)

    print("\n=== SECOND DATE ===\n")

    year2 = int(input("Year: "))
    month2 = int(input("Month: "))
    day2 = int(input("Day: "))

    data2 = datetime.date(year2, month2, day2)

    difference = data2 - data1

    print(f"\nDifference of {difference.days} days")

except ValueError:
    print("ta errado saporra ai")