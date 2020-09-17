# Sequence IJ 3
'''
Make a program that prints the sequence like the following exemple.
Input
This problem doesn't have input.
Output
Print the sequence like the example below.
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13
'''


def main():
    n = 5
    for i in range(1, 10, 2):
        n += 2
        for j in range(n, n-3, -1):
            print("I=%d J=%d" % (i, j))


if __name__ == "__main__":
    main()
