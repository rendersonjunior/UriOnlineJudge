# Highest and Position
'''
Read 100 integer numbers. Print the highest read value and the input position.

Input

The input file contains 100 distinct positive integer numbers.

Output

Print the highest number read and the input position of this value, according to the given example.
'''


def main():
    high = int(input())
    position = 1
    for x in range(2, 101):
        n = int(input())
        if n > high:
            high = n
            position = x

    print(str(high)+'\n'+str(position))

if __name__ == "__main__":
    main()
