# Squared and Cubic
"""
Write a program that reads an integer N (1 < N < 1000).
This N is the number of output lines printed by this program.

Input
The input file contains an integer N.

Output
Print the output according to the given example.

Input Sample
5

Output Sample
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
"""


def main():
    try:
        n = int(input())
        assert(1 < n < 1000)

        for i in range(n):
            print(str(i+1) + " " + str(pow(i+1, 2)) + " " + str(pow(i+1, 3)))

    except AssertionError:
        pass


if __name__ == "__main__":
    main()
