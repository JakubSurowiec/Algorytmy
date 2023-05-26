cyfry = []
x = int(input("Podoaj liczbę: "))
liczba = x

while x>0:
    cyfry.append(x%2)
    x=x//2
cyfry.reverse()

print("Zapis binarny ", liczba, " to: ", cyfry)