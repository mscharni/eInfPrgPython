### Emelt Informatika Érettségi - 2015 Október - Fej vagy írás

import random

dobas = ""
# 1. feladat: Szimuláljon egy pénzfeldobást, ahol azonos esélye van a fejnek és az írásnak is!
#   Az eredményt írassa ki a képernyőre a mintának megfelelően!
print("\n1. feladat:")
veletlen = random.randint(0,1)
if veletlen == 0:
    dobas = "I"
else:
    dobas = "F"        
print(f"A pénzfeldobás eredménye: {dobas}")

# 2. feladat: Kérjen be a felhasználótól egy tippet, majd szimuláljon egy pénzfeldobást!
#   Írassa ki a képernyőre a felhasználó tippjét és a dobás eredményét is, majd tájékoztassa a felhasználót az eredményről következő formában:
#   „Ön eltalálta.” vagy „Ön nem találta el.”!
print("\n2. feladat:")
tipp = input("Tippeljen! (F/I) = ")
veletlen = random.randint(0,1)
if veletlen == 0:
    dobas = "I"
else:
    dobas = "F"        
print(f"A tipp {tipp}, a dobás eredménye {dobas} volt.")
if tipp == dobas:
    print("Ön eltalálta!")
else:
    print("Ön nem találta el!")

# 3. feladat: Állapítsa meg, hány dobásból állt a kísérlet, és a választ a mintának megfelelően írassa ki a képernyőre!
print("\n3. feladat:")
dobasDb = 0         # összes dobás száma
fejDb = 0           # Összes fej száma
aktFejDb = 0        # aktuális fej-sorozat hossza
buffer =""          # aktuálisan négy egymást követő dobás
ketFej = "IFFI"     # pontosan kétfejű
ketFejDb = 0        # pontosan kétfejűek száma
maxFejDb = 0        # maximális fej-sorozat hossza
maxFejIdx = 0       # maximális fej-sorozat utáni I indexe

with open("kiserlet.txt", "r") as fileBe:
    # első négy sor (első négyes) beolvasása
    for i in range(0,4):
        sor = fileBe.readline().strip()
        buffer += sor
        dobasDb += 1
        if sor == "F":
            fejDb += 1
            aktFejDb +=1
        if sor == "I":
            if aktFejDb > maxFejDb:
                maxFejDb = aktFejDb
                maxFejIdx = dobasDb
            aktFejDb = 0

    if buffer == ketFej:
        ketFejDb += 1
    # többi sor beolvasása
    for sor in fileBe:
        sor = sor.strip()
        buffer = buffer[1:4] + sor
        dobasDb += 1
        if sor == "F":
            fejDb += 1
            aktFejDb += 1
        if buffer == ketFej:
            ketFejDb += 1
        if sor == "I":
            if aktFejDb > maxFejDb:
                maxFejDb = aktFejDb
                maxFejIdx = dobasDb
            aktFejDb = 0
print(f"A kísérlet {dobasDb} dobásból állt")

# 4. feladat: Milyen relatív gyakorisággal dobtunk a kísérlet során fejet?
#   (A fej relatív gyakorisága a fejet eredményező dobások és az összes dobás hányadosa.)
#   A relatív gyakoriságot a mintának megfelelően két tizedesjegy pontossággal, százalék formátumban írassa ki a képernyőre!
print("\n4. feladat")
gyakorisag = 100*fejDb/dobasDb
print(f"A kísérlet során a fej relatív gyakorisága {gyakorisag:.2f}%% volt.")

# 5. feladat: Hányszor fordult elő ebben a kísérletben, hogy egymás után pontosan két fejet dobtunk?
#   A választ a mintának megfelelően írassa ki a képernyőre! (Feltételezheti, hogy a kísérlet legalább 3 dobásból állt.)
print("\n5. feladat")
print(f"A kísérlet során {ketFejDb} alkalommal dobtak pontosan két fejet egymás után")

# 6. feladat: Milyen hosszú volt a leghosszabb, csak fejekből álló részsorozat?
#   Írassa ki a választ a képernyőre a mintának megfelelően, és adja meg egy ilyen részsorozat első tagjának helyét is! (A minta tagjainak számozását eggyel kezdjük.)
print("\n6. feladat")
print(f"A leghosszabb tisztafej sorozat {maxFejDb} tagból állt, kezdete a(z) {maxFejIdx-maxFejDb}. dobás")

# 7. feladat: Állítson elő és tároljon a memóriában 1000 db négy dobásból álló sorozatot!
#   Számolja meg, hogy hány esetben követett egy háromtagú „tisztafej” sorozatot fej, illetve hány esetben írás!
#   Az eredményt írassa ki a dobasok.txt állományba úgy, hogy az első sorba kerüljön az eredmény, a második sorban pedig egy-egy szóközzel elválasztva, egyetlen sorban szerepeljenek a dobássorozatok!
print("\n7. feladat:")
FI = "FI"
dobasok = []
FFFF = 0
FFFI = 0
for i in range(0,1000):
    dobas = ""
    for j in range(0,4):
        veletlen = random.randint(0,1)
        dobas += FI[veletlen]
    dobasok.append(dobas)
    if dobas == "FFFF":
        FFFF += 1
    if dobas == "FFFI":
        FFFI += 1

with open("dobasok.txt", "w") as fileKi:
    fileKi.write("FFFF: {}, FFFI: {}\n".format(FFFF,FFFI))
    for dobas in dobasok:
        fileKi.write(dobas + " ")
print("Adatok kiírva a 'dobasok.txt' állományba.")
