import datetime

formatd = "%d/%m/%Y"
formath = "%H:%M:%S"

birthday = datetime.date(2026, 2, 11)
print("Birthday:", birthday.strftime(formatd))
time_actually = datetime.datetime.now().strftime(formath)
print("Time actually:", time_actually)
today = datetime.date.today()
diferenca = today - birthday
print(f"Faz {diferenca.days} que você fez aniversário")
date_actually = datetime.datetime.now()
print("Data e hora atual: ", date_actually.strftime("%d/%m/%Y %H:%M:%S"))