import random

dobas = ""
# 1. feladat
veletlen = random.randint(0,1)
if veletlen == 0:
    dobas = "I"
else:
    dobas = "F"        
print("A pénzfeldobás eredménye: {}".format(dobas))

# 2. feladat
tipp = input("Tippeljen! (F/I) = ")
veletlen = random.randint(0,1)
if veletlen == 0:
    dobas = "I"
else:
    dobas = "F"        
print("A tipp {}, a dobás eredménye {} volt.".format(tipp, dobas))
if tipp == dobas:
    print("Ön eltalálta!")
else:
    print("Ön nem találta el!")

# 3. feladat
fileBe = open("kiserlet.txt", "r")
dobasDb = 0         # összes dobás száma
fejDb = 0           # Összes fej száma
aktFejDb = 0        # aktuális fej-sorozat hossza
buffer =""          # aktuálisan négy egymást követő dobás
ketFej = "IFFI"     # pontosan kétfejű
ketFejDb = 0        # pontosan kétfejűek száma
maxFejDb = 0        # maximális fej-sorozat hossza
maxFejIdx = 0       # maximális fej-sorozat utáni I indexe
# első három beolvasása
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

fileBe.close()

# 3. feladat
print("3. feladat")
print("A kísérlet {} dobásból állt".format(dobasDb))

# 4. feladat
print("4. feladat")
gyakorisag = 100*fejDb/dobasDb
print("A kísérlet során a fej relatív gyakorisága {:.2f}%% volt.".format(gyakorisag))

# 5. feladat
print("5. feladat")
print("A kísérlet során {} alkalommal dobtak pontosan két fejet egymás után".format(ketFejDb))

# 6. feladat
print("6. feladat")
print("A leghosszabb tisztafej sorozat {} tagból állt, kezdete a(z) {}. dobás".format(maxFejDb, maxFejIdx-maxFejDb))

# 7. feladat
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

fileKi = open("dobasok.txt", "w")
fileKi.writelines("FFFF: {}, FFFI: {}\n".format(FFFF,FFFI))
for dobas in dobasok:
    fileKi.write(dobas + " ")
fileKi.flush()
fileKi.close()