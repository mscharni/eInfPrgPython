### Emelt Informatika Érettségi - 2020 Október - Sorozatok
# egy szótárban helyezzük el az összetartozó adatokat, amit egy listában gyűjtünk

# 1. feladat: Olvassa be és tárolja el a lista.txt fájl tartalmát!
print("\n1. feladat")
adatok = []
# egyből a beolvasás során is elő lehetne állítani a szótárakat, de most marad így az egyszerűség kedvéért
with open('lista.txt', 'r', encoding='utf-8') as file:
    elemek = file.readlines()

for i in range(0, len(elemek), 5):
    # egy szótár előállítása 5 összetartozó adatból
    adat = {
        "datum" : elemek[i].strip(),           # dátum
        "cim"   : elemek[i+1].strip(),         # cím
        "epizod": elemek[i+2].strip(),         # epizód
        "perc"  : int(elemek[i+3].strip()),    # perc
        "latta" : int(elemek[i+4].strip())     # látta
    }
    # összes sorozat adatait tartalmazó listába fűzés
    adatok.append(adat)
print(f"Adatok beolvasva a 'lista.txt' file-ból!")

# 2. feladat: Írassa ki a képernyőre, hogy hány olyan epizód adatait tartalmazza a fájl, amelynek ismert az adásba kerülési dátuma!
print("\n2. feladat")
NI = 0
for adat in adatok:
    if adat['datum'] == 'NI':
        NI += 1
ossz_ep = len(adatok)
print(f"A listában {ossz_ep-NI} db vetítési dátummal rendelkező epizód van.")


# 3. feladat: Határozza meg, hogy a fájlban lévő epizódok hány százalékát látta már a listát rögzítő személy!
#   A százalékértéket a minta szerint, két tizedesjeggyel jelenítse meg a képernyőn!
print("\n3. feladat")
latta = 0
for adat in adatok:
    latta += adat['latta']
print(f"A listában lévő epizódok {latta/ossz_ep:.2%} -át látta.")


# 4. feladat: Számítsa ki, hogy összesen mennyi időt töltött a személy az epizódok megnézésével!
#   Az eredményt a minta szerint nap, óra, perc formában adja meg!
print("\n4. feladat")
osszperc = 0
for adat in adatok:
    if adat['latta'] == 1:
        osszperc += adat['perc']
nap = osszperc // (24*60)
ora = (osszperc - nap*24*60) // 60
perc = osszperc - nap*24*60 - ora*60
print(f"Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött.")


# 5. feladat: Kérjen be a felhasználótól egy dátumot „éééé.hh.nn” formában! Határozza meg, hogy az adott dátumig megjelent epizódokból melyeket nem látta még!
#   Az aznapi epizódokat is számolja bele!
#   A feltételnek megfelelő epizódok esetén írja a képernyőre tabulátorral elválasztva az évad- és az epizódszámot, valamint a sorozat címét a minta szerint!
print("\n5. feladat")
date = input("Adjon meg egy dátumot! Dátum = ")
i = 0
for adat in adatok:
    if adat['datum'] <= date and adat['latta'] == 0:
        print(f"{adat['epizod']}\t{adat['cim']}")    
    i += 1


# 6. feladat: Készítse el a megadott algoritmus alapján a hét napját meghatározó függvényt!
#   A függvény neve Hetnapja legyen!
#   A függvény az év, hónap és nap megadása után szöveges eredményként visszaadja, hogy az adott nap a hét melyik napja volt.
#   (Az a és b egész számok maradékos osztása esetén az a div b kifejezés adja meg a hányadost, az a mod b pedig a maradékot, például 17 div 7 = 2 és 17 mod 7 = 3.)
print("\n6. feladat")
def hetnapja(ev, ho, nap):
    napok = ['v', 'h', 'k', 'sze', 'cs', 'p', 'szo']
    honapok = [0, 3, 2, 5, 1, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev = ev - 1
    hetnapja = napok[(ev + ev//4 - ev//100 + ev//400 + honapok[ho-1] + nap) % 7]
    return hetnapja
print("Függgvény kész.")


# 7. feladat: Kérjen be a felhasználótól egy napot az előző feladatban látható rövidített alakban!
#   A napokat egy (h, k, p, v), kettő (cs), vagy három (sze, szo) karakterrel adja meg!
#   Határozza meg, hogy a fájlban lévő sorozatok közül melyike(ke)t vetítik az adott napon!
#   A sorozatok nevét a minta szerint jelenítse meg a képernyőn!
#   Ha az adott napon egy sorozatot sem adtak adásba, akkor „Az adott napon nem kerül adásba sorozat.” üzenetet jelenítse meg!
print("\n7. feladat")
nap = input("Adja meg a hét egy napját (például cs)! Nap = ")
cimek = []

for adat in adatok:
    if adat['datum'] != 'NI' and hetnapja(int(adat['datum'][0:4]), int(adat['datum'][5:7]), int(adat['datum'][8:10])) == nap:
        if adat['cim'] not in cimek:
            cimek.append(adat['cim'])
if cimek == []:
    print('Az adott napon nem kerül adásba sorozat.')
for cim in cimek:
    print(cim)
    
# 8. feladat: Határozza meg sorozatonként az epizódok összesített vetítési idejét és az epizódok számát!
#   A számításnál vegye figyelembe a vetítési dátummal nem rendelkező epizódokat is!
#   A megoldás során felhasználhatja, hogy egy sorozat epizódjainak adatai egymást követik a forrásállományban.
#   A listát írja ki a summa.txt fájlba!
#   A fájl egy sorában a sorozat címe,az adott sorozatra vonatkozó összesített vetítési idő percben és az epizódok száma szerepeljen szóközzel elválasztva!
print("\n8. feladat")
with open('summa_dict_in_list.txt', 'w') as file:
    elozo = adatok[0]
    # a ciklusban összes elemen végigmegyünk, a legelsőn is, majd ott berakjuk a perc és darab adatokat
    per = 0         
    ep = 0
    for adat in adatok:
        if adat['cim'] == elozo['cim'] :
            # sorozat x. eleme, csak növelünk
            per += adat['perc']
            ep += 1
        else:
            # sorozat váltás: ki kell írni az előző sorozatot
            file.write(f"{elozo['cim']} {per} {ep}")
            file.write(f"\n")
            # új sorozat első elemét letároljuk
            per = adat['perc']
            ep = 1
            elozo = adat
    # az utolsó sorozat kiiratása
    file.write(f"{elozo['cim']} {per} {ep}")
print(f"Adatok kiírva a 'summa_dict_in_list.txt' állományba!")