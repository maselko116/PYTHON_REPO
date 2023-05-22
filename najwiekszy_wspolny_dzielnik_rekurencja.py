
#NAJWIEKSZY WSPÓLNY DZIELNIK DWÓCH LICZB CAŁKOWITYCH

x = int(input("Wprowaź pierwszą liczbę całkowitą: "))
y = int(input("Wprowaź drugą liczbę całkowitą: "))

#4,6
def najwiekszyDzielnik(x,y):
    dzielnik = 1
    if x < y:
        dzielnik = x
        while y % dzielnik == 0:
            dzielnik = dzielnik - 1
            print(dzielnik)
    elif x > y:
        while x % dzielnik == 0 and y % dzielnik == 0:
            if x % dzielnik == 0 and y % dzielnik == 0:
                return dzielnik - 1
        print(dzielnik)
    else:
        dzielnik = x
        print(dzielnik)

najwiekszyDzielnik(x,y)