from datetime import datetime, date

current = datetime.now()
print(current)
print(current.time())

today = date.today()
print(today)

formatted = current.strftime("%d-%m-%Y")
print(formatted)

date1 = date(2000, 5, 15)
date2 = date(2026, 5, 22)

difference = date2 - date1
print(difference.days)
