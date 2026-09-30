# **********************
# Kalkulačka spropitného 
# 30. 09. 2026
#***********************

print ("Kalkulačka spropitného") #Titulní text
celkem = float(input("Zadejte částku k úhradě: ")) #Načtení částky k úhradě
procenta_spropitneho = int(input("Zadejte procenta spropitného: ")) #Načtení procenta spropitného
lidi = int(input("Zadejte počet lidí: ")) #Načtení počtu lidí
spropitne = celkem * (procenta_spropitneho / 100) #Výpočet spropitného
celkem_s_propitnym = celkem + spropitne #Výpočet celkové částky spropitným
castka_na_osobu = celkem_s_propitnym / lidi #Výpočet částky na osobu
vysledek = round(castka_na_osobu, 2) #Zaokrouhlení výsledku na 2 desetinná místa
print ("Každý člověk by měl zaplatit: " + str(vysledek) + " Kč") #Výpis výsledku