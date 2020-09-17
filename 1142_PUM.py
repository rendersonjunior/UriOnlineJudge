# PUM
"""
Write a program that reads an integer N.
This N is the number of output lines printed by this program.

Input
The input file contains an integer N.

Output
Print the output according to the given example.

Input Sample
7

Output Sample
1 2 3 PUM
5 6 7 PUM
9 10 11 PUM
13 14 15 PUM
17 18 19 PUM
21 22 23 PUM
25 26 27 PUM
"""


def main():
    N = int(input())
    pum = 0
    for i in range(N):
        print(str(pum + 1) + " " + str(pum + 2) + " " + str(pum + 3) + " PUM")
        pum += 4


if __name__ == "__main__":
    main()