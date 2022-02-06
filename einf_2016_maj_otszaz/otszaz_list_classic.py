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
kosar = [[],[]]  # kezdetben üres a kosár, két üres listát tartalmaz, az első a termékek nevét, a második az adott termék darabszámát tartalmazza
# egy termék [termék neve] és [darab] formában kerüla  kosárba
with open("penztar.txt", "r") as fileBe:
    for sor in fileBe:
        termek = sor.strip()
        if termek == "F":
            # letároljuk a kész kosarak között
            kosarak.append(kosar)
            # új kosarat nyitunk (kiürítjuk a péntárosnál lévő kosarat)
            kosar = [[],[]]
        else:
            # megpróbáljuk megnövelni a termék kosárbeli sorszámának megfelelő darabszámot
            try:
                # ha van ilyen termék, akkor sikerül
                kosar[1][kosar[0].index(termek)] +=1  
            except ValueError:
                # ha nem sikerül, akkor a kosár végéhez fűzzük a termék nevét és darabszámát
                kosar[0].append(termek)
                kosar[1].append(1)

print("Az adatok beolvasva a 'penztar.txt' állományból.")
print(kosarak)
# 2. feladat: Határozza meg, hogy hányszor fizettek a pénztárnál!
print("\n2. feladat")
# a kifizetések száma ugyanayyi, mint a kosarak száma 
print(f"A kifizetések száma: {len(kosarak)}")

# 3. feladat: Írja a képernyőre, hogy az első vásárlónak hány darab árucikk volt a kosarában!
print("\n3. feladat")
# az első korás a nulladik, végigmegyünk az összes trméken és összeadjuk a darabszámokat
db = 0
for darab in kosarak[0][1]:
    db += darab
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
    # ha van már a kosárban ilyen termék, akkor növeljük a darabszámát
    if kosar[0].count(termek) != 0:
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
for i in range(0, len(kosar[0])):
     print(f"{kosar[0][i]} {kosar[1][i]}")

# 8. feladat: Készítse el az osszeg.txt fájlt, amelybe soronként az egy-egy vásárlás alkalmával fizetendő összeg kerüljön a kimeneti mintának megfelelően!
print("\n8. feladat")
with open("osszeg_list_classic.txt", "w") as fileKi:
    idx = 1
    for kosar in kosarak:
        # kosárbeli termékek összes ára
        osszar = 0
        for darab in kosar[1]:
            osszar += ertek(darab)
        fileKi.write(f"{idx}: {osszar}\n")
        idx +=1
print("Adatok kiírva az 'osszeg_list_classic.txt' állományba")
