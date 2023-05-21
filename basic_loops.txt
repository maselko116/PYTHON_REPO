#ZADANIE 2

for i in range(1,11):
 print("wartość:", i)
i = 0
while i < 10:
    i = i + 1
    print("wartość: ",i)

#ZADANIE 3

def silnia(x):
    wynik = 1
    for i in range(1,x+1):
        wynik=wynik * i
    return wynik
    print(wynik)
print("silnia z podanej cyfry to:",silnia(4))

#ZADANIE 4

for i in range(1,21):
    if i%2==0:
        print(i)

#ZADANIE 5

liczba = 0
while liczba < 30:
    liczba = liczba + 1
    if liczba%3==0:
        print(liczba)

#ZADANIE 6


for i in range(1,31):
    if i%2==0:
        print(i)
        contin

#ZADANIE 7

def alfabet(x):
    litera = 96
    while litera < x:
        litera = litera + 1
        print(chr(litera))

alfabet(ord('s'))

#ZADANIE 8

x = int(input("podaj liczbe: "))
liczba = 0
wynik = 0
while x > liczba:
    liczba = liczba + 1
    wynik = wynik + liczba
print("suma liczb kolejnych do tej to:",wynik)

#ZADANIE 9

def parzyste(x):
    for i in range(0,x+1):
        if i % 2 == 0:
            print(i)
parzyste(10)

#ZADANIE 10

liczba = 101
while liczba >= 0:
    liczba = liczba - 1
    if liczba % 2==0 and liczba % 3 == 0:
        print(liczba)

#ZADANIE 11

liczba = 101
while liczba >= -100:
    liczba = liczba - 1
    if liczba % 2==0:
        if liczba%3 != 0 and liczba%8 != 0:
            print(liczba)
    continue

#ZADANIE 12


x = '0    1    '
y = '1    0    '
for i in range(4):
    for i in range(4):
        print(x,end=" ")
    print('\n')
    for i in range(4):
        print(y,end=" ")
    print('\n')

#ZADANIE 13

print("Oto wyniki mnożenia cyfr z tabliczki mnożenia do 5: ")
for i in range(1,6):
    for a in range(1,10):
        wynik = i * a
        print ("wynik mnożenia: ",i,"*",a,"=",wynik)
    print("\n")    
