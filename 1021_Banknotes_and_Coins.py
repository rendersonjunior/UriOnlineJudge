#Banknotes and Coins
def paper_money(cash,value):
    cash_paper = (cash - (cash%value))/value
    return int(cash_paper)

money = round(float(input()),2)

assert(money < 1000000 and money > 0), "Faixa de valores inválido!"

paper_cash = [100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.009]
aux_money = money

for value in paper_cash:
    #Valores
    if value == 1:
        print("MOEDAS:")
    elif value == 100:
        print("NOTAS:")

    if value < 1.1:
       qtd_cash = paper_money(float(aux_money), float(value))
       print(str(round(qtd_cash)) + " moeda(s) de R$ " + str(format(value,'.2f')))
       aux_money -= float(value*qtd_cash)
    else:
       qtd_cash = paper_money(aux_money, value)
       print(str(round(qtd_cash)) + " nota(s) de R$ " + str(format(value,'.2f')))
       aux_money -= float((value*qtd_cash))