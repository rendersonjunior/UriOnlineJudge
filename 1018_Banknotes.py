def paper_money(cash,value):
    cash_paper = (cash - (cash%value))/value
    return cash_paper

def left_money(cash,pick):
    return (cash - (cash%value))%pick

money = int(input())

assert(money < 1000000 and money > 0), "Faixa de valores inválido!"

paper_cash = [100,50,20,10,5,2,1]
aux_money = money

print(money)
for value in paper_cash:
    # Value
    if left_money(aux_money,value) == 0:
        qtd_cash = paper_money(aux_money, value)
        print(str(round(qtd_cash))+" nota(s) de R$ "+str(value)+",00")
        aux_money -= value * qtd_cash
    else:
        print("0 nota(s) de R$ " + str(value)+",00")