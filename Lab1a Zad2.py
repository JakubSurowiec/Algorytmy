n = int(input("Podaj liczbę n: "))
ile_n = 0

for i in range(n):
    num = int(input(f"Podaj liczbę {i+1}: "))
    if num < 0:
        ile_n += 1

print(f"Ilość liczb ujemnych: {ile_n}")