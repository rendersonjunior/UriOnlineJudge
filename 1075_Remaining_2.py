# Remaining 2
'''
Read an integer N. Print all numbers between 1 and 10000, which divided by N will give the rest = 2.

Input

The input is an integer N (N < 10000)

Output

Print all numbers between 1 and 10000, which divided by n will give the rest = 2, one per line.
'''


def main():
    n = int(input())

    try:
        assert (n < 10000)

        for i in range(1,10001):
            if i % n == 2:
                print(i)

    except AssertionError:
        pass


if __name__ == "__main__":
    main()