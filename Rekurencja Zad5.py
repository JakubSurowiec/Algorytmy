def hanoi (ile, skad, dokad, przez):
    if ile>0:
        hanoi(ile-1, skad, przez, dokad)
        print(skad, "---->", dokad)
        hanoi(ile-1, przez, dokad, skad)
hanoi(3, "A" , "B" , "C")
