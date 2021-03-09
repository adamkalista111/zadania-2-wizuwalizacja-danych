import math
#1

def zad1(sporty):
    print(sporty)
    sporty.reverse()
    print(sporty)
    sporty.append('hokej')
    sporty.append('tenis stołowy')
    sporty.append('tenis ziemny')
    return sporty

# print(zad1(['rugby', 'pilka nozna', 'koszykowka']))

#2

skroty = {
    'pt': 'Piątek',
    'czw': 'Czwartek',
    'sr': 'Środa',
    'wt': 'Wtorek',
    'pn': 'Poniedziałek',
    'sb': 'Sobota',
    'nd': 'Niedziela'
}

#3

ulubioneGry = {
    'lol': 'League of Legends',
    'cs:go': 'Counter Strike Global Offensive',
    'wow': 'World Of Warcraft',
    'poe': 'Path of Exile'
}
# print(len(ulubioneGry))

#4

def zad4(zdanie):
    ileA = 0
    for i in zdanie:
        if i == 'a':
            ileA += 1
    return ileA

# print(zad4(input('Podaj zdanie: ')))

#5

def zad5(a, b, c):
    return a**b + c

cyfry = open('zad5.txt', 'r')
zczytaneCyfry = cyfry.readlines()

# print(zad5(int(zczytaneCyfry[0]), int(zczytaneCyfry[1]), int(zczytaneCyfry[2])))

#6

def zad6(a, b, c):
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    return largest

# print(zad6(6,1,8))

# 7

def zad7(liczby):
    podniesione = []
    for i in liczby:
        podniesione.append(i**2)
    return podniesione

# print(zad7([1,7,1,7,19,19,14.4,14.1,4.20]))

#8

def zad8():
    parzyste = []
    i = 10
    while i > 0:
        wczytanaLiczba = int(input('Podaj liczbę: '))
        if wczytanaLiczba % 2 == 0:
            parzyste.append(wczytanaLiczba)
        i -= 1
    return parzyste

# print(zad8())


#9
# lista = [1, 2, 3, 4, 5]
# for liczba in lista:
#     a = int(liczba)%2
#     if a == 0:
#         print("E")
#     else:
#         print("EEEEEE")

#10

def zad10(liczba):
    if liczba < 0:
        return 'błąd'
    else:
        pierwiastek = math.sqrt(liczba)
        return pierwiastek

print(zad10(4))
