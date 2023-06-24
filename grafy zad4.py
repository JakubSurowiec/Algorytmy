def dijkstra(graf, start):
    odleglosci = {wierzcholek: float('inf') for wierzcholek in graf}
    odleglosci[start] = 0
    odwiedzone = set()

    while len(odwiedzone) < len(graf):
        biezacy_wierzcholek = None
        min_odleglosc = float('inf')

        for wierzcholek in graf:
            if odleglosci[wierzcholek] < min_odleglosc and wierzcholek not in odwiedzone:
                biezacy_wierzcholek = wierzcholek
                min_odleglosc = odleglosci[wierzcholek]

        odwiedzone.add(biezacy_wierzcholek)

        for sasiad, waga in graf[biezacy_wierzcholek].items():
            odleglosc = odleglosci[biezacy_wierzcholek] + waga

            if odleglosc < odleglosci[sasiad]:
                odleglosci[sasiad] = odleglosc

    return odleglosci

#przykład
graf = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 6},
    'D': {'B': 1, 'C': 6}
}

odleglosci = dijkstra(graf, 'B')
print(odleglosci)