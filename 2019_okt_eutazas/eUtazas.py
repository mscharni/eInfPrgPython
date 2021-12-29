class Utas:
    def __init__(self,s):
        self.megallo = int(s[0])
        self.datumIdo = s[1]
        self.datum = s[1][0:8]
        self.ido = s[1][9:4]
        self.kID = s[2]
        self.tipus = s[3]
        if self.tipus == "JGY":
            self.jE = True
            self.jDb = int(s[4])
            self.erv = True if self.jDb > 0 else False
        else :    
            self.jE = False
            self.eDatum = s[4]
            self.erv = True if self.datum <= self.eDatum else False

utasok=[]

# 1. feladat: Olvassa be és tárolja el az utasadat.txt fájl tartalmát!
print("\n1. feladat")
with open("utasadat.txt", "r") as fileBe:
    for sor in fileBe.readlines():
        utas = Utas(sor.strip().split(" "))
        utasok.append(utas)
print("Adatok beolvasva az 'utasadat.txt' állományból")

# 2. feladat: Adja meg, hogy hány utas szeretett volna felszállni a buszra!
print("\n2. feladat")
print(f"A buszra {len(utasok)} utas akart felszállni")

# 3. feladat: A közlekedési társaság szeretné, ha a járművőn csak az érvényes jeggyel vagy bérlettel rendelkezők utaznának.
#   Ezért a jegyeket és bérleteket a buszvezető a felszálláskor ellenőrzi.
#   (A bérlet még érvényes a lejárat napján.)
#   Adja meg, hogy hány esetben kellett a buszvezetőnek elutasítania az utas felszállását, mert lejárt a bérlete vagy már nem volt jegye!
print("\n3. feladat")
nemErvDb = 0
for utas in utasok:
    if utas.erv != True:
        nemErvDb += 1
print(f"A buszra {nemErvDb} utas nem szállhatott fel")

# 4. feladat: Adja meg, hogy melyik megállóban próbált meg felszállni a legtöbb utas!
#   (Több azonos érték esetén a legkisebb sorszámút adja meg!)
print("\n4. feladat")
maxUtas = 0
maxMegallo = 0
aktMegallo = utasok[0].megallo
aktUtas =0
for utas in utasok:
    if utas.megallo == aktMegallo:
        aktUtas += 1
    else:
        if aktUtas > maxUtas:
            maxUtas = aktUtas
            maxMegallo = aktMegallo
        aktUtas = 1
        aktMegallo = utas.megallo
print(f"A legtöbb utas ({maxUtas} fő) a {maxMegallo}. megállóban próbált felszállni")

# 5. feladat: A közlekedési társaságnak kimutatást kell készítenie, hogy hányszor utaztak valamilyen kedvezménnyel a járművön.
#   Határozza meg, hogy hány kedvezményes és hány ingyenes utazó szállt fel a buszra! (Csak az érvényes bérlettel rendelkező szállhatott fel a buszra!)
print("\n5. feladat")
kedvDb = 0
ingyDb = 0
for utas in utasok:
    # nem jegy
    if utas.erv == True and utas.jE == False:
        if "TAB NYB".find(utas.tipus) > -1:
            kedvDb += 1
        if "NYP RVS GYK".find(utas.tipus) > -1:
            ingyDb += 1
print(f"Ingyenesen utazók száma: {ingyDb} fő")
print(f"A kedvezményesen utazók száma: {kedvDb} fő")

# 6. feladat: Készítsen függvényt napokszama néven a megadott algoritmus alapján.
#   Az algoritmus a paraméterként megadott két dátumhoz (év, hónap, nap) megadja a közöttük eltelt napok számát!
#   (A MOD a maradékos osztást, a DIV az egészrészes osztást jelöli.)
#   Az algoritmust a fuggveny.txt fájlban találja.
#   A függvényt a következő feladat megoldásához felhasználhatja.
print("\n6. feladat")
def napokszama(e1, h1, n1, e2, h2, n2):
	h1 = (h1 + 9) % 12
	e1 = e1 - h1 // 10
	d1= 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
	h2 = (h2 + 9) % 12
	e2 = e2 - h2 // 10
	d2= 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
	return d2-d1
print("Függvény kész")

# 7. feladat: A közlekedési társaság azoknak az utasoknak, akiknek még érvényes, de 3 napon belül lejár a bérlete, figyelmeztetést szeretne küldeni e-mailben.
#   (Például, ha a felszállás időpontja 2019. február 5., és a bérlet érvényessége 2019. február 8., akkor már kap az utas levelet,
#   ha 2019. február 9. az érvényessége, akkor még nem kap levelet.)
#   Válogassa ki és írja a figyelmeztetes.txt állományba ezen utasok kártyaazonosítóját és a bérlet érvényességi idejét (éééé-hh-nn formátumban) szóközzel elválasztva!
print("\n7. feladat")
with open("figyelmeztetes.txt", "w") as fileKi:
    for utas in utasok:
        if utas.erv == True and utas.jE == False:
            e1 = int(utas.datum[0:4])
            h1 = int(utas.datum[4:6])
            n1 = int(utas.datum[6:8])
            e2 = int(utas.eDatum[0:4])
            h2 = int(utas.eDatum[4:6])
            n2 = int(utas.eDatum[6:8])
            if napokszama(e1, h1, n1, e2, h2, n2) <=3:
                fileKi.writelines(f"{utas.kID} {e2}-{h2}-{n2}\n")
print("Adatok kiírva a 'figyelmeztetes.txt' állományba")