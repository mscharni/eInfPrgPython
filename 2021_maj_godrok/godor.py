### Emelt Informatika Érettségi - 2021 május - Gödrök

# 1. feladat: Olvassa be és tárolja el a melyseg.txt fájl tartalmát!
# Írja ki a képernyőre, hogy az adatforrás hány adatot tartalmaz!
datas = []
print("1. feladat")
# olvasásra (r) nyitjuk meg az állományt
with open("melyseg.txt", "r") as fileBe:
    lines = fileBe.readlines()
for line in lines:
    data = int(line.strip())
    datas.append(data)
data_count = len(datas)
print(f"A fájl adatainak száma: {data_count}")

# 2. feladat: Olvasson be egy távolságértéket, majd írja a képernyőre, hogy milyen mélyen van a gödör alja azon a helyen!
# Ezt a távolságértéket használja majd a 6. feladat megoldása során is!
print("2. feladat")
tav = int(input("Adjon meg egy távolságértéket!")) - 1
melyseg = datas[tav]
print(f"Ezen a helyen a felszín {melyseg} méter mélyen van.")

# 3. feladat: Határozza meg, hogy a felszín hány százaléka maradt érintetlen és jelenítse meg 2 tizedes
# pontossággal!
print("3. feladat")
zeros = 0
for data in datas:
    if data == 0:
        zeros += 1
print(zeros)
# vagy az értéket kerekítjük (ha a továbbiakban már nincs szükségünk a pontos értékre)
arany = round(100 * zeros / data_count, 2)
print(f"Az érintetlen terület aránya {arany}%.")

# vagy a kiiratást kerekítjük, így megmarad az eredeti arány értéke a további felhasználásra
# arany2 = zeros / data_count
# print(f"Az érintetlen terület aránya {arany2:4.2%}.")

# 4. feladat: Írja ki a godrok.txt fájlba a gödrök leírását, azaz azokat a számsorokat, amelyek egy-egy gödör méterenkénti mélységét adják meg!
# Minden gödör leírása külön sorba kerüljön! Az állomány pontosan a gödrök számával egyező számú sort tartalmazzon!
# írásra (w) nyitjuk meg az állományt
with open("godrok.txt", "w") as fileKi:
    godor = False
    godor_count = 0
    for data in datas:
        if data != 0:
            fileKi.write(str(data))
            godor = True
        elif godor == True:
            fileKi.write("\n")
            godor = False
            godor_count += 1

# 5. feladat: Határozza meg a gödrök számát és írja a képernyőre!
print("5. feladat")
print(f"A gödrök száma: {godor_count}")

# 6. feladat: Ha a 2. feladatban beolvasott helyen nincs gödör, akkor „Az adott helyen nincs gödör.” üzenetet jelenítse meg, ha ott gödör található, akkor határozza meg, hogy...
print("6. feladat")
# a 'tav' helyen a 'melyseg' érték
if melyseg == 0:
    print("Az adott helyen nincs gödör.")
else:
    # 6/a feladat: mi a gödör kezdő és végpontja?
    print("a)")
    # kezdőpont megkeresése
    kezdet = tav
    while datas[kezdet - 1] != 0:
        kezdet -= 1
    # mivel nullától indul a sorszám, ezért növelni kell eggyel a kezdet sorszámát
    kezdet += 1
    # print(kezdet,datas[kezdet-1])
    # végpont megkeresése
    veg = tav
    while datas[veg] != 0:
        veg += 1

    print(f"A gödör kezdete: {kezdet} méter, a gödör vége: {veg} méter.")

    # 6/b feladat: a legmélyebb pontja felé mindkét irányból folyamatosan mélyül-e:
    print("b)")
    monotonitas = "le"
    valtas = 0
    for i in range(kezdet - 1, veg):
        if datas[i] < datas[i + 1] and monotonitas == "fel":
            # felfeléből lefele
            valtas += 1
            monotonitas = "le"
        elif datas[i] > datas[i + 1] and monotonitas == "le":
            # lefeléből felfele
            valtas += 1
            monotonitas = "fel"

    if valtas > 1:
        print("Nem mélyül folyamatosan.")
    else:
        print("Folyamatosan mélyül.")

    # 6/c feladat: mekkora a legnagyobb mélysége?
    print("c)")
    max_mely = 0
    for i in range(kezdet - 1, veg):
        if datas[i] > max_mely:
            max_mely = datas[i]
    print(f"A legnagyobb mélysége {max_mely} méter.")

    # 6/d feladat: mekkora a térfogata, ha szélessége minden helyen 10 méternyi?
    print("d)")
    terfogat = 0
    for i in range(kezdet - 1, veg):
        terfogat = terfogat + datas[i] * 10
    print(f"A térfogata {terfogat} m^3.")

    # 6/e feladat: mennyi vizet képes befogadni, ha a felszín legalább 1 méter mélyen van?
    print("e)")
    max_viz = terfogat - (veg - kezdet + 1) * 10
    print(f"A vízmennyiség {max_viz} m^3.")
