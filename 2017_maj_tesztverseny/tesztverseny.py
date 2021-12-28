class Versenyzo :
    azon = ""
    tippek = ""
    osszpont = 0 

versenyzok = []

# 1. feladat
print("1. feladat: Az adatok beolvasása")
fileBe = open("valaszok.txt", "r")
megoldasok = fileBe.readline().strip()
print(megoldasok)
for sor in fileBe:
    adat = sor.strip().split()
    versenyzo = Versenyzo()
    versenyzo.azon = adat[0]
    versenyzo.tippek = adat[1]
    versenyzo.osszpont = 0
    versenyzok.append(versenyzo)
fileBe.close()

# 2. feladat
print("2. feladat: A vetélkedőn {} versenyző indult.".format(len(versenyzok)))

# 3. feladat (A verzió)
beAzon = input("3. feladat: A versenyző azonosítója = ")
for versenyzo in versenyzok:
    if versenyzo.azon == beAzon:
        tipp = versenyzo.tippek 
        print("{}\t(a versenyző helyes válaszai [A megoldás])".format(tipp))
        break #megszakítjuk a ciklust (kilépünk a ciklusból)

# 3. feladat (B verzió)
i = 0
while versenyzok[i].azon == beAzon:
    i += 1
tipp = versenyzok[i-1].tippek
print("{}\t(a versenyző helyes válaszai [B megoldás])".format(tipp))

# 4. feladat
print("2. feladat:")
tippekJo = ""
for i in range(0,len(megoldasok)):
    if (megoldasok[i] == tipp[i]):
        tippekJo += "+"
    else :
        tippekJo += " "
    
print("{}\t(a helyes megoldás)".format(megoldasok))
print("{}\t(a versenyző helyes válaszai)".format(tippekJo))

# 5. feladat
joValaszadok = 0
sorszam = int(input("5. feladat: A feladat sorszáma = "))-1     #sorszám 0-tól indul 
for versenyzo in versenyzok:
        if versenyzo.tippek[sorszam] == megoldasok[sorszam]:
            joValaszadok += 1
szazalek = 100* joValaszadok / len(versenyzok)
print("A feladatra {} fő, a versenyzők {:.2f}%-a adott helyes választ.".format(joValaszadok, szazalek))

# 6. feladat
print("6. feladat: A versenyzők pontszámának meghatározása")
# A verzió
fileKi = open("pontok_A.txt", "w")
for versenyzo in versenyzok:
	osszPont = 0
	for i in range(0, len(versenyzo.tippek)):
		if versenyzo.tippek[i] == megoldasok[i]:
			if i < 5 :
				osszPont += 3
			elif i < 10:
				osszPont += 4
			elif i < 13:
				osszPont += 5
			else:
				osszPont += 6
	versenyzo.osszpont = osszPont
	fileKi.writelines("{} {}\n".format(versenyzo.azon, osszPont))
fileKi.flush()
fileKi.close()
# B verzió
ertek = (3,3,3,3,3,4,4,4,4,4,5,5,5,6)
fileKi = open("pontok_B.txt", "w")
for versenyzo in versenyzok:
	osszPont = 0
	for i in range(0, len(versenyzo.tippek)):
		if versenyzo.tippek[i] == megoldasok[i]:
				osszPont += ertek[i]
	versenyzo.osszpont = osszPont
	fileKi.writelines("{} {}\n".format(versenyzo.azon, osszPont))
fileKi.flush()
fileKi.close()

# 7. feladat
print("7. feladat: A verseny legjobbjai:")
# megkeresessük a három legnagyobb értéket
max = [0,0,0]
for versenyzo in versenyzok:
    if versenyzo.osszpont > max[0]:
        max[2] = max[1]
        max[1] = max[0]
        max[0] = versenyzo.osszpont
    else: 
        if versenyzo.osszpont < max[0] and versenyzo.osszpont > max[1]:
            max[2] = max[1]
            max[1] = versenyzo.osszpont
        else: 
            if versenyzo.osszpont < max[1] and versenyzo.osszpont > max[2]:
                max[2] = versenyzo.osszpont
# kiiratjuk a három legmagasabb értékhez tartozó versenyzőket
for i in range(0,3):
    for versenyzo in versenyzok:
        if versenyzo.osszpont == max[i]:
            print("{}. díj ({} pont): {}".format(i+1, versenyzo.osszpont, versenyzo.azon))
