# Triangle

def verify_triangle(a, b, c):
    if abs(b-c) < a < b+c:
        return True
    else:
        return False

def perimeter(a, b, c):
    return a+b+c

def trapezium_area(B,b,h):
    return ((B+b)/2)*h

triangle_values = str(input()).split()

a, b, c = triangle_values

a = float(a)
b = float(b)
c = float(c)

if verify_triangle(a, b, c):
    print("Perimetro = %.1f"%(perimeter(a, b, c)))
else:
    print("Area = %.1f"%(trapezium_area(a, b, c)))

