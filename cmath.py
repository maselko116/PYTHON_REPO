#Zadanie 1
import math
import cmath
def Walec(r, h, pi):
    v = pi*r**2*h
    S = (2*pi*r**2)+2*r*h*pi
    print("objetosc walca wynosi: ", v)
    print("pole powieszchni całkowitej walca wynosi: ", S)

r = int(input("Podaj promień walca: "))
h = int(input("Podaj wysokość walca: "))
pi = math.pi
Walec(r, h, pi)

#ZADANIE 2
import math
import cmath
liczba = int(input("Wprowadz liczbe aby sprawdzic czy jest obfita: "))
dzielniki = 0
for i in range(1,liczba):
    if liczba % i == 0:
        dzielniki = dzielniki + i

if liczba < dzielniki:
    print("liczba jest obfita")
else:
    print("liczba nie jest obfita")

#ZADANIE 3
import math
import cmath
T = float(input("podaj temperature otoczenia w celciuszach: "))
v = float(input("podaj predkosc wiatru: "))
t0 = (13.12) + (0.6215*T)-(11.37*pow(v,0.16))+(0.3965*T*(pow(v,0.16)))
print(round(t0,1))

#ZADANIE 4
import math
import cmath

PI = math.pi
R = 6371 # promień Ziemi w km

def odleglosc(poczatkowa_szerokosc, poczatkowa_dlugosc, koncowa_szerokosc, koncowa_dlugosc):
    dlat = math.radians(koncowa_szerokosc - poczatkowa_szerokosc)
    dlon = math.radians(koncowa_dlugosc - poczatkowa_dlugosc)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(poczatkowa_szerokosc)) * math.cos(math.radians(koncowa_szerokosc)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    odleglosc = R * c

    return odleglosc

poczatkowa_szerokosc = 18.4
poczatkowa_dlugosc = 55.3
koncowa_szerokosc = 24.1
koncowa_dlugosc = 58.7

wynik = odleglosc(poczatkowa_szerokosc, poczatkowa_dlugosc, koncowa_szerokosc, koncowa_dlugosc)
print("Odległość wynosi %.2fkm." % wynik)

#ZADANIE 5
import cmath
import math
print("Podaj pierwszą liczbę zespoloną:")
z1 = complex(input())

print("Podaj drugą liczbę zespoloną:")
z2 = complex(input())


wynik = z1 + z2
print("Wynik dodawania:", wynik)


wynik = z1 - z2
print("Wynik odejmowania:", wynik)

wynik = z1 / z2
print("Wynik odejmowania:", wynik)

wynik = z1 * z2
print("Wynik odejmowania:", wynik)

#ZADANIE 6
import math

def odchylenie_standardowe(lista): 
  srednia = sum(lista)/len(lista) 
  odchylenie = 0
  for liczba in lista: 
    odchylenie += (liczba - srednia)**2 
  odchylenie = odchylenie / len(lista) 
  odchylenie = math.sqrt(odchylenie) 
  return odchylenie
