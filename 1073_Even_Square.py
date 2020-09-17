# Even Square
import math


def main():
    n = int(input())
    try:
        assert (5 < n < 2000)

        for x in range(1, n+1):
            if x % 2 == 0:
                square = int(math.pow(x, 2))
                print("%d^2 = %d" % (x, square))

    except AssertionError:
        pass

if __name__ == "__main__":
    main()
