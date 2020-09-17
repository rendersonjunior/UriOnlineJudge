# Sum of Consecutive Odd Numbers I


def main():
    value_x = int(input())
    value_y = int(input())
    sum_odd = 0
    if value_y < value_x:
        value_x, value_y = value_y, value_x

    for odd in range(value_x+1, value_y):

        if odd % 2 != 0:
            sum_odd += odd

    print(sum_odd)


if __name__ == "__main__":
    main()
