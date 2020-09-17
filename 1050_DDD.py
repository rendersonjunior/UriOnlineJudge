# DDD


def main():

    ddd = {61: "Brasilia",
           71: "Salvador",
           11: "Sao Paulo",
           21: "Rio de Janeiro",
           32: "Juiz de Fora",
           19: "Campinas",
           27: "Vitoria",
           31: "Belo Horizonte"}

    number_ddd = int(input())
    city_ddd = str(ddd.get(number_ddd, "DDD nao cadastrado"))
    city_ddd.encode('utf-8')
    print(city_ddd)

if __name__ == "__main__":
    main()
