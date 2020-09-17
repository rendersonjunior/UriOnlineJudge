# Critical Wave
"""
The task is simple. Through some critical points in 2D, you have to draw a wave like curve.
Your goal is to include as many points as possible.

There will be an imaginary line y = a, which we call the major axis for the curve.
All the points on the curve should have different x coordinates. Their y coordinates should be of form a-1 or a+1.

Two consecutive points on the curve should have a difference of 2 in their y coordinate.

Input
There will be no more than 222 test cases.
Each test case starts with an integer N, the number of points in the test case.
In the next N lines, there will be N pair of integers giving the x and y coordinate of the points.
There will be no more than 1000 points in each test case.
All coordinates are integers -- they'd fit in a signed 2 byte integer data type. The data must be read of default input.

Output
For each test case print a number
-- the maximum number of critical points that can be included in a curve drawn from the given points.

Input Sample
10
0 1
1 0
1 -1
2 -2
3 1
3 -1
3 -2
4 1
4 -1
5 -1
10
0 2
2 0
1 -1
2 -2
3 1
3 -1
3 -2
4 1
4 -1
5 –1

Output Sample
4
3

“If you don’t consider your life as a journey you will advance nowhere
 and life will appear to you as an endless and hopeless track.”
"""
MAX_TEST_CASE = 222
MAX_POINT_CASE = 1000


def verify_difference(y):
    if y == 1 or y == -1:
        return True
    else:
        return False


def main():
    list_entries = []

    #   Entry data
    test_case = 1
    while True:
        if test_case > MAX_TEST_CASE:
            break
        try:
            size_test_case = int(input())
            if size_test_case > MAX_POINT_CASE:
                break

            list_points = []
            for i in range(size_test_case):
                x, y = input().split(" ")
                x = int(x)
                y = int(y)
                if verify_difference(y):
                    list_points.append((x, y))
                list_points.sort()
            list_entries.append(list_points)

            print(list_entries)
            for wave in list_entries:
                last_x, last_y = None, None
                critical_point = 0
                for i in wave:
                    x, y = i

                    if x == last_x:
                        continue

                    if y == last_y:
                        continue

                    last_x, last_y = x, y
                    critical_point += 1
            print(critical_point)
            test_case += 1
        except EOFError:
            break
    print("\n")


if __name__ == "__main__":
    main()
