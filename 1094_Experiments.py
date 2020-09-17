# Experiments
'''
Maria has just started as graduate student in a medical school and she's needing your help to organize a laboratory
experiment which she is responsible about. She wants to know, at the end of the year, how many animals were used in this
laboratory and the percentage of each type of animal is used at all.

This laboratory uses in particular three types of animals: frogs, rats and rabbits.
To obtain this information, it knows exactly the number of experiments that were performed,
the type and quantity of each animal is used in each experiment.

Input

The first line of input contains an integer N indicating the number of test cases that follows.
Each test case contains an integer Amount (1 ≤ Amount ≤ 15) which represents the amount of animal used and
a character Type ('C', 'R' or 'S'), indicating the type of animal:

- C: Coelho (rabbit in portuguese)
- R: Rato (rat  in portuguese)
- S: Sapo (frog in portuguese)

Output

Print the total of animals used,
the total of each type of animal and the percentual of each one in relation of the total of animals used.
The percentual must be printed with 2 digits after the decimal point.
'''


def calculate_avg(total_value, prop_value):
    return format((100*prop_value)/total_value, '.2f')


def main():
    experiments = {'C': 0,
                   'R': 0,
                   'S': 0}
    n = int(input())
    total_animals = 0
    for i in range(1, n+1):
        info = input().split(' ')
        experiments[info[1]] += int(info[0])
        total_animals += int(info[0])

    print("Total: %d cobaias" % total_animals)
    print("Total de coelhos: %d" % experiments['C'])
    print("Total de ratos: %d" % experiments['R'])
    print("Total de sapos: %d" % experiments['S'])
    print('Percentual de coelhos: {0} %'.format(calculate_avg(total_animals, experiments['C'])))
    print('Percentual de ratos: {0} %'.format(calculate_avg(total_animals, experiments['R'])))
    print('Percentual de sapos: {0} %'.format(calculate_avg(total_animals, experiments['S'])))


if __name__ == "__main__":
    main()
