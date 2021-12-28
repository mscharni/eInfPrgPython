nezoter = []
kategoria = []
maxSor = 15
maxHely = 20

# 1. feladat
print("1. feladat")
fileBe1 = open("foglaltsag.txt", "r")
fileBe2 = open("kategoria.txt", "r")
for sor in range(0,maxSor):
    sorAdat1 = fileBe1.readline().strip()
    sorAdat2 = fileBe2.readline().strip()
    nezoterSor = []
    kategoriaSor = []
    for hely in range(0,maxHely):
        nezoterSor.append(sorAdat1[hely])
        kategoriaSor.append(int(sorAdat2[hely]))
    nezoter.append(nezoterSor)
    kategoria.append(kategoriaSor)
fileBe1.close()
fileBe2.close()
print("Adatok beolvasva.")

# 2. feladat
print("2. feladat")
sorSz = int(input("Sor száma [1..{}] :".format(maxSor)))
helySz = int(input("Hely száma [1..{}] :".format(maxHely)))
allapot = ""
if nezoter[sorSz-1][helySz-1] == "x":
    allapot = "foglalt"
else:
    allapot = "szabad"
print("A(z) {}. sor {}. helye {}.".format(sorSz, helySz, allapot))

# 3. feladat
print("3. feladat")
szabadok = 0
for sor in range(0,maxSor):
    for hely in range(0,maxHely):
        if nezoter[sor][hely] == "x":
            szabadok += 1
print("Az előadásra eddig {} jegyet adtak el, ez a nézőtér {}%-a.".format(szabadok,round(100*szabadok/(maxSor*maxHely))))       

# 4. feladat
print("4. feladat")
kategoriaSzum = [0,0,0,0,0,0]
for sor in range(0,maxSor):
    for hely in range(0,maxHely):
        if nezoter[sor][hely] == "x":
            kategoriaSzum[kategoria[sor][hely]] += 1
maxI = 0
for i in range(0,6):
    if kategoriaSzum[maxI] < kategoriaSzum[i]:
        maxI = i
print("A legtöbb jegyet a(z) {}. árkategóriában értékesítették.".format(maxI))

# 5. feladat
print("5. feladat")
kategoriaSzum = [0,0,0,0,0,0]
kategoriaAr = [0,5000,4000,3000,2000,1500]
for sor in range(0,maxSor):
    for hely in range(0,maxHely):
        if nezoter[sor][hely] == "x":
            kategoriaSzum[kategoria[sor][hely]] += kategoriaAr[kategoria[sor][hely]]
            print(sor,hely,nezoter[sor][hely], kategoria[sor][hely], kategoriaAr[kategoria[sor][hely]])
        else:
            print(sor,hely,nezoter[sor][hely], kategoria[sor][hely],"----")
    print()
osszesBevetel = 0
for i in range(0,6):
    osszesBevetel += kategoriaSzum[i]
print("A teljes bevétel: {} Ft.".format(osszesBevetel))

# 6. feladat
print("6. feladat")
egyedulHely = 0
for sor in range(0,maxSor):
    # bal szél
    if nezoter[sor][0] == "o" and nezoter[sor][1] == "x":
        egyedulHely += 1
    # teljes közép
    for hely in range(1,maxHely-1):
        if nezoter[sor][hely-1] == "x" and nezoter[sor][hely] == "o" and nezoter[sor][hely+1] == "x":
            egyedulHely += 1
    # jobb szél
    if nezoter[sor][maxHely-2] == "x" and nezoter[sor][maxHely-1] == "o":
        egyedulHely += 1
print("{} egyedülálló hely van.".format(egyedulHely))

# 7. feladat
print("7. feladat")
fileKi = open("szabad.txt", "w")
for sor in range(0,maxSor):
    for hely in range(0,maxHely):
        if nezoter[sor][hely] == "o":
            fileKi.write(str(kategoria[sor][hely]))
        else:
            fileKi.write("x")
    fileKi.write("\n")
fileKi.flush()
fileKi.close()
print("Adatok kiirása az állományba kész.")
