def vypocet_obsahu(a, b):
    if a < 0 or b < 0:
        return None
    obsah = a * b
    return obsah

print("Výpočet výměry bytu")
print()

pocet_mistnosti = int(input("Zadejte počet místností: "))
mistnost = 1
obsah = 0
obsah_mistnosti = 0
while mistnost <= pocet_mistnosti:
    print(f"Zadej rozměry {mistnost}. místnosti:")
    strana_a = float(input("Zadejte délku (v metrech): "))
    strana_b = float(input("Zadejte šířku (v metrech): "))
    obsah_mistnosti += vypocet_obsahu(strana_a, strana_b)
    if obsah_mistnosti != None:
        obsah += obsah_mistnosti
        mistnost += 1
print(f"Celková výměra bytu je: {obsah} m²")


