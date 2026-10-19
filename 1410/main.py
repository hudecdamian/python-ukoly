ZAKLADNI_CENA = 500

vek = float(input("Zadejte věk návštěvníka: "))
student = input("Je student? (ano/ne): ").strip().lower()
pocet_osob = int(input("Zadejte počet osob: "))

if pocet_osob >= 4:
    typ_slevy = "Skupinová sleva (25 %)"
    sleva = 0.25
elif student == "ano" and vek < 26:
    typ_slevy = "Studentská sleva (30 %)"
    sleva = 0.30
elif vek >= 65:
    typ_slevy = "Seniorská sleva (20 %)"
    sleva = 0.20
else:
    typ_slevy = "Bez slevy"
    sleva = 0

cena_jedne = ZAKLADNI_CENA * (1 - sleva)
cena_celkem = cena_jedne * pocet_osob

print("Typ slevy:", typ_slevy)
print(f"Cena za jednu vstupenku: {cena_jedne:.2f} Kč")
print(f"Celková cena: {cena_celkem:.2f} Kč")
