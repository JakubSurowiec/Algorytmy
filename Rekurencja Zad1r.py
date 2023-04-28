def NWDRek (a,b)
    if a!=b:
        if a>b:
            return NWDRek(a-b,b)
        else:
            return NWDRek (a, b-a)
    return a

