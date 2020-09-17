# Snack

list_item = [(1, "Cachorro Quente", 4.00),
             (2, "X-Salada", 4.50),
             (3, "X-Bacon", 5.00),
             (4, "Torrada Simples", 2.00),
             (5, "Refrigerante", 1.50)]

desc_item = input().split(' ')

item ,qtd_consumed = desc_item

item = int(item)
qtd_consumed = int(qtd_consumed)

bill = list_item[item-1][2] * qtd_consumed
print("Total: R$ %.2f" % (bill))