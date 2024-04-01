def zellers_congruence(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    h = (day + 13 * (month + 1) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
    return (h + 5) % 7 + 1

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def has_53_weeks(year):
    jan1 = zellers_congruence(year, 1, 1)
    return jan1 == 4 or (is_leap_year(year) and jan1 == 3)

def find_years_with_53_weeks(start_year, end_year):
    years_with_53_weeks = []
    for year in range(start_year, end_year + 1):
        if has_53_weeks(year):
            years_with_53_weeks.append(year)
    return years_with_53_weeks

# Example usage
start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))

years_with_53_weeks = find_years_with_53_weeks(start_year, end_year)

if len(years_with_53_weeks) > 0:
    print("Years with 53 weeks:")
    for year in years_with_53_weeks:
        print(year)
else:
    print("No years with 53 weeks found in the given period.")
