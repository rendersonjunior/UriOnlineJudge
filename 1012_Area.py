def trunc(num, digits):
   sp = str(num).split('.')
   return '.'.join([sp[0], sp[:digits]])

string_number = input()
values = []

entry_string = string_number.split(" ")
for value in entry_string:
    values.append(float(trunc(value,1)))

a, b, c = values
#a = float("{0:.1f}".format(a)) #round(a,1)
#b = float("{0:.1f}".format(b)) #round(b,1)
#c = float("{0:.1f}".format(c)) #round(c,1)

print(a)
print(b)
print(c)

pi = 3.14159
rectangle_triangle = (1/2) * a * c
circle_area = pi * pow(c,2)
trapezium_area = ((1/2)*(a+b)) * c
square_area = pow(b,2)
rectangle = a*b

print("TRIANGULO: "+str(format(rectangle_triangle,'.3f')))
print("CIRCULO: "+str(format(circle_area,'.3f')))
print("TRAPEZIO: "+str(format(trapezium_area,'.3f')))
print("QUADRADO: "+str(format(square_area,'.3f')))
print("RETANGULO: "+str(format(rectangle,'.3f')))
