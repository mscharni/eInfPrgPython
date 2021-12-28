class Haz:
	oldal =  0
	hazszam = 0
	hossz = 0
	szin = ""

hazak = []      # összes ház
parosok = []    # páros oldalon lévő házak
ptlanok = []    # páratlan oldalon lévő házak

paros = 2		# páros oldal kezdő házszáma
ptlan = 1		# páratlan oldal kezdő házszáma

# 1. feladat
fileBe = open("kerites.txt", "r")
for sorBe in fileBe:
    adatok = sorBe.strip().split(" ")
    haz = Haz()
    haz.oldal = int(adatok[0])
    haz.hossz = int(adatok[1])
    haz.szin = str(adatok[2])
    if haz.oldal == 0:
        haz.hazszam = paros
        parosok.append(haz)
        paros += 2
    else:
        haz.hazszam = ptlan
        ptlanok.append(haz)
        ptlan += 2
    hazak.append(haz)
fileBe.close()

# 2. feladat
print("2. feladat")
print("Az eladott telkek száma: {}".format(len(hazak)))

# 3. feladat
print("3. feladat")
if hazak[-1].oldal == 0:
     oldal = "páros"
else :
    oldal = "páratlan"
print("A {} oldalon adták el az utolsó telket.".format(oldal))
print("Az utolsó telek házszáma: {}".format(hazak[-1].hazszam))

# 4. feladat
print("4. feladat")
i = 1
# bennmaradási feltétel: nem egyező színek vagy nem szín 
while (ptlanok[i].szin != ptlanok[i-1].szin) or ("#:".find(ptlanok[i].szin) != -1):
    i += 1
print("A szomszédossal egyezik a kerítés színe: {}".format(ptlanok[i].hazszam))

# 5. feladat
print("5. feladat")
szinek = ("A", "B", "C", "D")
hazSzam = int(input("Adjon meg egy házszámot!"))
# kiválasztjuk, hogy a páros, vagy páratlan oldallal dolgozunk 
# referencia
if hazSzam % 2 == 0:
	utca = parosok
else:
	utca = ptlanok

# megkeressük a házat 
i = 0
while hazSzam != utca[i].hazszam and i < len(utca):
	i += 1
hazSzin =  utca[i].szin
# derítsük ki, milyen színek nem lehetnek pl: "ABC"
nemJoSzin = "" + utca[i-1].szin  + utca[i].szin + utca[i+1].szin
# keresünk egy színt
j = 0
while nemJoSzin.find(szinek[j]) != -1 :
	j += 1

joHazSzin =  szinek[j]

print("A kerítés színe / állapota: {}".format(hazSzin))
print("Egy lehetséges festési szín: {}".format(joHazSzin))

# 6. feladat
print("6. feladat")
fileKi = open("utcakep.txt", "w")
utcaszin = ""
utcaszam = ""
for haz in ptlanok:
	szamhossz = haz.hossz - len(str(haz.hazszam)) 
	utcaszin += haz.szin * haz.hossz 
	utcaszam += str(haz.hazszam) + " " * (szamhossz)
fileKi.writelines(utcaszin)
fileKi.writelines("\n")
fileKi.writelines(utcaszam)
fileKi.flush()
fileKi.close()