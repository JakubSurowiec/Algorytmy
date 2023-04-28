# Przykładowa tablica
tablica = [3, 7, 1, 4, 2, 9, 3, -2, 5, 0]

min_wartosc = tablica[0]
for i in range(1, len(tablica)):
    if tablica[i] < min_wartosc:
        min_wartosc = tablica[i]
print("Minimalna wartość w tablicy to:", min_wartosc)