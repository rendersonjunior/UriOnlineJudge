seller_name = input("")
salary_monthly = round(float(input("")),2)
value_sales_sold = round(float(input("")),2)

comission = (value_sales_sold*0.15)

print("TOTAL = R$ "+str(format(salary_monthly+comission,'.2f')))

