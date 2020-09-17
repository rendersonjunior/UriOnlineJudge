# TDA RATIONAL

from fractions import Fraction
import math


def euclides(a, b):
    if a == 0:
        return 1
    else:
        if b > a:
            dividend = b
            divider = a
        else:
            dividend = a
            divider = b
    while dividend % divider != 0:
        c = dividend % divider
        dividend = divider
        divider = c
    return divider


def func_calculate(op, value):
    assert (op in('+', '-', '*', '/') or value in('N', 'D')), "Argumentos inválidos para a função func_calculate!"

    if value == 'N':
        if op == '+':
            return lambda n1, d1, n2, d2: (n1 * d2 + n2 * d1)
        elif op == '-':
            return lambda n1, d1, n2, d2: (n1 * d2 - n2 * d1)
        elif op == '*':
            return lambda n1, d1, n2, d2: (n1 * n2)
        elif op == '/':
            return lambda n1, d1, n2, d2: (n1 * d2)
    elif value == 'D':
        if op == '/':
            return lambda n1, d1, n2, d2: (n2 * d1)
        else:
            return lambda n1, d1, n2, d2: (d1 * d2)
    else:
        pass

qtd_cases_test = int(input())

assert (qtd_cases_test >= 1 and qtd_cases_test <= 1*math.pow(10, 4)), "Intervalo de valores inválido!"

for i in range(qtd_cases_test):
    case_test = input().split(' ')
    N1, s1, D1, OP, N2, s2, D2 = case_test

    try:
        assert (s1 == '/' or s2 == '/'), "A "+str(i+1)+"º expressão não contém números racionais"
        assert ((int(N1) > 0 and int(N2) > 0 and int(D1) > 0 and int(D2) > 0)
            and (int(N1) <= 1000 and int(N2) <= 1000 and int(D1) <= 1000 and int(D2) <= 1000))\
               , "Faixa de valores inválidos na "+str(i+1)+"º expressão"
    except AssertionError:
        break

    func_n = func_calculate(OP,'N')
    func_d = func_calculate(OP,'D')

    num = int(func_n(int(N1), int(D1), int(N2), int(D2)))
    den = int(func_d(int(N1), int(D1), int(N2), int(D2)))

    e = euclides(num,den)

    s_num = num/e
    s_den = den/e

    if s_den < 0:
        s_num *= -1
        s_den *= -1

    print('%d/%d = %d/%d' % (num,den,s_num,s_den))