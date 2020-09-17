# Positives and Average


def main():
    sum_positives = 0
    qtd_positives = 0

    for x in range(6):
        number = float(input())
        if number >= 0:
            qtd_positives += 1
            sum_positives += number

    avg = sum_positives/qtd_positives

    print("%d valores positivos" % qtd_positives)
    print(format(avg,'.1f'))

if __name__ == "__main__":
    main()
