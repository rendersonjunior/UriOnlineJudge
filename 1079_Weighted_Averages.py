# Weighted Averages
'''
Read an integer N, which represents the number of following test cases.
Each test case consists of three floating-point numbers, each one with one digit after the decimal point.
Print the weighted average for each of these sets of three numbers, considering that the first number has weight 2,
the second number has weight 3 and the third number has weight 5.

Input

The input file contains an integer number N in the first line.
Each N following line is a test case with three float-point numbers, each one with one digit after the decimal point.

Output

For each test case, print the weighted average according with below example.
'''


def main():
    n = int(input())

    for i in range(n):
        float_average = input().split(" ")
        a = round(float(float_average[0]), 1)
        b = round(float(float_average[1]), 1)
        c = round(float(float_average[2]), 1)

        average = round(((a*2.0)+(b*3.0)+(c*5.0))/10.0, 1)
        print(average)

if __name__ == "__main__":
    main()
