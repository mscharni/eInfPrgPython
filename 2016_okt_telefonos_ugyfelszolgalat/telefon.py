### Emelt Informatika Érettségi - 2016 Október - Telefonos ügyfélszolgálat

# adatszerkezet
class Hivas:
    sorszam = 0
    kidoS = ""
    vidoS = ""
    kora = 0
    kido = 0
    vido = 0
    hossz = 0
    fogadott: False

# listák
hivasok = []
fogadottak = []

# 1. feladat: Készítse el az mpbe függvényt, amely az óra, perc, másodperc alakban megadott időpont  másodpercben kifejezett értékét adja!
#   A függvényt a megoldásba be kell építenie!
print("\n1. feladat")
def mpbe(o, p, mp):
    return o*60*60 + p*60 + mp
print("Függvény kész.")

# 2. feladat: Olvassa be a hivas.txt állományban talált adatokat, s annak felhasználásával oldja meg a következő feladatokat!
print("\n2. feladat")
with open("hivas.txt", "r") as fileBe:
    i = 1   # ha a sorszámozást 1-től indítjuk (állomány első sora)
    for sor in fileBe:
        sorAdat = sor.strip().split(" ")
        # új hívás objektum létrehozása
        hivas = Hivas()
        hivas.sorszam = i
        hivas.kidoS = sorAdat[0] + " " + sorAdat[1] + " " + sorAdat[2]
        hivas.vidoS = sorAdat[3] + " " + sorAdat[4] + " " + sorAdat[5]
        hivas.kora = int(sorAdat[0])
        hivas.kido = mpbe(int(sorAdat[0]), int(sorAdat[1]), int(sorAdat[2]))
        hivas.vido = mpbe(int(sorAdat[3]), int(sorAdat[4]), int(sorAdat[5]))
        hivas.hossz = hivas.vido-hivas.kido

        # hozzáadás a listához
        hivasok.append(hivas)
        i += 1
print("Adatok beolvasva a 'hivas.txt' állományból.")

# 3. feladat: Készítsen statisztikát, amely megadja, hogy óránként hány hívás futott be!
#   A képernyőn soronként egy óra-darabszám párost jelenítsen meg! Csak azok az órák jelenjenek meg, amelyben volt hívás!
print("\n3. feladat")
# órákon belüli hívások számosságát nyilvántartó, 24 elemű lista, feltöltve nullával
orak = [0]*24
for hivas in hivasok:
    orak[hivas.kora] += 1
for i in range(0, 23):
    if orak[i] != 0:
        print(f"{i} ora {orak[i]} hivas")

# 4. feladat: Írja a képernyőre a leghosszabb hívásnak a sorszámát és másodpercben kifejezett hosszát – attól függetlenül, hogy a hívó tudott-e beszélni az ügyfélszolgálatossal vagy sem!
#   Azonos híváshossz esetén elegendő egyet megjelenítenie.
print("\n4. feladat")
maxHivas = hivasok[0]
for hivas in hivasok:
    if hivas.hossz > maxHivas.hossz:
        maxHivas = hivas
print(f"A leghosszabb ideig vonalban lévő hivó {maxHivas.sorszam}. sorban szerepel, a hivás hossza: {maxHivas.hossz} másodperc.")

# 5. feladat: Olvasson be egy munkaidőn belüli időpontot, majd jelenítse meg a képernyőn, hogy hányadik hívóval beszélt akkor az alkalmazott, és éppen hányan vártak arra, hogy sorra kerüljenek!
#   Ha nem volt hívó, akkor a „Nem volt beszélő.” üzenetet jelenítse meg!
print("\n5. feladat")
idoBeS = input("Adjon meg egy időpontot! (óra perc másodperc):")
idoBe = idoBeS.split(" ")
beIdo = mpbe(int(idoBe[0]), int(idoBe[1]), int(idoBe[2]))
# első fogadott hívás megkeresése
fhi = 0
while hivasok[fhi].vido < beIdo:
    fhi +=1
hivasok[fhi].fogadott = True
# várakozók megszámolása
i = fhi
while hivasok[i].kido < beIdo and beIdo < hivasok[i].vido:
    i += 1
if i == fhi:
    print("Nem volt beszélő.")
else:
    # a várakozók számában maga a vonalban lévő is szerepel, ezért csökkenteni kell eggyel
    varakozok = i - fhi -1
    print(f"A várakozók száma: {varakozok} a beszélő a {hivasok[fhi].sorszam}. hivó.")

# 6. feladat: Írja a képernyőre, annak a hívónak az azonosítóját, akivel a munkatárs utoljára beszélt!
#   Írja ki a várakozás másodpercekben mért hosszát is! (Ha nem kellett várnia, a várakozási idő 0.)
print("\n6. feladat")
efhi = 0            # első fogadott hívás sorszáma
kezdet = 8*60*60    # kezdő időpont
veg = 12*60*60      # záró (vég) időpont
# nap első fogadott hívásának megkeresése
while hivasok[efhi].vido < kezdet:
    efhi +=1
# első fogadott hívás letárolása
fogadottak.append(hivasok[efhi])
fhi = efhi           # fogadott hívás indexe
i = fhi + 1          # első fogadott hívás utáni elemek kezdőindexe
while hivasok[i].kido < veg:
    # ha fogadott hívás, akkor letároljuk
    if hivasok[i].vido > hivasok[fhi].vido:
        fogadottak.append(hivasok[i])
        fhi = i
    i += 1
# utolsó fogadott hívás indexe
ufhi = len(fogadottak) -1
print(f"Az utolso telefonalo adatai a(z) {fogadottak[ufhi].sorszam}. sorban vannak, {fogadottak[ufhi-1].vido - fogadottak[ufhi].kido} masodpercig vart.")

# 7. feladat: Készítse el a sikeres.txt állományt, amely az ügyfélszolgálathoz bekapcsolt hívások listáját tartalmazza!
#   A fájl egyes soraiban a hívó sorszáma, a beszélgetés kezdete (amikor az ügyfélszolgálatos fogadta a hívást) és vége szerepeljen a mintának megfelelő formában!
print("\n7. feladat")
with open("sikeres.txt", "w") as fileKi:
    for fogadott in fogadottak:
        fileKi.write(f"{fogadott.sorszam} {fogadott.kidoS} {fogadott.vidoS}\n")
print("Adatok kiírva a 'sikeres.txt' állományba")
