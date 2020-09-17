# Sequence IJ 1
'''
Make a program that prints the sequence like the following example.

Input

This problem doesn't have input.

Output

Print the sequence like the example below.

I=1 J=60
I=4 J=55
I=7 J=50
...
I=? J=0
'''


def main():
    i = 1
    for j in range(60, -1, -5):
        print("I=%d J=%d" % (i, j))
        i += 3

if __name__ == "__main__":
    main()
