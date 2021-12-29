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

# 1. feladat: Olvassa be és tárolja el a kerites.txt fájl tartalmát!
print("\n1. feladat")
with open("kerites.txt", "r") as fileBe:
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
print("Adatok beolvasva a 'kerites.txt' állományból")

# 2. feladat: Írja a képernyőre, hogy hány telket adtak el az utcában!
print("\n2. feladat")
print("Az eladott telkek száma: {}".format(len(hazak)))

# 3. feladat: Jelenítse meg a képernyőn, hogy az utolsó eladott telek
#   a. melyik (páros / páratlan) oldalon talált gazdára!
#   b. milyen házszámot kapott!
print("\n3. feladat")
if hazak[-1].oldal == 0:
     oldal = "páros"
else :
    oldal = "páratlan"
print(f"A {oldal} oldalon adták el az utolsó telket.")
print(f"Az utolsó telek házszáma: {hazak[-1].hazszam}")

# 4. feladat: Írjon a képernyőre egy házszámot a páratlan oldalról, amely melletti telken ugyanolyan színű a kerítés!
#   (A hiányzó és a festetlen kerítésnek nincs színe.)
#   Feltételezheti, hogy van ilyen telek, a több ilyen közül elég az egyik ház számát megjeleníteni.
print("\n4. feladat")
i = 1
# bennmaradási feltétel: nem egyező színek vagy nem szín 
while (ptlanok[i].szin != ptlanok[i-1].szin) or ("#:".find(ptlanok[i].szin) != -1):
    i += 1
print(f"A szomszédossal egyezik a kerítés színe: {ptlanok[i].hazszam}")

# 5. feladat: Kérje be a felhasználótól egy eladott telek házszámát, majd azt felhasználva oldja meg a következő feladatokat!
#   a. Írja ki a házszámhoz tartozó kerítés színét, ha már elkészült és befestették,egyébként az állapotát a „#” vagy „:” karakter jelöli!
#   b. A házszámhoz tartozó kerítést szeretné tulajdonosa be- vagy átfesteni.
#       Olyan színt akar választani, amely különbözik a mellette lévő szomszéd(ok)tól és a jelenlegi színtől is.
#       Adjon meg egy lehetséges színt! A színt a teljes palettából (A–Z) szabadon választhatja meg.
print("\n5. feladat")
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
hazSzin = utca[i].szin
# derítsük ki, milyen színek nem lehetnek pl: "ABC"
nemJoSzin = "" + utca[i-1].szin  + utca[i].szin + utca[i+1].szin
# keresünk egy színt
j = 0
while nemJoSzin.find(szinek[j]) != -1 :
	j += 1

joHazSzin = szinek[j]

print(f"A kerítés színe / állapota: {hazSzin}")
print(f"Egy lehetséges festési szín: {joHazSzin}")

# 6. feladat: Jelenítse meg az utcakep.txt fájlban a páratlan oldal utcaképét a mintának megfelelően!
print("\n6. feladat")
with open("utcakep.txt", "w") as fileKi:
    utcaszin = ""
    utcaszam = ""
    for haz in ptlanok:
        szamhossz = haz.hossz - len(str(haz.hazszam))       # a ház hosszából le kell vonni a házszám karaktereinek számát
        utcaszin += haz.szin * haz.hossz
        utcaszam += str(haz.hazszam) + " " * (szamhossz)    # a számhossznak megfelelő számú szóköz előállítása
    fileKi.writelines(utcaszin)
    fileKi.writelines("\n")
    fileKi.writelines(utcaszam)
print("Adatok kiírva az 'utcakep.txt' állományba")