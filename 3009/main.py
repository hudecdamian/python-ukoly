print ("Kalkulačka spropitného") 
celkem = float(input("Zadejte částku k úhradě: ")) 
procenta_spropitneho = int(input("Zadejte procenta spropitného: ")) 
lidi = int(input("Zadejte počet lidí: ")) 
spropitne = celkem * (procenta_spropitneho / 100) 
celkem_s_propitnym = celkem + spropitne 
castka_na_osobu = celkem_s_propitnym / lidi 
vysledek = round(castka_na_osobu, 2) 
print ("Každý člověk by měl zaplatit: " + str(vysledek) + " Kč")
