# Logical Sequence 2
"""
Write an program that reads two numbers X and Y (X < Y). After this, show a sequence of 1 to y, passing to the next line to each X numbers.

Input
The input contains two integer numbers X (1 < X < 20) and Y (X < Y < 100000).

Output
Each sequence must be printed in one line, with a blank space between each number, like the following example.

Input Sample
3 99

Output Sample
1 2 3
4 5 6
7 8 9
10 11 12
...
97 98 99

"""


def main():
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    ret = ""
    for i in range(y):
        if ((i+1) % x) == 0:
            ret += str(i + 1)
            print(ret)
            ret = ""
            continue
        else:
            ret += str(i + 1) + " "
    if len(ret) > 0:
        print(ret)


if __name__ == "__main__":
    main()
