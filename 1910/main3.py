a = int(input("Zadejte první číslo: "))
b = int(input("Zadejte druhé číslo: "))
c = int(input("Zadejte třetí číslo: "))

if a > b:
    x = a
    a = b
    b = x
if b > c:
    x = b
    b = c
    c = x
if a > b:
    x = a
    a = b
    b = x

print (f"{a} , {b} , {c}")
