# prím-e?
# bekérjük az ellenőrizendő számot
szam = int(input("Ellenőrizendő szám = "))
# Az első szám, amivel megpróbáljuk osztani, a kettő
oszto = 2
# addig próbálgatjuk a számot osztogatni egyre növekvő számokkal, amíg meg nem találjuk az első osztóját.  
while szam % oszto != 0:
    print(f"A(z) {oszto} nem osztója a {szam}-nak")
    # vesszük az eggyel nagyobb számot
    oszto += 1
# a ciklusból kilépve megnézzük, hogy a talált osztó kisebb-e, mint maga a szám
if szam == oszto:
    # nem találtunk egyetlen, a számnál kisebb osztót
    print(f"A(z) {szam} prím!")
else:
    # találtunk osztót
    print(f"A(z) {oszto} osztója a {szam}-nak, ezért a(z) {szam} összetett szám!")
    
