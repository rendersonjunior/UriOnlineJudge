# Ascending and Descending
'''
Read an undetermined number of pairs of integer values.
Write a message for each pair indicating if this two numbers are in ascending or descending order.
Input
The input file contains several test cases.
Each test case contains two integer numbers X and Y. The input will finished when X = Y.
Output
For each test case print “Crescente”, if the values X and Y are in ascending order, otherwise print “Decrescente”.
Input Sample
5 4
7 2
3 8
2 2
Output Sample
Decrescente
Decrescente
Crescente
'''


def main():
    xy = input().split(' ')
    x = int(xy[0])
    y = int(xy[1])

    while x != y:
        order = "Crescente" if x < y else "Decrescente"
        print(order)

        xy = input().split(' ')
        x = int(xy[0])
        y = int(xy[1])

if __name__ == "__main__":
    main()
