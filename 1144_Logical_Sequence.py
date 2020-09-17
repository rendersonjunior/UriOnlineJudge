# Logical Sequence
"""
Write a program that reads an integer N.
N * 2 lines must be printed by this program according to the example below.
For numbers with more than 6 digits, all digits must be printed
(no cientific notation allowed).

Input
The input file contains an integer N (1 < N < 1000).

Output
Print the output according to the given example.

Input Sample
5

Output Sample
1 1 1
1 2 2
2 4 8
2 5 9
3 9 27
3 10 28
4 16 64
4 17 65
5 25 125
5 26 126
"""


def main():
    try:
        n = int(input())
        assert(1 < n < 1000)

        for i in range(n):
            value = int(i+1)
            print(str(value) + " " + str(pow(value, 2)) + " " + str(pow(value, 3)))
            print(str(value) + " " + str(pow(value, 2)+1) + " " + str(pow(value, 3)+1))
    except AssertionError:
        pass


if __name__ == "__main__":
    main()
