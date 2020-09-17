# Interval

intervals = [(0,25),(25,50),(50,75),(75,100)]
value = float(input())

try:
    assert (value >= 0 and value <= 100)
    for x,y in intervals:
        if value >= 0 and value <= 25:
            print('Intervalo [%d,%d]' % (int(x), int(y)))
            break
        else:
            if value >= x and value <= y:
                print('Intervalo (%d,%d]' % (int(x), int(y)))
                break
except AssertionError:
    print("Fora de intervalo")