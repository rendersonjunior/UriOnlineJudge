product = []
total = 0.0
for x in range(2):
  sale_product = input("");

  entry_string = sale_product.split(" ")
  for value in entry_string:
    product.append(float(value))

  id_prod, qtd, value = product
  total = total + (qtd * value)
  product.clear()

print("VALOR A PAGAR: R$ "+str(format(total,'.2f')))
