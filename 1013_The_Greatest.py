a = int(input())
b = int(input())
c = int(input())

if a > b:
  maior_ab = int((a + c + abs(a - c)) / 2)
else:
  maior_ab = int((b + c + abs(b - c)) / 2)

print(str(maior_ab)+" eh o maior")