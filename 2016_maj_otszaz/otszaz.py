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

class Termek:
	def __init__(self):
		self.nev = ""
		self.db = 0

# 6. feladat
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
# 1. feladat
print("1. feladat")
fileBe = open("penztar.txt", "r")
sorszam = 1
kosar = Kosar()     # üres kosárral indítunk
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
fileBe.close

# 2. feladat
print("2. feladat")
print("A kifizetések száma: {}".format(len(kosarak)))

# 3. feladat
print("3. feladat")
print("Az első vásárló {} darab árucikket vásárolt.".format(kosarak[0].osszDb))

# 4. feladat
print("4. feladat")
beSzam = int(input("Adja meg egy vásárlás sorszámát! "))
beNev = input("Adja meg egy árucikk nevét! ")
beDb = int(input("Adja meg a vásárolt darabszámot! "))

# 5. feladat
print("5. feladat")
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
print("Az első vásárlás sorszáma: {}".format(vasarElso.sorszam))
print("Az utolsó vásárlás sorszáma: {}".format(vasarUtso.sorszam))
print("{} vásárlás során vettek belőle".format(vasarDb))

# 6. feladat
# forráskód elején

# 7. feladat
print("7. feladat")
# a kosarak indexe eggyel kisebb, mind a kosarak sorszáma
for termek in kosarak[beSzam-1].termekek:
    print("{} {}".format(termek.db, termek.nev))

# 8. feladat
fileKi = open("osszeg.txt", "w")
for kosar in kosarak:
    fileKi.writelines("{}: {}\n".format(kosar.sorszam, kosar.osszAr))
fileKi.flush()
fileKi.close()