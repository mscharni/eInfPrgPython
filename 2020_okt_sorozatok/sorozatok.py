### Emelt Informatika Érettségi - 2020 Október - Sorozatok

import datetime

# struktúra
epizod = {}

# lista
epizodok = []

# feladatokhoz
epizodCount = 0
adasbaCount = 0
lattaCount = 0
lattaSum = 0

# 1. feladat: Olvassa be és tárolja el a lista.txt fájl tartalmát!
print("\n1. feladat")
fileName = 'lista.txt'
with open(fileName, 'r') as fileBe:
    while True:
        # a sor-ban mindig a dátum-adat szerepel string formájában
        sor = fileBe.readline().strip()
        # van még mit beolvasni a file-ból
        if sor:
            if (sor != "NI"):
                datumS = str(sor).split(".")
            else:
                datumS = ["2222","12", "31"]
            cim = str(fileBe.readline().strip())
            resz = str(fileBe.readline().strip())
            hossz = int(fileBe.readline().strip())
            latta = int(fileBe.readline().strip())
            # 2-es-hez
            if(sor != "NI"):
                adasbaCount += 1

            # 3-ashoz és 4-eshez
            if (latta == 1):
                lattaCount += 1
                lattaSum += hossz
            epizod = {
                'datum' : datetime.date(int(datumS[0]),int(datumS[1]),int(datumS[2]),),
                'cim': cim,
                'resz': resz,
                'hossz': hossz,
                'latta': latta
            }
            epizodok.append(epizod)
            epizodCount +=1
        else:
            break
print(f"Adatok beolvasva a '{fileName}' file-ból!")

# 2. feladat: Írassa ki a képernyőre, hogy hány olyan epizód adatait tartalmazza a fájl, amelynek ismert az adásba kerülési dátuma!
print("\n2. feladat")
print(f"A listában {adasbaCount} db vetítési dátummal rendelkező epizód van.")

# 3. feladat: Határozza meg, hogy a fájlban lévő epizódok hány százalékát látta már a listát rögzítő személy!
#   A százalékértéket a minta szerint, két tizedesjeggyel jelenítse meg a képernyőn!
print("\n3. feladat")
print(f"A listában lévő epizódok {lattaCount/epizodCount:.2%}-át látta.")

# 4. feladat: Számítsa ki, hogy összesen mennyi időt töltött a személy az epizódok megnézésével!
#   Az eredményt a minta szerint nap, óra, perc formában adja meg!
print("\n4. feladat")
nap = int(lattaSum / (24*60))
ora = int((lattaSum - nap*24*60) / 60)
perc = lattaSum - nap*24*60 - ora*60
print(f"Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött.")

# 5. feladat: Kérjen be a felhasználótól egy dátumot „éééé.hh.nn” formában! Határozza meg, hogy az adott dátumig megjelent epizódokból melyeket nem látta még!
#   Az aznapi epizódokat is számolja bele!
#   A feltételnek megfelelő epizódok esetén írja a képernyőre tabulátorral elválasztva az évad- és az epizódszámot, valamint a sorozat címét a minta szerint!
print("\n5. feladat")
datumBeS = input("Adjon meg egy dátumot! Dátum = ").strip()
datumBeS = datumBeS.split('.')
datumBe = datetime.date(int(datumBeS[0]),int(datumBeS[1]),int(datumBeS[2]))    
lattaCount = 0
for epizod in epizodok:
    # adott dátum előtti
    if (epizod['datum'] <= datumBe):
        # nem látta
        if (epizod['latta'] == 0):
            print(f"{epizod['resz']}\t{epizod['cim']}")
            lattaCount += 1
if (lattaCount == 0):
    print(f"{datumBe} előtt minden epizódot látott!")

# 6. feladat: Készítse el a megadott algoritmus alapján a hét napját meghatározó függvényt!
#   A függvény neve Hetnapja legyen!
#   A függvény az év, hónap és nap megadása után szöveges eredményként visszaadja, hogy az adott nap a hét melyik napja volt.
#   (Az a és b egész számok maradékos osztása esetén az a div b kifejezés adja meg a hányadost, az a mod b pedig a maradékot, például 17 div 7 = 2 és 17 mod 7 = 3.)
print("\n6. feladat")
def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev = ev - 1
    return napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho-1] + nap) % 7]
print("Függgvény kész.")

# 7. feladat: Kérjen be a felhasználótól egy napot az előző feladatban látható rövidített alakban!
#   A napokat egy (h, k, p, v), kettő (cs), vagy három (sze, szo) karakterrel adja meg!
#   Határozza meg, hogy a fájlban lévő sorozatok közül melyike(ke)t vetítik az adott napon!
#   A sorozatok nevét a minta szerint jelenítse meg a képernyőn!
#   Ha az adott napon egy sorozatot sem adtak adásba, akkor „Az adott napon nem kerül adásba sorozat.” üzenetet jelenítse meg!
print("\n7. feladat")
napBe = input("Adja meg a hét egy napját (például cs)! Nap = ").strip()
adasban = False
lastCim = ""
for epizod in epizodok:
    lastDatum = epizod['datum']
    # ha az adott napra esik
    if (hetnapja(lastDatum.year, lastDatum.month,lastDatum.day) == napBe):
        # és még nem szerepelt
        if (epizod['cim'] != lastCim):
            print(f"{epizod['cim']}")
            adasban = True
            lastCim = epizod['cim']
if (adasban == False):
    print("Az adott napon nem kerül adásba sorozat.")

# 8. feladat: Határozza meg sorozatonként az epizódok összesített vetítési idejét és az epizódok számát!
#   A számításnál vegye figyelembe a vetítési dátummal nem rendelkező epizódokat is!
#   A megoldás során felhasználhatja, hogy egy sorozat epizódjainak adatai egymást követik a forrásállományban.
#   A listát írja ki a summa.txt fájlba!
#   A fájl egy sorában a sorozat címe,az adott sorozatra vonatkozó összesített vetítési idő percben és az epizódok száma szerepeljen szóközzel elválasztva!
print("\n8. feladat")
fileName = 'summa.txt'
with open(fileName, 'w') as fileKi:
    firstEpizod = epizodok[0]
    lastCim = firstEpizod['cim']
    lastSum = 0
    lastCount = 0
    for epizod in epizodok:
        if (epizod['cim'] == lastCim):
            lastSum += epizod['hossz']
            lastCount +=1
        else:
            fileKi.write("{0} {1} {2}\n".format(lastCim, lastSum, lastCount))
            lastCim = epizod['cim']
            lastSum = epizod['hossz']
            lastCount = 1
print(f"Adatok kiírva a '{fileName}' állományba!")
