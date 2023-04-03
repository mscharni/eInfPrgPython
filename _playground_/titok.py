import random
# betűket tartalmazó lista generálása
def listagen():
    _lista=[]
    # kisbetűk (angol)
    for i in range(97, 123):
        _lista.append(chr(i))
    # nagybetűk (angol)
    for i in range(65, 91):
        _lista.append(chr(i))
    # ékezetes kisbetűk (magyar)
    _lista.extend(["á","é","í","ó","ö","ő","ú","ü","ű"])
    # ékezetes nagybetűk (magyar)
    _lista.extend(["Á","É","Í","Ó","Ö","Ő","Ú","Ü","Ű"])
    # írásjelek
    _lista.extend([" ","!","?",",",".",";"])
    return _lista

# kódoló eljárás
def kodolo(kodolando):
    kodolt=""
    for karakter in kodolando:
        sorszam=abc.index(karakter)
        kodolt=kodolt+cba[sorszam]
    return kodolt

# dekódoló eljárás
def dekodolo(dekodolando):
    dekodolt=""
    for karakter in dekodolando:
        sorszam=cba.index(karakter)
        dekodolt=dekodolt+abc[sorszam]
    return dekodolt

# a szükséges adatok bekérése
mag = int(input("Kódolás magja="))


# lista generálása
abc=listagen()
# a kódoláshoz tartozó, a betűket keverten tartalmazó lista generálása
cba=abc.copy()
random.shuffle(cba, random.seed(mag))

irany = ""
while irany != "V":
    irany = input("Válasszon: (K)ódolás vagy (D)ekódolás vagy (V)ége?").upper()
    if irany == "K":
        szoveg = input("Kódolandó szöveg = ")
        # A bekért szó kódolása
        kodolt_szoveg=kodolo(szoveg)
        print(szoveg + " --> " +kodolt_szoveg)
    elif irany == "D":
        szoveg = input("Dekódolandó szöveg = ")
        # A kódolt szó dekódolása
        dekodolt_szoveg = dekodolo(kodolt_szoveg)
        print(kodolt_szoveg + " --> " +dekodolt_szoveg)
    elif irany != "V":
        print("a 'K', 'D', 'V' betűk közül válasszon!")
