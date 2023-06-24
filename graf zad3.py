class Graf:
    def __init__(self, liczba_wierzcholkow):
        self.liczba_wierzcholkow = liczba_wierzcholkow
        self.macierz_sasiedztwa = [[0] * liczba_wierzcholkow for _ in range(liczba_wierzcholkow)]

    def dodaj_krawedz(self, zrodlo, cel, waga=1):
        if zrodlo < 0 or zrodlo >= self.liczba_wierzcholkow or cel < 0 or cel >= self.liczba_wierzcholkow:
            print("Nieprawidłowe indeksy wierzchołków.")
            return

        self.macierz_sasiedztwa[zrodlo][cel] = waga

    def pobierz_macierz_sasiedztwa(self):
        return self.macierz_sasiedztwa

    def pobierz_liste_sasiedztwa(self):
        lista_sasiedztwa = [[] for _ in range(self.liczba_wierzcholkow)]
        for i in range(self.liczba_wierzcholkow):
            for j in range(self.liczba_wierzcholkow):
                if self.macierz_sasiedztwa[i][j] != 0:
                    lista_sasiedztwa[i].append((j, self.macierz_sasiedztwa[i][j]))
        return lista_sasiedztwa

    def wyswietl_graf(self):
        print("Macierz sąsiedztwa:")
        for wiersz in self.macierz_sasiedztwa:
            print(wiersz)
        print("\nLista sąsiedztwa:")
        lista_sasiedztwa = self.pobierz_liste_sasiedztwa()
        for wierzcholek, sasiedzi in enumerate(lista_sasiedztwa):
            print(f"{wierzcholek}: {sasiedzi}")
        print("\nInterpretacja graficzna:")
        for i in range(self.liczba_wierzcholkow):
            for j in range(self.liczba_wierzcholkow):
                if self.macierz_sasiedztwa[i][j] != 0:
                    print(f"{i} --({self.macierz_sasiedztwa[i][j]})--> {j}")


def buduj_graf():
    print("Witaj! Ten program pozwala na budowanie grafu.")
    typ_grafu = input("Podaj typ grafu (skierowany/nieskierowany): ")
    liczba_wierzcholkow = int(input("Podaj liczbę wierzchołków: "))

    graf = Graf(liczba_wierzcholkow)

    liczba_krawedzi = int(input("Podaj liczbę połączeń: "))

    print("Podaj połączenia w formacie: wierzchołek źródłowy, wierzchołek docelowy, waga (opcjonalnie)")
    for _ in range(liczba_krawedzi):
        informacje_o_krawedzi = input("Podaj połączenie: ").split(",")
        zrodlo = int(informacje_o_krawedzi[0])
        cel = int(informacje_o_krawedzi[1])
        if len(informacje_o_krawedzi) == 3:
            waga = int(informacje_o_krawedzi[2])
            graf.dodaj_krawedz(zrodlo, cel, waga)
        else:
            graf.dodaj_krawedz(zrodlo, cel)

    print("\nGraf został zdefiniowany:")
    graf.wyswietl_graf()


buduj_graf()