jogosultak = 12345
valasztokeruletek = 8
# a pártokat a nevük helyett a listabeli sorszámukkal azonosítjuk be:
# 0 = "-", 1 = "GYEP", 2 = "HEP", 3 = "TISZ", 4 = "ZEP"
partok = ["-", "GYEP", "HEP", "TISZ", "ZEP"]
partnevek = ["Független jelöltek", "Gyümölcsevők Pártja", "Húsevők Pártja", "Tejivók Szövetsége", "Zöldségevők Pártja"]
partszavazatok = [0,0,0,0,0]
jeloltek = []
keruletek=[0 for i in range(0,10)] # a nulladik sorszámút nem használjuk (kerületek soráma 1-től 8-ig terjed)
kepviselok=[None for i in range(0,10)] # a nulladik sorszámút nem használjuk (kerületek soráma 1-től 8-ig terjed)

class Jelolt():
    kerulet = 0
    szavazat = 0
    nev = ""
    partkod = 0
    partnev = ""
    global partszavazatok
    def __init__(self, datas):
        self.kerulet = int(datas[0])
        self.szavazat = int(datas[1])
        self.nev = datas[2] + " " + datas[3]
        self.partkod = partok.index(datas[4])  # a párt kódja
        self.partnev = ""
        # mivel a feladatban keverik a párt nevét és rövidítését, ezért kell a vizsgálat...
        if self.partkod == 0:
            self.partnev = "Független"
        else:
            self.partnev = datas[4]
        partszavazatok[self.partkod] += self.szavazat   # egyből összesítjük a pártokra adott szavazatokat


#1. Olvassa be a szavazatok.txt fájl adatait, majd ezek felhasználásával oldja meg a következő feladatokat!
#   Az adatfájlban legfeljebb 100 képviselőjelölt adatai szerepelnek.
print("\n1. feladat")
with open("szavazatok.txt", "r", encoding="utf8") as file:
    for line in file:
        datas = line.strip().split(" ")
        jelolt = Jelolt(datas)
        jeloltek.append(jelolt)
print("Adatok beolvasva a 'szavazatok.txt' file-ból")

# 2. Hány képviselőjelölt indult a helyhatósági választáson?
#   A kérdésre egész mondatban válaszoljon az alábbi mintához hasonlóan:
    # A helyhatósági választáson 92 képviselőjelölt indult.
print("\n2. feladat")
print(f"A helyhatósági választáson {len(jeloltek)} képviselőjelölt indult.")

# 3. Kérje be egy képviselőjelölt vezetéknevét és utónevét, majd írja ki a képernyőre, hogy az illető hány szavazatot kapott!
#   Ha a beolvasott név nem szerepel a nyilvántartásban, úgy jelenjen meg a képernyőn az „Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!” figyelmeztetés!
#   A feladat megoldása során feltételezheti, hogy nem indult két azonos nevű képviselőjelölt a választáson.
print("\n3. feladat")
nev = input("Adja meg a képviselőjelölt vezeték és keresztnevét: ")
i = 0
while i < len(jeloltek)-1 and jeloltek[i].nev != nev:
    i += 1
if jeloltek[i].nev == nev:
    print(f"A '{jeloltek[i].nev}' nevű jelölt {jeloltek[i].szavazat} szavazatot kapott.")
else:
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")

# 4. Határozza meg, hányan adták le szavazatukat, és mennyi volt a részvételi arány!
#   (A részvételi arány azt adja meg, hogy a jogosultak hány százaléka vett részt a szavazáson.)
#   A részvételi arányt két tizedesjegy pontossággal, százalékos formában írja ki a képernyőre!
#   Például:
#   A választáson 5001 állampolgár, a jogosultak 40,51%-a vett részt.
print("\n4. feladat")
ossz_szavazat = 0
for jelolt in jeloltek:
    ossz_szavazat += jelolt.szavazat
arany = ossz_szavazat / jogosultak
print(f"A választáson {ossz_szavazat} állampolgár, a jogosultak {arany:.2%}-a vett részt.")

# 5. Határozza meg és írassa ki a képernyőre az egyes pártokra leadott szavazatok arányát az összes leadott szavazathoz képest két tizedesjegy pontossággal!
#   A független jelölteket együtt, „Független jelöltek” néven szerepeltesse!
#   Például:
#   Zöldségevők Pártja= 12,34%
#   Független jelöltek= 23,40%
print("\n5. feladat")
for i in range(0, len(partok)):
    print(f"{partnevek[i]:20} = {partszavazatok[i]/ossz_szavazat:.2%}")

# 6. Melyik jelölt kapta a legtöbb szavazatot? Jelenítse meg a képernyőn a képviselő vezeték és utónevét, valamint az őt támogató párt rövidítését, vagy azt, hogy független!
# Ha több ilyen képviselő is van, akkor mindegyik adatai jelenjenek meg!
# első körben megállapítjuk a maximumot
print("\n6. feladat")
max_szavazat = jeloltek[0].szavazat
for i in range(1, len(jeloltek)):
    if max_szavazat < jeloltek[i].szavazat:
        max_szavazat = jeloltek[i].szavazat
# második körben kiírjuk a maximum szavazattal rendelkező jelölt(ek)et
for jelolt in jeloltek:
    if jelolt.szavazat == max_szavazat:
        print(f"{jelolt.nev:20} - {jelolt.partnev:20}")
# opcionális megoldás a szebb kiiratás érdekében:
# # kigyűjtjük a max szavazatokat elért jelölteket egy listába
# max_jeloltek = []
# for jelolt in jeloltek:
#     if jelolt.szavazat == max_szavazat:
#         max_jeloltek.append(f"{jelolt.nev:20} - {jelolt.partnev:20}")
# # majd a számosségtól függően kiiratjuk az eredményt
# if len(max_jeloltek) == 1:
#     print(f"A legtöbb ({max_szavazat}) szavazatot kapott jelölt:")
#     print(max_jeloltek[0])
# else:
#     print(f"A legtöbb ({max_szavazat}) szavazatot kapott jelöltek:")
#     for i in range(0, len(max_jeloltek)):
#         print(max_jeloltek[i])

# 7. Határozza meg, hogy az egyes választókerületekben kik lettek a képviselők!
#   Írja ki a választókerület sorszámát, a győztes vezeték- és utónevét, valamint az őt támogató párt rövidítését, vagy azt, hogy független
#   egy-egy szóközzel elválasztva a kepviselok.txt nevű szöveges fájlba!
#   Az adatok a választókerületek száma szerinti sorrendben jelenjenek meg! Minden sorba egy képviselő adatai kerüljenek!
print("\n7. feladat")
for jelolt in jeloltek:
    if jelolt.szavazat > keruletek[jelolt.kerulet]:
        keruletek[jelolt.kerulet] = jelolt.szavazat
        kepviselok[jelolt.kerulet] = jelolt

with open("kepviselok.txt", "w", encoding="utf8") as file:
    for i in range(1,9):
        file.writelines(f"{i} {kepviselok[i].nev} {kepviselok[i].partnev}\n")
print("Adatok kiírva a 'kepviselok.txt' file-ba")