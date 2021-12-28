class Vetel:
    nap = 0         # vétel napja
    vevo = 0        # vevő kódja
    szoveg = ""     # üzenet szövege

class Uzenet:
    nap = 0         # vétel napja
    szovegek = []   # adott napi üzenetek szövege
    hszoveg = ""    # helyreállított üzenet szövege


vetelek = []    # beérkező vételek

# 1. feladat
fileBe = open("veetel.txt", "r")
for sor in fileBe:
    vetel = Vetel()
    # páratlan sor
    adatSor = sor.strip().split(" ")
    vetel.nap = int(adatSor[0])
    vetel.vevo = int(adatSor[1])
    # páros sor
    vetel.szoveg = fileBe.readline().strip()

    vetelek.append(vetel)
fileBe.close()

# 2. feladat
print("2. feladat:")
print("Az első üzenet rögzítője: {}".format(vetelek[0].vevo))
print("Az utolsó üzenet rögzítője: {}".format(vetelek[-1].vevo))

# 3. feladat:
print("3. feladat:")
for vetel in vetelek:
    if "farkas" in vetel.szoveg:
        print("{}. nap {}. rádióamatőr".format(vetel.nap, vetel.vevo))

# 4. feladat:
print("4. feladat:")
uzenetek = []    # 11 elemű, minden napra egy uzenet
for i in range(1,12):
    uzenet = Uzenet()
    uzenet.nap = i
    uzenet.szovegek = []
    uzenet.hszoveg = ""
    uzenetek.append(uzenet)

# minden vetel szövegét hozzáadjuk a megfelelő nap-indexű uzenet szovegek listájához
for vetel in vetelek:
    uzenetek[vetel.nap-1].szovegek.append(vetel.szoveg)

for uzenet in uzenetek:
    print("{}. nap: {} rádióamatőr".format(uzenet.nap, len(uzenet.szovegek)))


# 5. feladat:
print("5. feladat:")
fileKi = open("adaas.txt", "w")
for uzenet in uzenetek:
    hszoveg = list(uzenet.szovegek[0])
    for szoveg in uzenet.szovegek:
        for i in range(0,89):
            if szoveg[i] != "#":
                hszoveg[i] = szoveg[i]
    
    uzenet.hszoveg = "".join(hszoveg)
    fileKi.writelines(uzenet.hszoveg)
    fileKi.writelines("\n")
fileKi.flush()
fileKi.close()

# 6. feladat:
print("6. feladat:")
def szame(szo):
    valasz = True
    for i in range(0,len(szo)):
        if szo[i] < '0' or szo[i]>'9':
            valasz = False
    return valasz

# 7. feladat:
print("7. feladat:")
napS = int(input("Adja meg a nap sorszámát! "))
vevoS = int(input("Adja meg a rádióamatőr sorszámát! "))
# adott vétel megkeresése
felnottE = False
kolyokE = False
_vetel = None
for vetel in vetelek:
    if vetel.nap == napS and vetel.vevo == vevoS:
        _vetel = vetel
        exit
if _vetel != None:
    _szoveg = _vetel.szoveg
    # felnőtt rész: '/' előtti rész
    _sepI = _szoveg.find("/")
    if _sepI != -1:
        felnottS = _szoveg[0:_sepI]
        # a talált szövegrész szám-e?
        if szame(felnottS):
            felnott = int(felnottS)
            felnottE = True
        # kölyök rész: '/' utáni és ' ' előtti rész
        _sepII = _szoveg.find(" ",_sepI)
        if _sepII != -1:
            kolyokS = _szoveg[_sepI+1:_sepII]
            # a talált szövegrész szám-e?
            if szame(kolyokS):
                kolyok = int(kolyokS)
                kolyokE = True
    # csak akkor számolunk, ha van felnőtt és kölyök is
    if felnottE and kolyokE:
        print("A megfigyelt egyedek száma: {}".format(felnott + kolyok))
    else:
        # minden más esetben nem értelmezhető
        print("Nincs információ")
else:
    print("Nincs ilyen feljegyzés")

