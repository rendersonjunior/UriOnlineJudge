# Positive Numbers


def main():
    sum_positive = 0

    for x in range(6):
        if float(input()) >= 0:
            sum_positive += 1

    print("%d valores positivos" % sum_positive)

if __name__ == "__main__":
    main()
