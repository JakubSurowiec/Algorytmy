# Przykładowa tablica
tablica = [3, 7, 1, 4, 2, 9, 7, -2, 4, 0]

szukana_liczba = int(input("Podaj szukaną liczbę: "))
znaleziona = False
for liczba in tablica:
    if liczba == szukana_liczba:
        print("Podana liczba znajduję się w tablicy")
        znaleziona = True
        break
if not znaleziona:
    print("Podana liczba nie znajduje się w tablicy")