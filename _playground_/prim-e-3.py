# prím-e?
# bekérjük az ellenőrizendő számot
szam = int(input("Ellenőrizendő szám = "))
# megnézzük, hogy páros-e (a 2-re azt fogja írni, hogy összetett szám)
oszto = 2
if szam % oszto == 0:
    # találtunk osztót
    print(f"A(z) {oszto} osztója a {szam}-nak, ezért a(z) {szam} összetett szám!")
else:
    # páratlan a szám, csak páratlan számokkal vizsgáljuk az oszthatóságot
    oszto = 3
    # addig próbálgatjuk a számot osztogatni egyre növekvő számokkal, amíg meg nem találjuk az első osztóját, vagy az osztó nagyobb lesz a szám gyökénél.  
    while szam % oszto != 0 and oszto*oszto <= szam:
        print(f"A(z) {oszto} nem osztója a {szam}-nak")
        # vesszük a következő páratlan számot
        oszto += 2
    # a ciklusból kilépve megnézzük, hogy a legutolsó osztó valóban osztója-e a számnak
    if oszto * oszto > szam:
        # nem találtunk egyetlen, a számnál gyökénél nemnagyobb osztót
        print(f"A(z) {szam} prím!")
    else:
        # találtunk osztót
        print(f"A(z) {oszto} osztója a {szam}-nak, ezért a(z) {szam} összetett szám!")
    
