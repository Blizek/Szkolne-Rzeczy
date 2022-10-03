import random


# def sorotwanie_bombelkowe(lista):
#     for i in range(len(lista) - 1, 0, -1):
#       for j in range(i):
#         if lista[j] > lista[j + 1]:
#           tymczasowa = lista[j]
#           lista[j] = lista[j + 1]
#           lista[j + 1] = tymczasowa
#
#     return lista

# def sortowanie_wstawianie(lista):
#     for i in range(1, len(lista) - 1):
#         for j in range(i, -1, -1):
#             if lista[j] > lista[j + 1]:
#                 tymczasowa = lista[j]
#                 lista[j] = lista[j + 1]
#                 lista[j + 1] = tymczasowa
#
#     return lista

# def sortowanie_wybieranie(lista):
#     for i in range(1, len(lista) - 1):
#         aktualna = lista[i - 1]
#         najmniejsza = aktualna
#         indeks_najmniejszej = i - 1
#         for j in range(i, len(lista)):
#             if lista[j] < najmniejsza:
#                 najmniejsza = lista[j]
#                 indeks_najmniejszej = j
#         lista[i - 1] = najmniejsza
#         lista[indeks_najmniejszej] = aktualna
#
#     return lista

def quicksort(p, k):
    if p < k:
        m = p
        for i in range(p + 1, k + 1):
            if lista_liczb[i] < lista_liczb[p]:
                pom = lista_liczb[i]
                lista_liczb[i] = lista_liczb[p]
                lista_liczb[p] = pom
        pom = lista_liczb[p]
        lista_liczb[p] = lista_liczb[m]
        lista_liczb[m] = pom
        quicksort(p, m - 1)
        quicksort(m + 1, k)


lista_liczb = []

while len(lista_liczb) < 150:
    losowa_liczba = random.randint(1, 1000)
    if losowa_liczba not in lista_liczb:
      lista_liczb.append(losowa_liczba)

# posortowane = sorotwanie_bombelkowe(lista_liczb)
# posortowane = sortowanie_wstawianie(lista_liczb)
quicksort(0, len(lista_liczb) - 1)

f = open("wyniki1_sorotwanie_liczb.txt", "w+")

# odp1 = "\n".join(str(liczba) for liczba in posortowane)
odp1 = "\n".join(str(liczba) for liczba in lista_liczb)

f.write(odp1)
f.close()

nowa_liczba = int(input("Nowa liczba: "))
lista_liczb.append(nowa_liczba)

# # posortowane2 = sorotwanie_bombelkowe(lista_liczb)
# # posortowane2 = sortowanie_wstawianie(lista_liczb)
# posortowane2 = sortowanie_wybieranie(lista_liczb)
quicksort(0, len(lista_liczb) - 1)

g = open("wyniki2_sortowanie_liczb.txt", "w+")

# odp2 = "\n".join(str(liczba) for liczba in posortowane2)
odp2 = "\n".join(str(liczba) for liczba in lista_liczb)

g.write(odp2)
g.close()


