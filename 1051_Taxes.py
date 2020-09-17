# Taxes


def main():
    salary_taxes = [(0.00,    2000.00, 0.00),
                    (2000.01, 3000.00, 0.08),
                    (3000.01, 4500.00, 0.18),
                    (4500.00, 9999999999999.00, 0.28)]
    salary_taxes.sort(reverse=True)
    salary = float(input())

    salary_tax = 0
    for min_s, max_s, perc_s in salary_taxes:
        if min_s <= salary <= max_s:
            tax_value = round((salary - round(min_s)), 2)
            salary_tax += round((tax_value * perc_s), 2)
            salary -= tax_value

    if salary_tax > 0:
        print("R$ %.2f" % salary_tax)
    else:
        print("Isento")

if __name__ == "__main__":
    main()
