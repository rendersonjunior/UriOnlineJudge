a = round(float(input()),1)
b = round(float(input()),1)
c = round(float(input()),1)

if a < 0:
    a = 0
if b < 0:
    b = 0
if c < 0:
    c = 0

if a > 10:
    a = 10
if b > 10:
    b = 10
if c > 10:
    c = 10

media = (a*2+b*3+c*5)/10

print("MEDIA = "+str(format(media,'.1f')))