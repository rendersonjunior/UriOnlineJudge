# Animal

classifications = {"vertebrado": 1,
                   "invertebrado": 2,
                   "ave": 3,
                   "mamifero": 4,
                   "inseto": 5,
                   "anelideo": 6,
                   "carnivoro": 7,
                   "onivoro": 8,
                   "herbivoro": 9,
                   "hematofago": 10
                   }

list_animals = {"137": ["aguia"],
                "138": ["pomba"],
                "148": ["homem"],
                "149": ["vaca"],
                "2510": ["pulga"],
                "259": ["lagarta"],
                "2610": ["sanguessuga"],
                "268": ["minhoca"]
                }


def word_code(word):
    return str(classifications[word])


def function_code(code):
    return str(list_animals[code][0])


def main():
    type_subfilter = str(input()).lower()
    type_class = str(input()).lower()
    type_order = str(input()).lower()

    value_hash = word_code(type_subfilter)+word_code(type_class)+word_code(type_order)
    print(function_code(value_hash))


if __name__ == "__main__":
    main()
