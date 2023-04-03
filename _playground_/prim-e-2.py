# prím-e?
# bekérjük az ellenőrizendő számot
szam = int(input("Ellenőrizendő szám = "))
# Az első szám, amivel megpróbáljuk osztani, a kettő
oszto = 2
# addig próbálgatjuk a számot osztogatni egyre növekvő számokkal, amíg meg nem találjuk az első osztóját, vagy az osztó nagyobb lesz a szám gyökénél.  
while szam % oszto != 0 and oszto*oszto <= szam:
    print(f"A(z) {oszto} nem osztója a {szam}-nak")
    # vesszük az eggyel nagyobb számot
    oszto += 1
# a ciklusból kilépve megnézzük, hogy a legutolsó osztó valóban osztója-e a számnak
if oszto * oszto > szam:
    # nem találtunk egyetlen, a számnál gyökénél nemnagyobb osztót
    print(f"A(z) {szam} prím!")
else:
    # találtunk osztót
    print(f"A(z) {oszto} osztója a {szam}-nak, ezért a(z) {szam} összetett szám!")
    
