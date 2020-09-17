# Collectable Cards
"""
Richard and Vicent are crazy about football collectable cards.
In their spare time, they arrange a way of playing some game involving such cards.
Both also have the habit of exchanging the repeated cards with their friends,
and one day they thought about a different game.
They called all their friends and proposed the following:
with the cards in hand, each one tried to make an exchange with his closest friend following this simple rule:
each one must count how many cards he owned.
After this, they had to split these cards into stacks,
all of it with the same size, as large as it was possible for both players.
Then, each one choose one of the friend's card stacks to receive.
For example, if Richard and Vincent would change the cards with respectively 8 and 12 cards each,
both must put his cards in stacks of four cards (Richard would have two stacks and Vincent had three stacks),
and both choose a stack from his friend to receive it.
Input
The first input line contains a single integer N (1 ≤ N ≤ 3000),
indicating the number of test cases.
Each test case contains two integer numbers
F1 (1 ≤ F1 ≤ 1000) and F2 (1 ≤ F2 ≤ 1000)  indicating, respectly,
the among of collectable cards that Richard and Vicent have to change.

Output
For each test case there will be an integer number at the output,
representing the maximum size of the stack of cards which can be exchanged between two players.

Input Sample
3
8 12
9 27
259 111

Output Sample
4
9
37
"""
# Usando MDC (Maximo Divisor Comum)

'''
# Gasta tempo + 2s
def mdc(f1, f2):
    ret = 1
    value = 2
    while True:
        smallest = min(f1, f2)
        if value > smallest:
            break
        if (f1 % value == 0) and (f2 % value == 0):
            f1 /= value
            f2 /= value
            ret *= value
        else:
            value += 1
    return ret
'''

# mdc, usando recursividade.


def mdc(f1, f2):
    if f2 == 0:
        return f1
    else:
        return mdc(f2, f1 % f2)


def main():
    #try:
    n = int(input())

    #    assert(1 <= n <= 3000)

    for i in range(n):
        values = input().split(" ")
        f1, f2 = values
        f1 = int(f1)
        f2 = int(f2)
        print(mdc(f1, f2))
    #except AssertionError:
    #    pass


if __name__ == "__main__":
    main()
