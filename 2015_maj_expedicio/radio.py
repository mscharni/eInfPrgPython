class Vetel:
    nap = 0         # vétel napja
    vevo = 0        # vevő kódja
    szoveg = ""     # üzenet szövege

class Uzenet:
    nap = 0         # vétel napja
    szovegek = []   # adott napi üzenetek szövege
    hszoveg = ""    # helyreállított üzenet szövege


vetelek = []    # beérkező vételek

# 1. feladat: Olvassa be és tárolja a veetel.txt fájl tartalmát!
print("\n1. feladat:")
with open("veetel.txt", "r") as fileBe:
    for sor in fileBe:
        vetel = Vetel()
        # páratlan sor
        adatSor = sor.strip().split(" ")
        vetel.nap = int(adatSor[0])
        vetel.vevo = int(adatSor[1])
        # páros sor
        vetel.szoveg = fileBe.readline().strip()

        vetelek.append(vetel)
print("Adatok beolvasva a 'veetel.txt' állományból.")

# 2. feladat: Írja a képernyőre, hogy melyik rádióamatőr rögzítette az állományban szereplő első és melyik az utolsó üzenetet!
print("\n2. feladat:")
print(f"Az első üzenet rögzítője: {vetelek[0].vevo}")
print(f"Az utolsó üzenet rögzítője: {vetelek[-1].vevo}")

# 3. feladat: Adja meg az összes olyan feljegyzés napját és a rádióamatőr sorszámát, amelynek szövegében a „farkas” karaktersorozat szerepel!
print("\n3. feladat:")
for vetel in vetelek:
    if "farkas" in vetel.szoveg:
        print(f"{vetel.nap}. nap {vetel.vevo}. rádióamatőr")

# 4. feladat: Készítsen statisztikát, amely megadja, hogy melyik napon hány rádióamatőr készített feljegyzést.
#   Azok a napok 0 értékkel szerepeljenek, amikor nem született feljegyzés!
#   Az eredmény a képernyőn jelenjen meg a napok sorszáma szerint növekvően!
#   A megjelenítést a feladat végén látható minta szerint alakítsa ki!
print("\n4. feladat:")
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
    print(f"{uzenet.nap}. nap: {len(uzenet.szovegek)} rádióamatőr")


# 5. feladat: A rögzített üzenetek alapján kísérelje meg helyreállítani az expedíció által küldött üzenetet!
#   Készítse el az adaas.txt fájlt, amely napok szerinti sorrendben tartalmazza a küldött üzeneteket!
#   Ha egy időpontban senkinél nem volt vétel, akkor azon a ponton a # jel szerepeljen!
print("\n5. feladat:")
with open("adaas.txt", "w") as fileKi:
    for uzenet in uzenetek:
        hszoveg = list(uzenet.szovegek[0])
        for szoveg in uzenet.szovegek:
            for i in range(0,89):
                if szoveg[i] != "#":
                    hszoveg[i] = szoveg[i]

        uzenet.hszoveg = "".join(hszoveg)
        fileKi.writelines(uzenet.hszoveg)
        fileKi.writelines("\n")
print("Adatok kiírva a 'adaas.txt' állományba")

# 6. feladat: Készítsen függvényt szame néven az alábbi algoritmus alapján!
#   A függvény egy karaktersorozathoz hozzárendeli az igaz vagy a hamis értéket.
#   A függvény elkészítésekor az algoritmusban megadott változóneveket használja!
print("\n6. feladat:")
def szame(szo):
    valasz = True
    for i in range(0,len(szo)):
        if szo[i] < '0' or szo[i]>'9':
            valasz = False
    return valasz

# 7. feladat: Olvassa be egy nap és egy rádióamatőr sorszámát, majd írja a képernyőre a megfigyelt egyedek számát (a kifejlett és kölyök egyedek számának összegét)!
#   Ha nem volt ilyen feljegyzés, a „Nincs ilyen feljegyzés” szöveget jelenítse meg!
#   Ha nem volt megfigyelt  egyed vagy számuk nem állapítható meg, a „Nincs információ” szöveget jelenítse meg!
#   Amennyiben egy számot közvetlenül # jel követ, akkor a számot tekintse nem megállapíthatónak!
print("\n7. feladat:")
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
        print(f"A megfigyelt egyedek száma: {felnott + kolyok}")
    else:
        # minden más esetben nem értelmezhető
        print("Nincs információ")
else:
    print("Nincs ilyen feljegyzés")

