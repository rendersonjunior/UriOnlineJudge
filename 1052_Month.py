# Month


def main():

    month_in_year = {1: "January",
                     2: "February",
                     3: "March",
                     4: "April",
                     5: "May",
                     6: "June",
                     7: "July",
                     8: "August",
                     9: "September",
                     10: "October",
                     11: "November",
                     12: "December"}

    decimal_month = int(input())
    print(month_in_year.get(decimal_month))

if __name__ == "__main__":
    main()