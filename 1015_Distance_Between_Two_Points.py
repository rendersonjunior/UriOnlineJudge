import math

#leitura em duas linhas
p1 = input().split(' ')
p2 = input().split(' ')

#atribui valores em variaveis
x1, y1 = p1
x2, y2 = p2

#faz a conversão de tipos
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

distance = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))

print(format(distance,'.4f'))