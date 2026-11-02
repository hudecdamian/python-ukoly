import random
tajne_cislo = random.randint(1, 20)
tip = 0

while tip != tajne_cislo:
    tip = int(input("Tipni číslo mezi 1 a 20: "))
    if tip < tajne_cislo:
        print("Příliš nízké!")
    elif tip > tajne_cislo:
        print("Příliš vysoké!")
    else:
        print("Gratulace! Uhodl jsi číslo.")
        break