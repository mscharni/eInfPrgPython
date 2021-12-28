class Hianyzo:
	ho = 0
	nap = 0
	nev = ""
	orak ="       "

class Tanulo:
	nev = ""
	osszhianyzas = 0

# 1. feladat
hianyzok = []
ho = 0
nap = 0
fileBe = open('naplo.txt', 'r')
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

# 2. feladat	
print("2. feladat")
print("A naplóban {} bejegyzés van.".format(len(hianyzok)))

# 3. feladat
print("3. feladat")
igazolt = 0
igtlan = 0
for hianyzo in hianyzok:
    igazolt += hianyzo.orak.count("X")
    igtlan += hianyzo.orak.count("I")

print("Az igazolt hiányzások száma {}, az igazolatlanoké {} óra.".format(igazolt, igtlan))

# 4. feladat
def hetnapja(honap, nap):
    napnev = ("vasarnap", "hetfo", "kedd", "szerda", "csutortok","pentek", "szombat")
    napszam = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
    napsorszam = (napszam[honap-1]+nap) % 7
    return  napnev[napsorszam]

# 5. feladat
print("5. feladat")
honap = int(input("A hónap sorszáma = "))
nap = int(input("A nap sorszáma = "))
print("Azon a napon {} volt.".format(hetnapja(honap, nap)))

# 6. feladat
print("6. feladat")
napnev = input("A nap neve = ")
orasorsz = int(input("A óra sorszáma = ")) -1
osszhianyzas = 0
for hianyzo in hianyzok:
    if hetnapja(hianyzo.ho, hianyzo.nap) == "szerda":
        if (hianyzo.orak[orasorsz] ==  "X") or (hianyzo.orak[orasorsz] ==  "I"):
            osszhianyzas += 1
print("Ekkor összesen {} óra hiányzás történt.".format(osszhianyzas))


# 7. feladat
tanulok = []
print("7. feladat")
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
    