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

# átalakító eljárás
def konvertalo(szoveg, irany):
    if irany == "K":
        honnan = abc
        hova = cba
    else:
        honnan = cba
        hova = abc
    konvertalt=""
    for karakter in szoveg:
        sorszam=honnan.index(karakter)
        konvertalt += hova[sorszam]
    return konvertalt


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
    if irany == "K" or irany =="D":
        szoveg = input("Konvertálandó szöveg = ")
        # A bekért szó átalakítása
        konvertalt_szoveg=konvertalo(szoveg, irany)
        print(szoveg + " --> " +konvertalt_szoveg)
    elif irany != "V":
        print("a 'K', 'D', 'V' betűk közül válasszon!")
