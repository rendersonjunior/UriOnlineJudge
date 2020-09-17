# Even or Odd


def even_or_odd(number):
    if number % 2 == 0:
        return "EVEN"
    return "ODD"


def positive_or_negative(number):
    if number > 0:
        return "POSITIVE"
    return "NEGATIVE"


def main():

    n = int(input())

    try:
        assert (n < 10000)
        try:
            for i in range(n+1):
                x = int(input())
                if x == 0:
                    print("NULL")
                else:
                    print("%s %s" % (even_or_odd(x), positive_or_negative(x)))
        except EOFError:
            pass
    except AssertionError:
        pass

if __name__ == "__main__":
    main()
