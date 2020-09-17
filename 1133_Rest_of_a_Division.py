# Rest of a Division
"""
Write a program that reads two integer numbers X and Y.
Print all numbers between X and Y which dividing it by 5 the rest is equal to 2 or equal to 3.

Input
The input file contains 2 any positive integers, not necessarily in ascending order.

Output
Print all numbers according to above description, always in ascending order.

Input Sample
10
18

Output Sample
12
13
17
"""


def main():
    x = int(input())
    y = int(input())
    # troca valores para colocar em sequencia
    if x > y:
        x, y = y, x

    for i in range(x+1, y, 1):
        if i % 5 == 2 or i % 5 == 3:
            print(i)


if __name__ == "__main__":
    main()
