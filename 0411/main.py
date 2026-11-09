print("Program Vaše číslo bude hádat.")
print("Instrukce:")
print("Myslete si číslo od 1 do 100")
print("Odpovídejte:")
print("v - větší")
print("m - menší")
print("s - správně")

dole = 1 
nahore = 100 
pokusy = 0 
odpoved = "" 

print()
while odpoved != "s":
    tip = (dole + nahore) // 2 
    pokusy = pokusy + 1 
    odpoved = input(f"Je Vaše číslo {tip}? (v/m/s): ") 
    if odpoved == "v": 
        dole = tip + 1
    elif odpoved == "m":
        nahore = tip - 1
print(f"Uhodl jsem Vaše číslo {tip} na {pokusy}. pokus.")