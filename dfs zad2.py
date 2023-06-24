class Graf:
    def __init__(self):
        self.graf = {}

    def dodaj_krawedz(self, start, koniec):
        if start not in self.graf:
            self.graf[start] = []
        self.graf[start].append(koniec)

    def przeszukiwanie_dfs(self, start):
        odwiedzone = set()
        self._przeszukiwanie_dfs_rekurencyjne(start, odwiedzone)

    def _przeszukiwanie_dfs_rekurencyjne(self, wierzcholek, odwiedzone):
        odwiedzone.add(wierzcholek)
        print(wierzcholek)

        if wierzcholek in self.graf:
            for sasiad in self.graf[wierzcholek]:
                if sasiad not in odwiedzone:
                    self._przeszukiwanie_dfs_rekurencyjne(sasiad, odwiedzone)

#przykład
g = Graf()
g.dodaj_krawedz('A', 'B')
g.dodaj_krawedz('A', 'C')
g.dodaj_krawedz('B', 'D')
g.dodaj_krawedz('B', 'E')
g.dodaj_krawedz('C', 'F')


g.przeszukiwanie_dfs('A')