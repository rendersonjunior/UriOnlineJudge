# Multiples of 13
"""
Write a program that reads two integer numbers X and Y
and calculate the sum of all number not divisible by 13 between them, including both.

Input
The input file contains 2 integer numbers X and Y without any order.

Output
Print the sum of all numbers between X and Y not divisible by 13,
including them if it is the case.
"""


def main():
    x = int(input())
    y = int(input())
    if x > y:
        total = x
        x = y
        y = total
    total = 0
    for i in range(x, y+1, 1):
        if (i % 13) != 0:
            total += i
    print(total)


if __name__ == "__main__":
    main()
