# Array Hash
import string


def position_alphabet(char):
    try:
        alphabet = list(string.ascii_uppercase)
        # print(alphabet.index(char))
        return alphabet.index(char)
    except:
        return 0

qtd_test_cases = int(input())
list_string = []

assert (1 <= qtd_test_cases <= 100)
for i in range(qtd_test_cases):
    qtd_strings = int(input())
    hashing = 0
    for j in range(qtd_strings):
        word = str(input()).replace(" ","-")
        sum_word = 0
        for k in range(len(word)):
            sum_word = position_alphabet(word[k])
            # print("%d + %d + %d"%(sum_word,j,k))
            hashing += sum_word + j + k
    list_string.append(hashing)

for count in range(qtd_test_cases):
    print(list_string[count])
