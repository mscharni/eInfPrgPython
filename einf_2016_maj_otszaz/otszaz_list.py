### Emelt Informatika Érettségi - 2016 Május - Ötszáz

# 6. feladat: Határozza meg, hogy a bekért darabszámot vásárolva egy termékből mennyi a fizetendő összeg!
#   A feladat megoldásához készítsen függvényt ertek néven, amely a darabszámhoz a fizetendő összeget rendeli!
def ertek(db):
    if db > 2:
        ossz = 500 + 450 + 400*(db-2)
    elif db == 2:
        ossz = 500 + 450
    else:
        ossz = 500
    return ossz

kosarak=[]

# 1. feladat: Olvassa be és tárolja el a penztar.txt fájl tartalmát!
print("\n1. feladat")
sorszam = 0
kosar = [["F",0]]  # kezdetben üres a kosár, de belerakunk két fiktív terméket (a kosár végére végére), hogy a keresés funkció működjön
# egy termék ['termék neve', darab] formában kerüla  kosárba
with open("penztar.txt", "r") as fileBe:
    for sor in fileBe:
        termek = sor.strip()
        if termek == "F":
            # letároljuk a kész kosarak között
            kosarak.append(kosar)
            # új kosarat nyitunk (kiürítjuk a péntárosnál lévő kosarat)
            kosar = [["F",0]]
        else:
            # megnézzük, hogy van-e már a kosárban ilyen termék
            i = 0
            while kosar[i][0] != termek and kosar[i][0] != "F":
                i += 1
            # ha nincs a kosárban ilyen termék, akkor belerakjuk
            if kosar[i][0] == "F":
                kosar.insert(0,[termek, 1])
            else:
                # van, tehát növeljük a darabszámot
                kosar[i][1] +=1  

print("Az adatok beolvasva a 'penztar.txt' állományból.")

# 2. feladat: Határozza meg, hogy hányszor fizettek a pénztárnál!
print("\n2. feladat")
# a kifizetések száma ugyanannyi, mint a kosarak száma 
print(f"A kifizetések száma: {len(kosarak)}")

# 3. feladat: Írja a képernyőre, hogy az első vásárlónak hány darab árucikk volt a kosarában!
print("\n3. feladat")
# az első korás a nulladik, végigmegyünk az összes trméken és összeadjuk a darabszámokat
db = 0
for termek in kosarak[0]:
    db += termek[1]
print(f"Az első vásárló {db} darab árucikket vásárolt.")

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
hanyszor = 0
idx = 0
for kosar in kosarak:
    # megkeressük, hogy van-e a kosárban az adott termékből
    i = 0
    while kosar[i][0] != termek and kosar[i][0] != "F":
        i += 1
    # ha van már a kosárban ilyen termék, akkor növeljük a darabszámát
    if kosar[i][0] != "F":
        hanyszor +=1
        # elsőként?
        if elso == -1:
            elso = idx
        utso = idx
    idx += 1
print(f"Az első vásárlás sorszáma: {elso+1}")
print(f"Az utolsó vásárlás sorszáma: {utso+1}")
print(f"{hanyszor} vásárlás során vettek belőle")

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
    if termek[0] != "F": 
        print(f"{termek[0]} {termek[1]}")

# 8. feladat: Készítse el az osszeg.txt fájlt, amelybe soronként az egy-egy vásárlás alkalmával fizetendő összeg kerüljön a kimeneti mintának megfelelően!
print("\n8. feladat")
with open("osszeg_list.txt", "w") as fileKi:
    idx = 1
    for kosar in kosarak:
        # kosárbeli termékek összes ára
        osszar = -500  # a "F" fiktív termékért nem fizetünk
        for termek in kosar:
            osszar += ertek(termek[1])
        fileKi.write(f"{idx}: {osszar}\n")
        idx +=1
print("Adatok kiírva az 'osszeg_list.txt' állományba")
