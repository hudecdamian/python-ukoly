bodx = (1, 2, 3, 4)
body = (5, 6, 7, 8)

cislox = float(input("Zadejte x souřadnici bodu: "))
cisloy = float(input("Zadejte y souřadnici bodu: "))

if cislox < bodx[0] or cislox > bodx[1] or cisloy < body[0] or cisloy > body[1]:
    print("Bod se nachází mimo obdélník.")
elif cislox == bodx[0] or cislox == bodx[1] or cisloy == body[0] or cisloy == body[1]:
    print("Bod se nachází na hranici obdélníku.")
else:
    print("Bod se nachází uvnitř obdélníku.")
