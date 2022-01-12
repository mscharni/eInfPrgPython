### Emelt Informatika Érettségi - 2016 Május - Ötszáz

# 6. feladat: Határozza meg, hogy a bekért darabszámot vásárolva egy termékből mennyi a fizetendő összeg!
#   A feladat megoldásához készítsen függvényt ertek néven, amely a darabszámhoz a fizetendő összeget rendeli!
def ertek(db):
    ossz = 500
    if db == 1:
        ossz += 500
    elif db == 2:
        ossz += 500 + 450
    else:
        ossz += 500 + 450 + 400*(db-2)
    return ossz

kosarak=[]

# 1. feladat: Olvassa be és tárolja el a penztar.txt fájl tartalmát!
print("\n1. feladat")
sorszam = 0
kosar = {}  # kezdetben üres a kosár
with open("penztar.txt", "r") as fileBe:
    for sor in fileBe:
        termek = sor.strip()
        if termek == "F":
            # kosár fizetés
            sorszam += 1
            ossz_db = 0
            ossz_ar = 0
            # összeszámoljuk a termékek darabszámát és az egyes termékek darabszám után fizetendő összeget
            for termek in kosar:
                ossz_db += kosar[termek]
                ossz_ar += ertek(kosar[termek])
            # a kiegészítő információk neveit aláhúzásjellel kezdjük, hogy megkülönböztethessük a termékek neveitől
            kosar["_sorszam"] = sorszam       # letároljuk a kosárba a vásárló sorszámát
            kosar["_ossz_db"] = ossz_db       # letároljuk a kosárba a összes termék darabszámát
            kosar["_ossz_ar"] = ossz_ar       # letároljuk a kosárba a teljes fizetendő összeget
            kosarak.append(kosar)
            # új kosarat nyitunk (kiürítjuk a péntárosnál lévő kosarat)
            kosar = {}
        else:
            try:
                # ha van már a kosárban ilyen termék, akkor növeljük a darabszámát
                kosar[termek] +=1  
            except KeyError:
                # ha nincs, akkor létrehozzuk a kosárban a terméket
                kosar[termek] = 1

print("Az adatok beolvasva a 'penztar.txt' állományból.")

# 2. feladat: Határozza meg, hogy hányszor fizettek a pénztárnál!
print("\n2. feladat")
# a kifizetések száma ugyanayyi, mint a kosár sorszáma 
print(f"A kifizetések száma: {sorszam}")

# 3. feladat: Írja a képernyőre, hogy az első vásárlónak hány darab árucikk volt a kosarában!
print("\n3. feladat")
# az első korás a nulladik
print(f"Az első vásárló {kosarak[0]['_ossz_db']} darab árucikket vásárolt.")

# 4. feladat: Kérje be a felhasználótól egy vásárlás sorszámát, egy árucikk nevét és egy darabszámot!
#   A következő három feladat megoldásánál ezeket használja fel!
print("\n4. feladat")
sorszam = int(input("Adja meg egy vásárlás sorszámát! "))
termek = input("Adja meg egy árucikk nevét! ")
db = int(input("Adja meg a vásárolt darabszámot! "))

# 5. feladat: Határozza meg, hogy a bekért árucikkből
#   a. melyik vásárláskor vettek először, és melyiknél utoljára!
#   b. összesen hány alkalommal vásároltak!
print("\n5. feladat")
elso = -1
utso = -1
vasaroltak = 0
for kosar in kosarak:
    # ha a kosárban van adott termék
    if termek in kosar.keys():
        vasaroltak +=1
        # elsőként?
        if elso == -1:
            elso = kosar["_sorszam"]
        utso = kosar["_sorszam"]            

print(f"Az első vásárlás sorszáma: {elso}")
print(f"Az utolsó vásárlás sorszáma: {utso}")
print(f"{vasaroltak} vásárlás során vettek belőle")

# 6. feladat: Határozza meg, hogy a bekért darabszámot vásárolva egy termékből mennyi a fizetendő összeg!
#   A feladat megoldásához készítsen függvényt ertek néven, amely a darabszámhoz a fizetendő összeget rendeli!
#   A függvény a forráskód elején!
print("\n6. feladat")
print(f"{db} darab vételekor fizetendő: {ertek(db)}")

# 7. feladat: Határozza meg, hogy a bekért sorszámú vásárláskor mely árucikkekből és milyen mennyiségben vásároltak!
#   Az árucikkek nevét tetszőleges sorrendben megjelenítheti.
print("\n7. feladat")
# a kosarak indexe eggyel kisebb, mind a kosarak sorszáma
kosar = kosarak[sorszam-1]
for termek in kosar:
    # csak a termékeket kell kiírni
    if termek[0] != "_": 
        print(f"{termek} {kosar[termek]}")

# 8. feladat: Készítse el az osszeg.txt fájlt, amelybe soronként az egy-egy vásárlás alkalmával fizetendő összeg kerüljön a kimeneti mintának megfelelően!
print("\n8. feladat")
with open("osszeg2.txt", "w") as fileKi:
    for kosar in kosarak:
        fileKi.write(f"{kosar['_sorszam']}: {kosar['_ossz_ar']}\n")
print("Adatok kiírva az 'osszeg2.txt' állományba")
