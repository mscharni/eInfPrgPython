# 2007 május - SMS - Emelt Informatika Érettségi feladat
kod = {
    "a" : "2",
    "b" : "2",
    "c" : "2",
    "d" : "3",
    "e" : "3",
    "f" : "3",
    "g" : "4",
    "h" : "4",
    "i" : "4",
    "j" : "5",
    "k" : "5",
    "l" : "5",
    "m" : "6",
    "n" : "6",
    "o" : "6",
    "p" : "7",
    "q" : "7",
    "r" : "7",
    "s" : "7",
    "t" : "8",
    "u" : "8",
    "v" : "8",
    "w" : "9",
    "x" : "9",
    "y" : "9",
    "z" : "9",
    }

# a paraméterként kapott szónak megfelelő kódsort adja vissza
def kodol(szo):
    kodsor = ""
    for betu in list(szo):
        kodsor += kod[betu]
    return kodsor
    
# 1. Kérjen be a felhasználótól egy betűt, és adja meg, hogy milyen kód (szám) tartozik hozzá!
print("\n1. feladat")
betu = input("Betű = ").lower()
print(f"Kód = {kod[betu]}")

# 2. Kérjen be a felhasználótól egy szót, és határozza meg, hogy milyen számsorral lehet ezt a telefonba bevinni!
print("\n2. feladat")
szo = input("Szó = ").lower()
print(f"Kódsor = {kodol(szo)}")

# 3. Olvassa be a szavak.txt fájlból a szavakat, és a továbbiakban azokkal dolgozzon
print("\n3. feladat")
szavak = []
with open ("szavak.txt", "r") as fileBe:
    for line in fileBe:
        szavak.append(line.strip().lower())

# 4. Határozza meg és írassa a képernyőre, hogy melyik a leghosszabb tárolt szó!
#   Amennyiben több azonos hosszúságú van, elegendő csak az egyiket megjeleníteni.
#   Adja meg ennek a szónak a hosszát is!
print("\n4. feladat")
hosszo = ""
for szo in szavak:
    if len(szo) > len(hosszo):
        hosszo = szo
print(f"Leghosszabb szó a '{hosszo}', amely hossza {len(hosszo)}!")


# 5. Határozza meg és írassa a képernyőre, hogy hány rövid szó található a fájlban!
#   Rövid szónak tekintjük a legfeljebb 5 karakterből álló szavakat.
print("\n5. feladat")
rovidb = 0
for szo in szavak:
    if len(szo) <= 5:
        rovidb += 1
print(f"{rovidb} rövid szó található a szótárban!")

# 6. Írassa a kodok.txt állományba a szavak.txt fájlban található szavaknak megfelelő számkódokat!
#   Minden szónak feleljen meg egy számkód, és minden számkód külön sorba kerüljön!
print("\n6. feladat")
with open("kodok.txt", "w") as fileKi:
    for szo in szavak:
        fileKi.writelines(kodol(szo))
        fileKi.writelines("\n")
print("Adatok kiírva a 'kodok.txt' állományba.")
