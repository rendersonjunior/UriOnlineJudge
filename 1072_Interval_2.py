# Interval 2


def main():
    qtd_test_case = int(input())

    try:
        assert (qtd_test_case < 10000)

        qtd_in = 0
        qtd_out = 0

        for x in range(qtd_test_case):
            if 10 <= int(input()) <= 20:
                qtd_in += 1
            else:
                qtd_out += 1

        print("%d in" % qtd_in)
        print("%d out" % qtd_out)
    except AssertionError:
        pass


if __name__ == "__main__":
    main()
