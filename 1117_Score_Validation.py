# Score Validation
"""
Write a program that reads two scores of a student.
Calculate and print the average of these scores.
Your program must accept just valid scores [0..10].
Each score must be validated separately.
Input
The input file contains many floating-point numbers​​, positive or negative.
The program execution will be finished after the input of two valid scores.

Output
When an invalid score is read, you should print the message "nota invalida".
After the input of two valid scores, the message "media = " must be printed followed by the average of the student.
The average must be printed with 2 numbers after the decimal point.

Input Sample
-3.5
3.5
11.0
10.0

Output Sample
nota invalida
nota invalida
media = 6.75
"""


def main():
    l = []
    while len(l) < 2:
        value = float(input())
        if 0.0 <= value <= 10.0:
            l.append(value)
        else:
            print("nota invalida")

    print("media = %.2f" % float(sum(l)/len(l)))


if __name__ == "__main__":
    main()
