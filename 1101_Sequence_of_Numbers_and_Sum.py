# Sequence of Numbers and Sum
'''
Read an undetermined number of pairs values M and N (stop when any of these values is less or equal to zero). 
For each pair, print the sequence from the smallest to the biggest (including both) and the sum of consecutive integers 
between them (including both).
Input
The input file contains pairs of integer values M and N. The last line of the file contains a number zero or negative, 
or both.
Output
For each pair of numbers, print the sequence from the smallest to the biggest and the sum of these values, 
as shown below.
Input Sample
5 2
6 3
5 0
Output Sample
2 3 4 5 Sum=14
3 4 5 6 Sum=18
'''


def main():
    mn = input().split(" ")
    m = int(mn[0])
    n = int(mn[1])
    while m > 0 and n > 0:
        total = 0
        string_range = ''

        if m > n:
            n, m = m, n

        for s in range(m, n+1):
            string_range += str(s)+' '
            total += s

        print("%sSum=%d" % (string_range, total))

        mn = input().split(" ")
        m = int(mn[0])
        n = int(mn[1])


if __name__ == "__main__":
    main()
