class Hianyzo:
	ho = 0
	nap = 0
	nev = ""
	orak ="       "

class Tanulo:
	nev = ""
	osszhianyzas = 0

# 1. feladat: Olvassa be és tárolja el a naplo.txt fájl tartalmát!
print("\n1. feladat")
hianyzok = []
ho = 0
nap = 0
with open('naplo.txt', 'r') as fileBe:
    for sorBe in fileBe:
        sor = sorBe.strip().split(" ")
        if sor[0] == "#":
            ho = int(sor[1])
            nap = int(sor[2])
        else:
            hianyzo = Hianyzo()
            hianyzo.ho = int(ho)
            hianyzo.nap = int(nap)
            hianyzo.nev	= sor[0] + " " + sor[1]
            hianyzo.orak = sor[2]
            hianyzok.append(hianyzo)
print("Adatok beolvasva a 'naplo.tx' állományból")

# 2. feladat: Határozza meg és írassa ki, hogy hány sor van a fájlban, ami hiányzást rögzít!
print("\n2. feladat")
print(f"A naplóban {len(hianyzok)} bejegyzés van.")

# 3. feladat: Számolja meg és írassa ki, hogy összesen hány óra igazolt és hány óra igazolatlan hiányzás volt a félév során!
print("\n3. feladat")
igazolt = 0
igtlan = 0
for hianyzo in hianyzok:
    igazolt += hianyzo.orak.count("X")
    igtlan += hianyzo.orak.count("I")

print(f"Az igazolt hiányzások száma {igazolt}, az igazolatlanoké {igtlan} óra.")

# 4. feladat: Készítsen függvényt hetnapja néven, amely a paraméterként megadott dátumhoz (hónap, nap) megadja, hogy az a hét melyik napjára esik (hétfő, kedd…).
#   Tudjuk, hogy az adott év nem volt szökőév, továbbá azt is, hogy január elseje hétfőre esett.
#   Használhatja az megadott algoritmust is, ahol a tömbök indexelése 0-val kezdődik, de ettől eltérő megoldású függvényt is készíthet.
print("\n4. feladat")
def hetnapja(honap, nap):
    napnev = ("vasarnap", "hetfo", "kedd", "szerda", "csutortok","pentek", "szombat")
    napszam = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
    napsorszam = (napszam[honap-1]+nap) % 7
    return  napnev[napsorszam]
print("Függvény kész.")

# 5. feladat: Kérjen be egy dátumot (hónap, nap), és a hetnapja függvény felhasználásával írassa ki, hogy az a hét melyik napjára esett!
print("\n5. feladat")
honap = int(input("A hónap sorszáma = "))
nap = int(input("A nap sorszáma = "))
print(f"Azon a napon {hetnapja(honap, nap)} volt.")

# 6. feladat: Kérje be a hét egy tanítási napjának nevét és egy aznapi tanítási óra óraszámát (például: kedd 3)!
#   Írassa ki a képernyőre, hogy a félév során az adott tanítási órára összesen hány hiányzás jutott!
print("\n6. feladat")
napnev = input("A nap neve = ")
orasorsz = int(input("A óra sorszáma = ")) -1
osszhianyzas = 0
for hianyzo in hianyzok:
    if hetnapja(hianyzo.ho, hianyzo.nap) == "szerda":
        if (hianyzo.orak[orasorsz] ==  "X") or (hianyzo.orak[orasorsz] ==  "I"):
            osszhianyzas += 1
print(f"Ekkor összesen {osszhianyzas} óra hiányzás történt.")


# 7. feladat: Írassa ki a képernyőre a legtöbb órát hiányzó tanuló nevét!
#   Ha több ilyen tanuló is van, akkor valamennyi neve jelenjen meg szóközzel elválasztva!
tanulok = []
print("\n7. feladat")
for hianyzo in hianyzok:
    ti = 0
    while ti < len(tanulok) and tanulok[ti].nev != hianyzo.nev:
        ti += 1
    if (ti == len(tanulok)):
        tanulo = Tanulo()
        tanulo.nev  = hianyzo.nev
        tanulo.osszhianyzas = 0
        tanulok.append(tanulo)
    else:
        tanulo = tanulok[ti]
    tanulo.osszhianyzas += hianyzo.orak.count("X") + hianyzo.orak.count("I")

# maxkeresés
maxHiany = tanulok[0].osszhianyzas
for tanulo in tanulok:
	if tanulo.osszhianyzas > maxHiany:
		maxHiany = tanulo.osszhianyzas

# max értékkel rendelkezők kiiratása
maxTanulok = "A legtöbbet hiányzó tanulók:"
for tanulo in tanulok:
    if tanulo.osszhianyzas == maxHiany:
        maxTanulok += " " + tanulo.nev
print(maxTanulok)
    