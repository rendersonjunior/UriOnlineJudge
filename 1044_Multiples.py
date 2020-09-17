# Multiples

check_multiples = input().split(' ')

a, b = check_multiples

a = int(a)
b = int(b)

if a % b == 0 or 0 == b % a:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")