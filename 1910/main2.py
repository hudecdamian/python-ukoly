a = int(input("Zadejte první číslo: "))
b = int(input("Zadejte druhé číslo: "))
c = int(input("Zadejte třetí číslo: "))

min = a
max = a
if b < min:
    min = b
else:
    if c < min:
        min = c
    if b > max:
        max = b
    if c > max:
         max = c
print (f"Nejmenší číslo je: {min} Největší číslo je: {max}")
