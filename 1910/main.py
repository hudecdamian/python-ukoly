cislo1 = int(input("Zadejte první číslo: "))
cislo2 = int(input("Zadejte druhé číslo: "))
cislo3 = int(input("Zadejte třetí číslo: "))

if cislo1 > cislo2 and cislo1 > cislo3:
    print("Největší číslo je:", cislo1)
elif cislo2 > cislo1 and cislo2 > cislo3:
    print("Největší číslo je:", cislo2)
elif cislo3 > cislo1 and cislo3 > cislo2:
    print("Největší číslo je:", cislo3)

if cislo1 > cislo2 and cislo1 < cislo3:
    print("Prostřední číslo je:", cislo1)
elif cislo2 > cislo1 and cislo2 < cislo3:
    print("Prostřední číslo je:", cislo2)
elif cislo3 > cislo1 and cislo3 < cislo2:
    print("Prostřední číslo je:", cislo3)

if cislo1 < cislo2 and cislo1 < cislo3:
    print("Nejmenší číslo je:", cislo1)
elif cislo2 < cislo1 and cislo2 < cislo3:
    print("Nejmenší číslo je:", cislo2)
elif cislo3 < cislo1 and cislo3 < cislo2:
    print("Nejmenší číslo je:", cislo3)
