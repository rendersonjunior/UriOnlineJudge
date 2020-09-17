# Six Odd Numbers


def main():
    value = int(input())

    try:
        assert(value > 0)

        for odd in range(value, value+12):
            if odd % 2 != 0:
                print(odd)

    except AssertionError:
        pass


if __name__ == "__main__":
    main()
