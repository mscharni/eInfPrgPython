### Emelt Informatika Érettségi - 2014 Október - Nézőtér

nezoter = []
kategoria = []
maxSor = 15
maxHely = 20

# 1. feladat: Olvassa be és tárolja el a foglaltsag.txt és a kategoria.txt fájl adatait!
print("\n1. feladat")
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

# 2. feladat: Kérje be a felhasználótól egy sor, és azon belül egy szék számát, majd írassa ki a képernyőre, hogy az adott hely még szabad-e vagy már foglalt!
print("\n2. feladat")
sorSz = int(input("Sor száma [1..{}] :".format(maxSor)))
helySz = int(input("Hely száma [1..{}] :".format(maxHely)))
allapot = ""
if nezoter[sorSz-1][helySz-1] == "x":
    allapot = "foglalt"
else:
    allapot = "szabad"
print(f"A(z) {sorSz}. sor {helySz}. helye {allapot}.")

# 3. feladat: Határozza meg, hogy hány jegyet adtak el eddig, és ez a nézőtér befogadóképességének hány százaléka!
#   A százalékértéket kerekítse egészre, és az eredményt a következő formában írassa ki a képernyőre:
#   Például:
#   Az előadásra eddig 156 jegyet adtak el, ez a nézőtér 42%-a.
print("\n3. feladat")
szabadok = 0
for sor in range(0,maxSor):
    for hely in range(0,maxHely):
        if nezoter[sor][hely] == "x":
            szabadok += 1
print(f"Az előadásra eddig {szabadok} jegyet adtak el, ez a nézőtér {szabadok/(maxSor*maxHely):.2%}-a.")

# 4. feladat: Határozza meg, hogy melyik árkategóriában adták el a legtöbb jegyet!
#   Az eredményt írassa ki a képernyőre az alábbi formában:
#   Például:
#   A legtöbb jegyet a(z) 3. árkategóriában értékesítették.
print("\n4. feladat")
kategoriaSzum = [0,0,0,0,0,0]
for sor in range(0,maxSor):
    for hely in range(0,maxHely):
        if nezoter[sor][hely] == "x":
            kategoriaSzum[kategoria[sor][hely]] += 1
maxI = 0
for i in range(0,6):
    if kategoriaSzum[maxI] < kategoriaSzum[i]:
        maxI = i
print(f"A legtöbb jegyet a(z) {maxI}. árkategóriában értékesítették.")

# 5. feladat: Mennyi lenne a színház bevétele a pillanatnyilag eladott jegyek alapján?
print("\n5. feladat")
kategoriaSzum = [0,0,0,0,0,0]
kategoriaAr = [0,5000,4000,3000,2000,1500]
for sor in range(0,maxSor):
    for hely in range(0,maxHely):
        if nezoter[sor][hely] == "x":
            kategoriaSzum[kategoria[sor][hely]] += kategoriaAr[kategoria[sor][hely]]
osszesBevetel = 0
for i in range(0,6):
    osszesBevetel += kategoriaSzum[i]
print(f"A teljes bevétel: {osszesBevetel} Ft.")

# 6. feladat: Mivel az emberek általában nem egyedül mennek színházba, ha egy üres hely mellett nincs egy másik üres hely is, akkor azt nehezebben lehet értékesíteni.
#   Határozza meg, és írassa ki a képernyőre, hogy hány ilyen „egyedülálló” üres hely van a nézőtéren!
print("\n6. feladat")
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

# 7. feladat: A színház elektronikus eladási rendszere az érdeklődőknek az üres helyek esetén a hely árkategóriáját jeleníti meg, míg a foglalt helyeket csak egy „x” karakterrel jelzi.
#   Készítse el ennek megfelelően a fenti adatokat tartalmazó szabad.txt fájlt!
print("\n7. feladat")
with open("szabad.txt", "w") as fileKi:
    for sor in range(0,maxSor):
        for hely in range(0,maxHely):
            if nezoter[sor][hely] == "o":
                fileKi.write(str(kategoria[sor][hely]))
            else:
                fileKi.write("x")
        fileKi.write("\n")
print("Adatok kiirása az állományba kész.")
