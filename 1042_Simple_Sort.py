# Simple Sort


list_sort = input().split(' ')
a, b, c = list_sort
list_sort = [int(a), int(b), int(c)]

'''
for i in list_sort:
    for j in list_sort:
        if i < j:
            aux = list_sort[list_sort.index(i)]
            list_sort[list_sort.index(i)] = list_sort[list_sort.index(j)]
            list_sort[list_sort.index(j)] = aux
'''

list_sort.sort()

print(list_sort[0])
print(list_sort[1])
print(list_sort[2])
print('')
print(a)
print(b)
print(c)