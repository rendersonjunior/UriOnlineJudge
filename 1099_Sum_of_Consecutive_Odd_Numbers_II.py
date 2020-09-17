# Sum of Consecutive Odd Numbers II
'''
Read an integer N that is the number of test cases.
Each test case is a line containing two integer numbers X and Y.
Print the sum of all odd values between them, not including X and Y.
Input
The first line of input is an integer N that is the number of test cases that follow.
Each test case is a line containing two integer X and Y.
Output
Print the sum of all odd numbers between X and Y.
'''


def main():
    n = int(input())
    for i in range(1, n+1):
        sum_odd = 0
        test_case = input().split(' ')
        x, y = test_case
        x = int(x)
        y = int(y)
        if y < x:
            x, y = y, x
        for s in range(x+1, y):
            if s % 2 != 0:
                sum_odd += s
        print(sum_odd)


if __name__ == "__main__":
    main()
