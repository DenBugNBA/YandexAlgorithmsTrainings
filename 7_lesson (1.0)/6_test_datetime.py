import datetime

b_day, b_month, b_year = 2, 5, 1988
d_day, d_month, d_year = 13, 11, 2005

birth_date = datetime.date(b_year, b_month, b_day)
death_date = datetime.date(d_year, d_month, d_day)

# print(birth_date.day)
# print(birth_date.month)
# print(birth_date.year)


if birth_date.month == 2 and birth_date.day == 29:
    eighteen_years = birth_date.replace(year=birth_date.year + 18, month=3, day=1)
else:
    eighteen_years = birth_date.replace(year=birth_date.year + 18)

print(eighteen_years, "- eighteen years")
print(eighteen_years < death_date, "- eighteen_years < death_day")
print()


d_day1, d_month1, d_year1 = 1, 3, 2020
death_date1 = datetime.date(d_year1, d_month1, d_day1)

last_date1 = death_date1 - datetime.timedelta(days=1)
print(last_date1)
print()

d_day2, d_month2, d_year2 = 1, 5, 2020
death_date2 = datetime.date(d_year2, d_month2, d_day2)

last_date2 = death_date2 - datetime.timedelta(days=1)
print(last_date2)
print(last_date2.year)
print()


b_day3, b_month3, b_year3 = 29, 2, 2008
birth_date3 = datetime.date(b_year3, b_month3, b_day3)
eighty_years = birth_date3.replace(year=birth_date3.year + 80)
print(eighty_years)

b_day4, b_month4, b_year4 = 29, 2, 2020
birth_date4 = datetime.date(b_year4, b_month4, b_day4)
# ValueError: day is out of range for month
# eighty_years2 = birth_date4.replace(year=birth_date4.year + 80)
