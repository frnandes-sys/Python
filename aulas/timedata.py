import datetime

date_actually = datetime.datetime.now()
year = date_actually.year
month = date_actually.month
day = date_actually.day
print("Dia:", day, "Mês:", month,"Ano:", year, "\n")

formato = "%d/%m/%Y %H:%M:%S"
date_formated = date_actually.strftime(formato)

data_atual = datetime.date.today()
um_ano = datetime.timedelta(days=365)
data_futura = data_atual + um_ano
format = "%d/%m/%Y"
print("Data daqui a um ano:", data_futura.strftime(format),"\n")

print("Actual Date:", date_formated)


# codigo base

print("\n=== CALCULATE THE DIFFERENCE BETWEEN DATES ===\n")

try:
    year = int(input("Fist - Year: "))
    month = int(input("First - Month: "))
    day = int(input("Fisrt - Day: "))

    data1 = datetime.date(year, month, day)

    print("\n=== SECOND DATE ===\n")

    year2 = int(input("Second -Year: "))
    month2 = int(input("Second - Month: "))
    day2 = int(input("Second - Day: "))

    data2 = datetime.date(year2, month2, day2)

    difference = data2 - data1

    print(f"\nThe Difference is {difference.days} days")

except ValueError:
    print("ta errado saporra ai")