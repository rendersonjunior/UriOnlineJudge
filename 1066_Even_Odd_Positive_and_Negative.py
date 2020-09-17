# Even, Odd, Positive and Negative


def main():
    qtd_even = 0
    qtd_odd = 0
    qtd_positive = 0
    qtd_negative = 0

    for i in range(5):
        i_number = int(input())

        # Par ou Impar
        if i_number % 2 == 0:
            qtd_even += 1
        else:
            qtd_odd += 1

        # Positivo ou Negativo, diferente de 0
        if i_number != 0:
            if i_number > 0:
                qtd_positive += 1
            else:
                qtd_negative += 1

    print("%d valor(es) par(es)" % qtd_even)
    print("%d valor(es) impar(es)" % qtd_odd)
    print("%d valor(es) positivo(s)" % qtd_positive)
    print("%d valor(es) negativo(s)" % qtd_negative)

if __name__ == "__main__":
    main()
