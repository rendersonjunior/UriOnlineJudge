# Sequence IJ 4
'''
Make a program that prints the sequence like the following example.
Input
This problem doesn't have input.
Output
Print the sequence like the example below.
I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?
'''


def main():
    i = 0
    do = True
    while do:
        for j in range(1, 4):
            i = float(round(i, 1)) if i-int(i) > 0 else int(round(i, 0))
            print("I=%s J=%s" % (str(i), str(j+i)))
        i += 0.2
        do = True if i <= 2.0 else False

if __name__ == "__main__":
    main()
