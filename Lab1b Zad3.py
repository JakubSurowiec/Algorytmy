tablica = [1, 2, 3, 11, 21, 111, 231]

n = len(tablica)
for i in range(n):
    for j in range(i+1, n):
        if str(tablica[i]) > str(tablica[j]):
            tablica[i], tablica[j] = tablica[j], tablica[i]
print(tablica)