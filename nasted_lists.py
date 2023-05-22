lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
n = int(input("podaj liczbe co ile chcesz zagnieździć litery: "))
pusta_lista = []
for i in range(n):
    pusta_lista.append([])
for i in range(len(lista1)):
    pusta_lista[i % n].append(lista1[i])

print(pusta_lista)
