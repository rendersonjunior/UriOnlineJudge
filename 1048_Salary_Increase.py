# Salary Increase
'''Read the employee's salary, calculate and print the new employee's salary, as well the money earned and the increase
percentual obtained by the employee, with corresponding messages in Portuguese, as the below example.

Input

The input contains only a floating-point number, with 2 digits after the decimal point.

Output

Print 3 messages followed by the corresponding numbers (see example) informing the new salary, the among of money earned
and the percentual obtained by the employee. Note:
Novo salario:  means "New Salary"
Reajuste ganho: means "Money earned"
Em percentual: means "In percentage"

'''

def main():
    reajust_salary_table = [(0.00,    400.00,  0.15),
                            (400.01,  800.00,  0.12),
                            (800.01,  1200.00, 0.10),
                            (1201.00, 2000.00, 0.07),
                            (2000.01, 999999999999.00, 0.04)]

    salary_func = round(float(input()),2)

    for min, max, perc in reajust_salary_table:
        if round(min, 2) <= salary_func <= round(max,2):
            reajust_value = salary_func * perc
            percentage = str(round(perc*100))+" %"
            break

    new_salary = salary_func + reajust_value

    print("Novo salario: %.2f" % new_salary)
    print("Reajuste ganho: %.2f" % reajust_value)
    print("Em percentual: %s" % percentage)

if __name__ == "__main__":
    main()