'''Stwórz funkcję do wyznaczania techniką iteracyjną
największy wspólny dzielnik dwóch liczb'''

rows = int(input("wprowadz ile wierszy: "))
col = int(input("wprowadz ile kolumn: "))
tabOgl = []
#liczby = int(input("wprowadz liczbe: "))
for r in range(rows):
    tab2 = []
    for c in range(col):
        tab2.append((r+1)*(c+1))
    tabOgl.append(tab2)
    print()
for i in tabOgl:
    print(i)
