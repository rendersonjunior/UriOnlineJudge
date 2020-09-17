emp_number = int(input())
hours_worked = int(input())
salary_per_hour = float(input())

print("NUMBER = "+str(emp_number))
print("SALARY = U$ "+str(format(hours_worked*salary_per_hour,'.2f')))