# Bhaskara's Formula
import math


def return_delta(a, b, c):
    return round(float(math.pow(b, 2)-4*a*c),5)


def bhaskara_formula(a, b, delta, root):
    assert (root in('x1','x2')),"Valor inválido para root"
    if root == 'x1':
        x1 = ((-1*b) + math.sqrt(delta))/(2*a)
        return x1
    else:
        x2 = ((-1*b) - math.sqrt(delta))/(2*a)
        return x2


values = input().split(' ')

a, b, c = values

a = float(a)
b = float(b)
c = float(c)

try:
    delta = return_delta(a, b, c)
    x1 = bhaskara_formula(a,b,delta,'x1')
    x2 = bhaskara_formula(a,b,delta,'x2')

    print("R1 = %.5f" % x1)
    print("R2 = %.5f" % x2)
except ZeroDivisionError:
    print("Impossivel calcular")
except ValueError:
    print("Impossivel calcular")
