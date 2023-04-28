tab = [5, 2, 7, 16, 8]

def odwrocona(tab, start, end):
    if start >= end:
        return

    tab[start], tab[end] = tab[end], tab[start]
    odwrocona(tab, start + 1, end - 1)

odwrocona(tab,0, len(tab) - 1)
print(tab)