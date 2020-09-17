# Triangle Types
import math


triangle_sides = input().split(' ')

for x in range(3):
    triangle_sides[x] = float(triangle_sides[x])
triangle_sides.sort(reverse=True)
a, b, c = triangle_sides

a2, b2, c2 = math.pow(a,2), math.pow(b,2), math.pow(c,2)

if a >= (b+c):
    print("NAO FORMA TRIANGULO")
else:
    if a2 == (b2+c2):
        print("TRIANGULO RETANGULO")
    if a2 > (b2+c2):
        print("TRIANGULO OBTUSANGULO")
    if a2 < (b2+c2):
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if (a == b != c) or (b == c != a) or (c == a != b):
        print("TRIANGULO ISOSCELES")