# kosár kezelésére szolgáló osztály
class Kosar:
	def __init__(self):
		self.sorszam = 0
		self.osszDb	= 0
		self.osszAr	= 0
		self.termekek = []

	def getTermek(self,termeknev):
		_vanBenne = None
		for termek in self.termekek:
			if (termek.nev == termeknev) :
				_vanBenne = termek
		return _vanBenne	

# termék kezelésére szolgáló osztály
class Termek:
	def __init__(self):
		self.nev = ""
		self.db = 0

# 6. feladat: Határozza meg, hogy a bekért darabszámot vásárolva egy termékből mennyi a fizetendő összeg!
#   A feladat megoldásához készítsen függvényt ertek néven, amely a darabszámhoz a fizetendő összeget rendeli!
def ertek(db):
	osszAr = 0
	if db == 1:
		osszAr += 500
	elif db == 2:
		osszAr += 500 + 450
	else:
		osszAr += 500 + 450 + 400*(db-2)
	return osszAr

kosarak=[]

# 1. feladat: Olvassa be és tárolja el a penztar.txt fájl tartalmát!
print("\n1. feladat")
sorszam = 1
kosar = Kosar()  # üres kosárral indítunk
with open("penztar.txt", "r") as fileBe:
    for sor in fileBe:
        sorAdat = sor.strip()
        if sorAdat == "F":
            # kosár fizetés
            ossz = 0
            # összeszámoljuk az egyes terméktípusok után fizetendő összeget
            for termek in kosar.termekek:
                ossz += ertek(termek.db)
            kosar.osszAr = ossz       # letároljuk a kosárba a teljes fizetendő összeget
            kosar.sorszam = sorszam     # letároljuk a kosárba a vásárló sorszámát
            sorszam += 1
            kosarak.append(kosar)
            # új kosarat nyitunk
            kosar = Kosar()
        else:
            # kosarat feltölt
            # vesszük a kosárbeli terméket
            termek = kosar.getTermek(sorAdat)
            # ha nincs, akkor üres objektumot kapunk vissza, ekkor létrehozzuk a kosárban a terméket
            if termek == None:
                # ha nincs még ilyen termék a kosárban, akkor felvesszük
                termek = Termek()
                termek.nev = sorAdat
                termek.db = 1
                kosar.termekek.append(termek)
            else:
                # van, ekkor csak növeljük a termék számát
                termek.db +=1                   # növeljük a kosárbeli termék darabszámát
            kosar.osszDb += 1                   # növeljük a kosárbeli termékek számát
print("Az adatok beolvasva a 'penztar.txt' állományból.")

# 2. feladat: Határozza meg, hogy hányszor fizettek a pénztárnál!
print("\n2. feladat")
print(f"A kifizetések száma: {len(kosarak)}")

# 3. feladat: Írja a képernyőre, hogy az első vásárlónak hány darab árucikk volt a kosarában!
print("\n3. feladat")
print(f"Az első vásárló {kosarak[0].osszDb} darab árucikket vásárolt.")

# 4. feladat: Kérje be a felhasználótól egy vásárlás sorszámát, egy árucikk nevét és egy darabszámot!
#   A következő három feladat megoldásánál ezeket használja fel!
print("\n4. feladat")
beSzam = int(input("Adja meg egy vásárlás sorszámát! "))
beNev = input("Adja meg egy árucikk nevét! ")
beDb = int(input("Adja meg a vásárolt darabszámot! "))

# 5. feladat: Határozza meg, hogy a bekért árucikkből
#   a. melyik vásárláskor vettek először, és melyiknél utoljára!
#   b. összesen hány alkalommal vásároltak!
print("\n5. feladat")
vasarElso = None
vasarUtso = None
vasarDb = 0
for kosar in kosarak:
    # ha még nincs első vásárló
    if vasarElso == None:
        # és van benne termék
        if kosar.getTermek(beNev) != None:
            vasarElso = kosar
    # ha van benne termék akkor megjegyezzük a kosarat
    if kosar.getTermek(beNev):
        vasarUtso = kosar
        vasarDb +=1
print(f"Az első vásárlás sorszáma: {vasarElso.sorszam}")
print(f"Az utolsó vásárlás sorszáma: {vasarUtso.sorszam}")
print(f"{vasarDb} vásárlás során vettek belőle")

# 6. feladat: Határozza meg, hogy a bekért darabszámot vásárolva egy termékből mennyi a fizetendő összeg!
#   A feladat megoldásához készítsen függvényt ertek néven, amely a darabszámhoz a fizetendő összeget rendeli!
#   A függvény a forráskód elején!
print("\n6. feladat")
print(f"{beDb} darab vételekor fizetendő: {ertek(beDb)}")

# 7. feladat: Határozza meg, hogy a bekért sorszámú vásárláskor mely árucikkekből és milyen mennyiségben vásároltak!
#   Az árucikkek nevét tetszőleges sorrendben megjelenítheti.
print("\n7. feladat")
# a kosarak indexe eggyel kisebb, mind a kosarak sorszáma
for termek in kosarak[beSzam-1].termekek:
    print(f"{termek.db} {termek.nev}")

# 8. feladat: Készítse el az osszeg.txt fájlt, amelybe soronként az egy-egy vásárlás alkalmával fizetendő összeg kerüljön a kimeneti mintának megfelelően!
print("\n8. feladat")
with open("osszeg.txt", "w") as fileKi:
    for kosar in kosarak:
        fileKi.writelines("{}: {}\n".format(kosar.sorszam, kosar.osszAr))
print("Adatok kiírva az 'osszeg.txt' állományba")