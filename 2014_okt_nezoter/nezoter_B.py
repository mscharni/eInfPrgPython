### Emelt Informatika Érettségi - 2014 Október - Nézőtér

nezoter = []
kategoria = []
maxSor = 15
maxHely = 20
kategoriaSzum = [0,0,0,0,0,0]
kategoriaErtek = [0,0,0,0,0,0]
kategoriaAr = [0,5000,4000,3000,2000,1500]
# 1. feladat
print("1. feladat")
fileBe1 = open("foglaltsag.txt", "r")
fileBe2 = open("kategoria.txt", "r")
fileKi = open("szabad2.txt", "w")
fileKi1 = open("foglaltsag.csv", "w")
fileKi2 = open("kategoria.csv", "w")
szabadok = 0
for sor in range(0,maxSor):
    sorAdat1 = fileBe1.readline().strip()
    sorAdat2 = fileBe2.readline().strip()
    nezoterSor = []
    kategoriaSor = []
    for hely in range(0,maxHely):
        nezoterSor.append(sorAdat1[hely])
        kategoriaSor.append(int(sorAdat2[hely]))
        # előfeldolgozás
        if sorAdat1[hely] == "x":
            # 3. feladat
            szabadok += 1       
            # 4. feladat
            kategoriaSzum[int(sorAdat2[hely])] += 1
            # 5. feladat
            kategoriaErtek[int(sorAdat2[hely])] += kategoriaAr[int(sorAdat2[hely])]
            # 7. feladat
            fileKi.write("x")
        else:
            fileKi.write(sorAdat2[hely])
        fileKi1.write(sorAdat1[hely]+",")
        fileKi2.write(sorAdat2[hely]+",")
    nezoter.append(nezoterSor)
    kategoria.append(kategoriaSor)
    fileKi.write("\n")    
    fileKi1.write("\n")
    fileKi2.write("\n")
fileKi.flush()
fileKi.close()
fileKi1.flush()
fileKi1.close()
fileKi2.flush()
fileKi2.close()

fileBe2.close()
fileBe1.close()
print("Adatok beolvasva feldolgozva és kiratva.")

# 2. feladat
print("2. feladat")
sorSz = int(input(f"Sor száma [1..{maxSor}] :"))
helySz = int(input(f"Hely száma [1..{maxHely}] :"))
allapot = ""
if nezoter[sorSz-1][helySz-1] == "x":
    allapot = "foglalt"
else:
    allapot = "szabad"
print(f"A(z) {sorSz}. sor {helySz}. helye {allapot}.")

# 3. feladat
print("3. feladat")
print(f"Az előadásra eddig {szabadok} jegyet adtak el, ez a nézőtér {szabadok/(maxSor*maxHely):.2%}%-a.")

# 4. feladat
print("4. feladat")
maxI = 0
for i in range(0,6):
    if kategoriaSzum[maxI] < kategoriaSzum[i]:
        maxI = i
print(f"A legtöbb jegyet a(z) {maxI}. árkategóriában értékesítették.")

# 5. feladat
print("5. feladat")
osszesBevetel = 0
for i in range(0,6):
    osszesBevetel += kategoriaErtek[i]
print(f"A teljes bevétel: {osszesBevetel} Ft.")

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
print(f"{egyedulHely} egyedülálló hely van.")


