# Type of Fuel
"""
A gas station wants to determine which of their products is the preference of
their customers.
Write a program to read the type of fuel supplied
(coded as follows: 1. Alcohol 2. Gasoline 3. Diesel 4. End).
If you enter an invalid code (outside the range of 1 to 4) a new code must be requested.
The program will end when the inserted code is the number 4.

Input
The input contains only integer and positive values.

Output
It should be written the message: "MUITO OBRIGADO" and the amount of customers
who fueled each fuel type, as an example.

Input Sample
8
1
7
2
2
4

Output Sample
MUITO OBRIGADO
Alcool: 1
Gasolina: 2
Diesel: 0
"""


def main():
    alcohol = 0
    gasoline = 0
    diesel = 0
    while True:
        fuel = int(input())
        if fuel == 1:
            # Alcohol
            alcohol += 1
        elif fuel == 2:
            # Gasoline
            gasoline += 1
        elif fuel == 3:
            # Diesel
            diesel += 1
        elif fuel == 4:
            break
    print("MUITO OBRIGADO")
    print("Alcool: %d" % alcohol)
    print("Gasolina: %d" % gasoline)
    print("Diesel: %d" % diesel)


if __name__ == "__main__":
    main()