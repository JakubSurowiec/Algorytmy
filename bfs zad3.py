from collections import deque

def bfs(graf, start):
    odwiedzone = set()  # Zbiór odwiedzonych wierzchołków
    kolejka = deque()  # Kolejka do przechowywania wierzchołków do odwiedzenia

    odwiedzone.add(start)
    kolejka.append(start)

    while kolejka:
        wierzcholek = kolejka.popleft()
        print(wierzcholek)  # Możesz tutaj wykonać operację na wierzchołku (np. zapisać do listy)

        # Przejdź przez sąsiadów wierzchołka
        for sasiad in graf[wierzcholek]:
            if sasiad not in odwiedzone:
                odwiedzone.add(sasiad)
                kolejka.append(sasiad)
#przykład
graf = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

startowy_wierzcholek = 'A'

bfs(graf, startowy_wierzcholek)