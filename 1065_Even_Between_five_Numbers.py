# Even Between five Numbers


def main():
    qtd_even = 0

    for i in range(5):
        if int(input()) % 2 == 0:
            qtd_even += 1

    print("%d valores pares" % qtd_even)


if __name__ == "__main__":
    main()
