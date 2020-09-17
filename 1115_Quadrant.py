# Quadrant
'''
Write a program to read the coordinates (X, Y) of an indeterminate number of points in Cartesian system.
For each point write the quadrant to which it belongs.
The program finish when at least one of two coordinates is NULL (in this situation without writing any message).
Input
The input contains several tests cases. Each test case contains two integer numbers.
Output
For each test case, print the corresponding quadrant which these coordinates belong, as in the example.
Input Sample
2 2
3 -2
-8 -1
-7 1
0 2
Output Sample
primeiro
quarto
terceiro
segundo
'''


def main():
    condition = True
    while condition:
        coordinates = input().split(' ')

        x = int(coordinates[0])
        y = int(coordinates[1])

        if x > 0 < y:
            print("primeiro")
        elif x < 0 < y:
            print("segundo")
        elif x < 0 > y:
            print("terceiro")
        elif x > 0 > y:
            print("quarto")
        else:
            pass
        condition = False if x == 0 or y == 0 else True


if __name__ == "__main__":
    main()
