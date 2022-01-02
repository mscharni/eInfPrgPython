import math

class Program():
    def __init__(self, idx, line):
        self.sorszam = idx
        self.program = line.strip()
        self.program_rovid = self.program.replace("ED", "").replace("DE", "").replace("KN", "").replace("NK", "")
        self.program_uj = self.get_uj_program()
        self.egyszerusitheto = (self.program != self.program_rovid)
        self.tav_ED = list(self.program_rovid).count("E")-list(self.program_rovid).count("D")
        self.tav_KN = list(self.program_rovid).count("K") - list(self.program_rovid).count("N")
        self.get_max_tav()
        self.energia = self.get_energia()

    def get_program_arrows(self, prg):
        return prg.replace("E", "↑").replace("D", "↓").replace("K", "→").replace("N", "←")

    def get_max_tav(self):
        max_tav = 0
        tav_x = 0
        tav_y = 0
        prg = self.program
        for i in range(0, len(prg)):
            if prg[i] == "E":
                tav_y +=1
            elif prg[i] == "D":
                tav_y -=1
            elif prg[i] == "K":
                tav_x +=1
            else:
                tav_x -= 1
            tav = math.sqrt(tav_x**2 + tav_y**2)
            if tav > max_tav:
                max_tav = tav
        self.max_tav_lepes = i + 1
        self.max_tav_ertek = max_tav

    def get_energia(self):
        prg = self.program
        energ = 2 + len(prg)   # induláskori 2 és minden lépés 1
        lep = prg[0]
        for i in range(1, len(prg)):
            if prg[i] != lep:   # irányváltás, ha az előző lépésbeli iránytól eltér
                energ += 2
            lep = prg[i]        # lépés -> előző lépés
        return energ

    def get_uj_program(self):
        prg = self.program
        prg_uj = ""
        lep = prg[0]
        lep_sor = lep
        for i in range(1, len(prg)):
            if prg[i] == lep:           # azonos betű
                lep_sor += prg[i]
            else:                       # eltérő betű: változás
                if len(lep_sor) > 1:    # ki kell írni a darabszámot
                    prg_uj += str(len(lep_sor))
                prg_uj += lep_sor[0]    # és a karaktert
                lep_sor = prg[i]        # újraindítjuk a lépéssorozatot
            lep = prg[i]
        # az utolsó karakter(sor kezelése
        if len(lep_sor) >1:
            prg_uj += str(len(lep_sor))
        prg_uj += lep_sor[0]  # és a karaktert
        return prg_uj

programok = []
# 1. Olvassa be a program.txt állományban talált adatokat, s azok felhasználásával oldja meg a következő feladatokat!
#   Ha az állományt nem tudja beolvasni, az állomány első 10 sorának adatait jegyezze be a programba és dolgozzon azzal!
print("\n1. feladat")
idx = 0
with open("program.txt") as fileBe:
    fileBe.readline()       # az első sorban lévő adatot nem használjuk fel
    for line in fileBe:
        idx += 1
        program = Program(idx, line)
        programok.append(program)
print("Adatok beolvasva a 'program.txt' állományból")

# 2. Kérje be egy utasítássor számát, majd írja a képernyőre, hogy:
#   a. Egyszerűsíthető-e az utasítássorozat! Az egyszerűsíthető, illetve nem egyszerűsíthető választ írja a képernyőre!
#       (Egy utasítássort egyszerűsíthetőnek nevezünk, ha van benne két szomszédos, ellentétes irányt kifejező utasításpár, hiszen ezek a párok  elhagyhatók.
#       Ilyen ellentétes utasításpár az ED, DE, KN, NK.)
#   b. Az utasítássor végrehajtását követően legkevesebb mennyi E vagy D és K vagy N utasítással lehetne a robotot a kiindulási pontba visszajuttatni!
#       A választ a következő formában jelenítse meg: 3 lépést kell tenni az ED, 4 lépést a KN tengely mentén.
#   c. Annak végrehajtása során hányadik lépést követően került (légvonalban) legtávolabb a robot a kiindulási ponttól és mekkora volt ez a távolság!
#       A távolságot a lépés sorszámát követően 3 tizedes pontossággal írja a képernyőre!
print("\n2. feladat")
idx = int(input("Program sorszáma = "))
program = programok[idx-1]
# a.,
if program.egyszerusitheto:
    print("Egyszerűsíthető")
else:
    print("Nem egyszerűsíthető")
# b.,
print(f"{abs(program.tav_ED)} lépést kell tenni az ED, {abs(program.tav_KN)} lépést a KN tengely mentén")

# c.,
print(f"{program.max_tav_lepes}. lépésben {program.max_tav_ertek:.3f} a legnagyobb távolság.")

# 3. A robot a mozgáshoz szükséges energiát egy beépített akkuból nyeri.
#   A robot 1 centiméternyi távolság megtételéhez 1 egység, az irányváltásokhoz és az induláshoz 2 egység energiát használ.
#   Ennek alapján az EKK utasítássor végrehajtásához 7 egység energia szükséges.
#   A szakkörön használt teljesen feltöltött kis kapacitású akkuból 100, a nagykapacitásúból 1000 egységnyi energia nyerhető ki.
#   Adja meg azon utasítássorokat, amelyek végrehajtásához a teljesen feltöltött kis kapacitású akku is elegendő!
#   Írja a képernyőre egymástól szóközzel elválasztva az utasítássor sorszámát és a szükséges energia mennyiségét!
#   Minden érintett utasítássor külön sorba kerüljön!
print("\n3. feladat")
for program in programok:
    if program.energia <= 100:
        print(f"{program.sorszam} {program.energia}")

# 4. Gáborék továbbfejlesztették az utasításokat értelmező programot.
#   Az új, jelenleg még tesztelés alatt álló változatban a több, változatlan irányban tett elmozdulást helyettesítjük az adott irányban tett elmozdulások számával és az irány betűjével.
#   Tehát például a DDDKDD utasítássor leírható rövidített 3DK2D formában is.
#   Az önállóan álló utasításnál az 1-es számot nem szabad kiírni!
#   Hozza létre az ujprog.txt állományt, amely a program.txt állományban foglalt utasítássorozatokat az új formára alakítja úgy, hogy az egymást követő azonos utasításokat minden esetben a rövidített alakra cseréli!
#   Az ujprog.txt állományba soronként egy utasítássor kerüljön, a sorok ne tartalmazzanak szóközt!
print("\n4. feladat")
with open("ujprog.txt", "w") as fileKi:
    for program in programok:
        fileKi.writelines(f"{program.program_uj}\n")
print("Adatok kiírva a 'ujprog.txt' állományba")

# 5. Sajnos a tesztek rámutattak arra, hogy a program új verziója még nem tökéletes, ezért vissza kell térni az utasítássorok leírásának régebbi változatához.
#   Mivel a szakkörösök nagyon bíztak az új változatban, ezért néhány utasítássort már csak ennek megfelelően készítettek el.
#   Segítsen ezeket visszaírni az eredeti formára! Az ismétlődések száma legfeljebb 200 lehet! Kérjen be egy új formátumú utasítássort, majd írja a képernyőre régi formában!
print("\n5. feladat")

# visszakonvertáló függvény (ez elhagyható, de a kiegészítő feladat miatt praktikus)
def convert_to_old(prg):
    chars = ["E", "K", "D", "N"]
    digits = [str(n) for n in range(0,10)]
    uj_prg = list(prg)
    regi_prg = ""
    prev_char = uj_prg[0]
    # kezdő karakter kezelése
    if prev_char in digits:
        db = prev_char          # számmal kezdődik: le kell tárolni a számot
    else:
        regi_prg = prev_char    # betűvel kezdődik:  régi program első karaktere
        db = "1"                # egy darab van belőle
    # végigmegyünk az összes többi karakteren
    for idx in range(1, len(uj_prg)):
        char = uj_prg[idx]
        # ha irány-karakter
        if char in chars:
            regi = "".join([char * int(db)])
            regi_prg += regi
            db = "1"
        elif char in digits:
            # ha szám, akkor az előző szám volt-e (többjegyű számok kezelése)
            if prev_char in digits:
                db += char
            else:
                db = char
        else:
            print("hibás rövidítés: érvénytelen karakter!")
        prev_char = char
    return regi_prg

uj_prg = input("Új formátumú utasítássor = ").upper()
regi_prog = convert_to_old(uj_prg)
print(f"Régi formátumú utasítássor: {regi_prog}")

# tesztelési célokból visszakonvertáljuk az 'ujprog.txt' állományban lévő programokat: vissze kell kapnunk a program.txt-beli formát
print("\n5. feladat: visszakonvertálás ellenőrző tesztje (nem része az érettséginek)")
with open("ujprog.txt", "r") as fileBe:
    idx = 0
    for line in fileBe:
        uj_prg = line.strip()
        regi_prog = convert_to_old(uj_prg)
        jo_e = regi_prog == programok[idx].program
        if jo_e:
            print(f"{idx + 1:2}. program helyes")
        else:
            print(f"{idx + 1:2}. program hibás")
            print(f"{idx + 1:2}. konvert = {regi_prog}")
            print(f"{idx + 1:2}. eredeti = {programok[idx].program}")
        idx += 1