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

# 1. feladat 
# print("1. feladat")
# file megnyitása olvasásra
fileBe = open("ajto.txt", "r")
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
# file bezárása
fileBe.close()

# 2. feladat 
print("2. feladat")
# valójában ez felesleges, mivel a legelső sorban van az első belépő (kezdetben üres a társalgó...)
elsoBe = 0
while adatok[elsoBe].beki != "be":
    elsoBe += 1
print("Az első belépő : {}".format(adatok[elsoBe].azo))
utolsoKi = len(adatok)-1
while adatok[utolsoKi].beki != "ki":
    utolsoKi -= 1
print("Az utolsó kilépő : {}".format(adatok[utolsoKi].azo))


# 3. feladat 
# print("\n3. feladat")
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
fileKi = open("athaladas.txt", "w")
for szemely in szemelyek:
    if szemely.atlep != 0:
        fileKi.writelines(str(szemely.azo) + " " + str(szemely.atlep) +"\n")

# file bezárása
fileKi.flush()
fileKi.close()

# 4. feladat 
print("\n4. feladat")
bentiek = "A végén a társalgóban voltak:"
for szemely in szemelyek:
    if szemely.beki == "be":
        bentiek += " " + str(szemely.azo)
print("{}".format(bentiek))

# 5. feladat 
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
print("Például {}-kor voltak a legtöbben a társalgóban.".format(maxIdo))

# 6. feladat 
print("\n6. feladat")
beAzo = int(input("Adja meg a személy azonosítóját! "))

# 7. feladat 
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

# 8. feladat 
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
print("A(z) {}. személy összesen {} percet volt bent, a megfigyelés végén {}".format(beAzo,osszIdo,beki))