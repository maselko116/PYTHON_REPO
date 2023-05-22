#ZADANIE Z PRAWA DE MORGANA
p = bool(input("wprowadz do p - 0 lub 1: "))
q = bool(input("wprowadz q - 0 lub 1: "))

wynik1 = bool(not(p and q))
wynik2 = bool((not p) or (not q))

print ("Lewa strona równania to: ",wynik1)
print ("Prawa strona równania to: ",wynik2)
if wynik1 == wynik2:
    print("Wyniki równania są takie same")
else:
    print("wyniki równania są równe")