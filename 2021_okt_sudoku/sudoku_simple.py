### Emelt Informatika Érettségi - 2021 Október - Sudoku

# visszaadja, hogy az x,y koordinátájú elem melyik résztáblába tartozik
def get_resz(x,y):
    resz = (x // 3)*3 + (y // 3)
    return resz

# az r sorszámú résztábla kilenc elemét adja vissza egy listában
def get_resztabla(r):
    resz_tabla = []
    rx = r // 3     # résztábla sora
    ry = r % 3      # résztábla oszlopa
    # három különböző sor
    for x in range(0,3):
        # három oszlopnyi elem
        elem_sor = tabla[3*rx + x][3*ry: 3*ry + 3]
        resz_tabla.extend(elem_sor)
    return resz_tabla

# sudoku tábla egy 9*9-es 2 dimenziós tömbben (nested list)
tabla = []
# lepesek egy n*3-es 2 dimenziós tömbben (nested list)
lepesek = []


# 1. Olvassa be egy fájl nevét, egy sor és egy oszlop sorszámát (1 és 9 közötti számot)!
# A későbbi feladatokat ezen értékek felhasználásával kell megoldania!
print("\n1.feladat")
filename = input("Állomány neve = ")
# filename = "kozepes.txt"
row = int(input("Sor = "))-1
col = int(input("Oszlop = "))-1


# 2. Az előző feladatban beolvasott névnek megfelelő fájl tartalmát olvassa be, és tárolja el a táblázat adatait!
print("\n2.feladat")
with open(filename, "r") as fileBe:
    # elso kilenc sor beolvasasa
    for i in range(0,9):
        # a sort egyből feldaraboljuk: karaktereket tartalmazó listává
        sor = fileBe.readline().strip().split(" ")
        # és hozzáfűzzük a tömbhöz
        tabla.append(sor)
    # a maradék sor kiolvasása (az állomány végéig)
    while True:
        line = fileBe.readline()
        # ha nem üres stringet olvasunk ki
        if line != "":
            datas = line.strip().split(" ")
            lepesek.append([datas[0], int(datas[1]), int(datas[2])])
        else:
            # vége az állománynak, kilépünk a ciklusból
            break
print("Adatok beolvasva")


# 3. Írja ki a képernyőre, hogy a beolvasott sor és oszlop értékének megfelelő hely…
# a. milyen értéket tartalmaz! Ha az adott helyen a 0 olvasható, akkor az „Az adott helyet még nem töltötték ki.” szöveget jelenítse meg!
# b. melyik résztáblázathoz tartozik!
print("\n3.feladat")
if tabla[row][col] != "0":
    print(f"a) Érték = {tabla[row][col]}")
else:
    print("a) Az adott helyet még nem töltötték ki.")
print(f"b) Résztábla = {get_resz(row,col)+1}")


# 4. Határozza meg a táblázat hány százaléka nincs még kitöltve! Az eredményt egy tizedesjegy pontossággal jelenítse meg a képernyőn!
print("\n4.feladat")
ossz = len(tabla)*len(tabla[0])
zerok = 0
# minden sor egy lista, amelyben megszámoljuk, hány nulla van
for i in range(0,len(tabla)):
    zerok += tabla[i].count("0")
print(f"{zerok/ossz:.1%}")


# 5. Vizsgálja meg, hogy a fájlban szereplő lépések lehetségesek-e a beolvasott táblázaton!
# Tekintse mindegyiket úgy, mintha az lenne az egyetlen lépés az eredeti táblázaton, de ne hajtsa azt végre!
# Állapítsa meg, hogy okoz-e valamilyen ellentmondást a lépés végrehajtása!
# Írja ki a lépéshez tartozó három értéket, majd a következő sorba írja az alábbi megállapítások egyikét!
# # Ha több megállapítás is igaz, elegendő csak egyet megjelenítenie.
# • „A helyet már kitöltötték”
# • „Az adott sorban már szerepel a szám”
# • „Az adott oszlopban már szerepel a szám”
# • „Az adott résztáblázatban már szerepel a szám”
# • „A lépés megtehető”
print("\n5.feladat")
for i in range(0, len(lepesek)):
    szam = lepesek[i][0]
    row  = lepesek[i][1]-1
    col  = lepesek[i][2]-1
    if tabla[row][col] != "0" :
        print("A helyet már kitöltötték")
    elif szam in tabla[row]:
        print("Az adott sorban már szerepel a szám")
    elif szam in [tabla[i][col] for i in range(0,9)]:
        print("Az adott oszlopban már szerepel a szám")
    elif szam in get_resztabla(get_resz(row,col)):
        print("Az adott résztáblázatban már szerepel a szám")
    else:
        print("A lépés megtehető")


  


