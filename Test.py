from datetime import date
import calendar

start_time = "25/12/2021"
day = int(start_time[:2])
month = int(start_time[3:5])
year = int(start_time[6:10])

if 1900 <= year <= 2100:
    if 1 <= month <= 12:
        _, last_day = calendar.monthrange(year, month)
        if 1 < day < last_day:
            return date(year, month, day).isoformat()
else:
    return "Error: Invalid date"


if 1<day< last_day

res = date(year, month, day).isoformat()
print(final_date)


year = 2022
month = 3
_, last_day = calendar.monthrange(year, month)

print(last_day)

# year = int(input("Введите год :"))
#
# print((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
