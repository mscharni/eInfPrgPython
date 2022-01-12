### Emelt Informatika Érettségi - 2018 Május - Társalgó

# adatszerkezet naplóbeli bejegyzés és személy
class Adat:
    azo = 0
    ora = 0
    perc = 0
    beki = ""

class Szemely:
    azo = 0
    atlep = 0
    beki = ""

# fileban tárolt adatok letárolására szolgáló lista
adatok = []

# 1. feladat: Olvassa be és tárolja el az ajto.txt fájl tartalmát!
print("\n1. feladat")
# file megnyitása olvasásra
with open("ajto.txt", "r") as fileBe:
    # adatok beolvasása fileból soronként
    for sor in fileBe:
        adatSor = sor.strip().split(" ")
        # új Naplo típusú objektum létrehozása (példányosítása)
        adat = Adat()
        # új objektum tulajdonságainak megadása
        adat.azo = int(adatSor[2])
        adat.ora = int(adatSor[0])
        adat.perc = int(adatSor[1])
        adat.beki = adatSor[3]
        # új objektum hozzáfűzése a listához
        adatok.append(adat)
print("Adatok beolvasva az 'ajto.txt' állományból.")

# 2. feladat: Írja a képernyőre annak a személynek az azonosítóját, aki a vizsgált időszakon belül először lépett be az ajtón, és azét, aki utoljára távozott a megfigyelési időszakban!
print("\n2. feladat")
# valójában ez felesleges, mivel a legelső sorban van az első belépő (kezdetben üres a társalgó...),
#   de a legelső, adott feltételnek megfelelő elem megkeresésének algoritmusa miatt szerepel
elsoBe = 0
while adatok[elsoBe].beki != "be":
    elsoBe += 1
print(f"Az első belépő : {adatok[elsoBe].azo}")
# utolsó kilépő megkeresése (visszafele)
utolsoKi = len(adatok)-1
while adatok[utolsoKi].beki != "ki":
    utolsoKi -= 1
print(f"Az utolsó kilépő : {adatok[utolsoKi].azo}")


# 3. feladat: Határozza meg a fájlban szereplő személyek közül, ki hányszor haladt át a társalgó ajtaján!
#   A meghatározott értékeket azonosító szerint növekvő sorrendben írja az athaladas.txt fájlba!
#   Soronként egy személy azonosítója, és tőle egy szóközzel elválasztva az áthaladások száma szerepeljen!
print("\n3. feladat")
# szemelyek adatait tartalmazó lista 
szemelyek = []
# feltöltjük üres értékekkel
for i in range(0,99):
    szemely = Szemely()
    szemely.azo = i
    szemely.atlep = 0
    szemely.beki = ""
    szemelyek.append(szemely)

# feltöltjük a személyek adatait (praktikusabb lehetne a filebeolvasáskor)
for adat in adatok:
    szemelyek[adat.azo].atlep += 1
    szemelyek[adat.azo].beki = adat.beki

# file megnyitása írásra
with open("athaladas.txt", "w") as fileKi:
    for szemely in szemelyek:
        if szemely.atlep != 0:
            fileKi.write(str(szemely.azo) + " " + str(szemely.atlep) +"\n")
print("Adatok kiírva az 'athaladas.txt' állományba.")

# 4. feladat: Írja a képernyőre azon személyek azonosítóját, akik a vizsgált időszak végén a társalgóban tartózkodtak!
print("\n4. feladat")
bentiek = "A végén a társalgóban voltak:"
for szemely in szemelyek:
    if szemely.beki == "be":
        bentiek += " " + str(szemely.azo)
print(f"{bentiek}")

# 5. feladat: Hányan voltak legtöbben egyszerre a társalgóban?
#   Írjon a képernyőre egy olyan időpontot (óra:perc), amikor a legtöbben voltak bent!
print("\n5. feladat")
letszam = 0
max = 0
maxIdo = ""
for adat in adatok:
    if adat.beki == "be":
        letszam += 1
        if letszam > max:
            max = letszam
            maxIdo = str(adat.ora) + ":" + str(adat.perc)
    else:
        letszam -= 1
print(f"Például {maxIdo}-kor voltak a legtöbben a társalgóban.")

# 6. feladat: Kérje be a felhasználótól egy személy azonosítóját!
#   A további feladatok megoldásánál ezt használja fel!
print("\n6. feladat")
beAzo = int(input("Adja meg a személy azonosítóját! "))

# 7. feladat: Írja a képernyőre, hogy a beolvasott azonosítóhoz tartozó személy mettől meddig tartózkodott a társalgóban!
print("\n7. feladat")
beIdo = ""
for adat in adatok:
    if adat.azo == beAzo:
        if adat.beki == "ki":
            print(beIdo + str(adat.ora) + ":" + str(adat.perc))
        else:
            beIdo = str(adat.ora) + ":" + str(adat.perc) +"-"
# ha bent marad, ki kell írni az utolsó kilépés időpontját
if szemelyek[beAzo].beki == "be":
    print(beIdo)

# 8. feladat: Határozza meg, hogy a megfigyelt időszakban a beolvasott azonosítójú személy összesen hány percet töltött a társalgóban!
#   Az előző feladatban példaként szereplő 22-es személy 5 alkalommal járt bent, a megfigyelés végén még bent volt.
#   Róla azt tudjuk, hogy 18 percet töltött bent a megfigyelés végéig.
#   A 39-es személy 6 alkalommal járt bent, a vizsgált időszak végén nem tartózkodott a helyiségben.
#   Róla azt tudjuk, hogy 39 percet töltött ott.
#   Írja ki,# hogy a beolvasott azonosítójú személy mennyi időt volt a társalgóban, és a megfigyelési időszak végén bent volt-e még!
print("\n8. feladat")
beki = ""
beIdo = 0
kiIdo= 0
osszIdo= 0
for adat in adatok:
    if adat.azo == beAzo:
        if adat.beki == "ki":
            kiIdo = adat.ora*60 + adat.perc
            osszIdo += kiIdo-beIdo
        else:
            beIdo = adat.ora*60 + adat.perc
# ha bent marad, hozzá kell adni a 15:00-ig terjedő időtartamot
if szemelyek[beAzo].beki == "be":
    osszIdo += 15*60-beIdo
    beki = "a társalgóban volt."
else:
    beki = "nem volt a társalgóban."
print(f"A(z) {beAzo}. személy összesen {osszIdo} percet volt bent, a megfigyelés végén {beki}")
