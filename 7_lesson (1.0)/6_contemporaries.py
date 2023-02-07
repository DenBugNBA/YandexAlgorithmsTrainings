import datetime
import calendar


def get_day_of_eighteen_years(birth_date, death_date):
    eighteen_years = None

    if birth_date.month == 2 and birth_date.day == 29:
        eighteen_years = datetime.date(birth_date.year + 18, 3, 1)
    else:
        eighteen_years = birth_date.replace(year=birth_date.year + 18)

    if eighteen_years < death_date:
        return eighteen_years

    return None


def get_last_day(birth_date, death_date):
    eighty_years = None

    if birth_date.month == 2 and birth_date.day == 29:
        if calendar.isleap(birth_date.year + 80):
            eighty_years = birth_date.replace(year=birth_date.year + 80)
        else:
            eighty_years = datetime.date(birth_date.year + 80, 3, 1)
    else:
        eighty_years = birth_date.replace(year=birth_date.year + 80)

    if eighty_years <= death_date:
        return eighty_years
    else:
        return death_date


def find_sets_of_contemporaries(years):
    events = []

    for i in range(len(years)):
        b_day, b_month, b_year, d_day, d_month, d_year = years[i]

        birth_date = datetime.date(b_year, b_month, b_day)
        death_date = datetime.date(d_year, d_month, d_day)

        eighteen_years = get_day_of_eighteen_years(birth_date, death_date)
        if eighteen_years:
            last_day = get_last_day(birth_date, death_date)

            events.append((eighteen_years, 1, i + 1))
            events.append((last_day, -1, i + 1))
    events.sort()

    current_set = []
    result_sets = []
    added_new_num = False

    for i in range(len(events)):
        if events[i][1] == 1:
            current_set.append(events[i][2])
            added_new_num = True
        elif events[i][1] == -1:
            if added_new_num:
                result_sets.append(current_set.copy())
                added_new_num = False
            current_set.remove(events[i][2])

    return result_sets


n = int(input())
years = []
for _ in range(n):
    birth_day, birth_month, birth_year, death_day, death_month, death_year = map(
        int, input().split()
    )
    years.append(
        (birth_day, birth_month, birth_year, death_day, death_month, death_year)
    )

# 2
# 3
# years = [(2, 5, 1988, 13, 11, 2005), (1, 1, 1, 1, 1, 30), (1, 1, 1910, 1, 1, 1990)]
# 18-летие:         None                 0019-01-01              1928-01-01
# последний день:                        0030-01-01              1990-01-01

# 2
# years = [(12, 12, 1000, 12, 12, 1018), (12, 12, 1000, 13, 12, 1018)]
# 18-летие:         None                      1018-12-12
# последний день:                             1018-12-13

# 2
# 1 3
# years = [(2, 5, 1968, 13, 11, 2005), (1, 1, 1, 1, 1, 30), (1, 1, 1910, 1, 1, 1990)]

# 0
# years = [(2, 5, 1988, 13, 11, 2005), (1, 1, 1, 1, 1, 10), (2, 1, 1910, 1, 1, 1928)]

# 1 2
# 2 3 4
# years = [
#     (1, 1, 1900, 1, 1, 1950),
#     (1, 1, 1910, 1, 1, 1990),
#     (1, 1, 1960, 1, 1, 2000),
#     (1, 1, 1970, 1, 1, 2005),
# ]

# 2 3
# 3 4 1
# years = [
#     (1, 1, 1970, 1, 1, 2005),
#     (1, 1, 1900, 1, 1, 1950),
#     (1, 1, 1910, 1, 1, 1990),
#     (1, 1, 1960, 1, 1, 2000),
# ]

# years = [(28, 2, 2008, 3, 1, 2044)]

result_sets = find_sets_of_contemporaries(years)
if result_sets == []:
    print(0)
else:
    for result_set in result_sets:
        print(*result_set)
