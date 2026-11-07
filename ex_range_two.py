numar = int(input("Introdu un numar intre 1 si 10: "))

while numar < 1 or numar > 10:
    print("Numarul introdus nu este corect!")
    print('')
    numar = int(input("Introdu un numar intre 1 si 10: "))
print("Bravo! Ai introdus un numar corect.")