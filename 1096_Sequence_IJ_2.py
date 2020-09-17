# Sequence IJ 2
'''
Make a program that prints the sequence like the following exemple.
Input
This problem doesn't have input.
Output
Print the sequence like the example below.
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=7
I=3 J=6
I=3 J=5
...
I=9 J=7
I=9 J=6
I=9 J=5
'''


def main():
    for i in range(1, 10, 2):
        for j in range(7, 4, -1):
            print("I=%d J=%d" % (i, j))


if __name__ == "__main__":
    main()
