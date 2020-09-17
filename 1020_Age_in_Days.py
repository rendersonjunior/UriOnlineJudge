#Age in Days
age_days = int(input())

def convert_age(age_days):
    age_list = []
    age_list.append(int((age_days - (age_days % 365)) / 365))
    age_days -= 365*age_list[0]
    age_list.append(int((age_days - (age_days % 30)) / 30))
    age_days -= 30 * age_list[1]
    age_list.append(age_days)
    return age_list

# 1 year: 365 days
# 1 month: 30 days

years, months, days = convert_age(age_days)

print(str(years) +" ano(s)")
print(str(months)+" mes(es)")
print(str(days) +" dia(s)")