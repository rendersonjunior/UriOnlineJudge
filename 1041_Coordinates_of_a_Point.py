# Coordinates of a Point

value_x_y = input().split(' ')
x, y = value_x_y

x = float(x)
y = float(y)

if x > 0 < y:
    print("Q1")
elif x < 0 < y:
    print("Q2")
elif x < 0 > y:
    print("Q3")
elif x > 0 > y:
    print("Q4")
elif x == 0 == y:
    print("Origem")
elif x != 0 == y:
    print("Eixo X")
elif x == 0 != y:
    print("Eixo Y")
else:
    print("Coordenadas incorretas")