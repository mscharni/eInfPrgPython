table = []
sectors = [[0 for n in range(0, 9)] for m in range(0, 9)]   # fill with zeros
steps = []

# 1. Olvassa be egy fájl nevét, egy sor és egy oszlop sorszámát (1 és 9 közötti számot)!
# A későbbi feladatokat ezen értékek felhasználásával kell megoldania!
print("\n1. feladat")
filename = input("Adja meg a bemeneti fájl nevét! (pl: konnyu.txt) = ")
row = int(input("Adja meg egy sor számát! = "))
col = int(input("Adja meg egy oszlop számát! = "))

# 2. Az előző feladatban beolvasott névnek megfelelő fájl tartalmát olvassa be, és tárolja el a táblázat adatait!
# Ha ezt nem tudja megtenni, akkor használja forrásként a rendelkezésre álló állományok egyikét!
print("\n2. feladat")
with open(filename) as file:
    for i in range(0, 9):
        # egy sor beolvasása
        line = file.readline()
        # egy sor feldarabolása
        row_datas = line.split()
        # sor letárolása a táblában
        table.append(row_datas)
        # a sor elemeinek letárolása a megfelelő szektorban (résztáblázatban)
        for j in range(0,9):
            cell = row_datas[j]
            sector = (i // 3)*3 + (j // 3)
            sectors[sector][(i % 3)*3 + j % 3] = cell
    # játékos lehetséges kitöltési lépéseinek letárolása
    for line in file:
        steps.append(line.split())

# print("table:")
# for i in range(0,9):
#     print(table[i])
# print("sectors:")
# for i in range(0,9):
#     print(sectors[i])
# print(f"steps_ {steps}")

# 3. Írja ki a képernyőre, hogy a beolvasott sor és oszlop értékének megfelelő hely…
# a. milyen értéket tartalmaz! Ha az adott helyen a 0 olvasható, akkor az „Az adott helyet még nem töltötték ki.” szöveget jelenítse meg!
# b. melyik résztáblázathoz tartozik!
print("\n3. feladat")
cell_value = table[row-1][col-1]
cell_sector = ((row-1) // 3)*3 + ((col-1) // 3) + 1
if cell_value == '0':
    print("„Az adott helyet még nem töltötték ki.")
else:
    print(f"Az adott helyen szereplő szám: {cell_value}")
print(f"A hely a(z) {cell_sector} résztáblázathoz tartozik.")

# 4. Határozza meg a táblázat hány százaléka nincs még kitöltve! Az eredményt egy tizedesjegy pontossággal jelenítse meg a képernyőn!
print("\n4. feladat")
zeros = 0
for i in range(0, 9):
    for j in range(0, 9):
        if table[i][j] == '0':
            zeros += 1
print(f"Az üres helyek aránya: {zeros/81:.1%} ")

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
print("\n5. feladat")
for step in steps:
    t_val = step[0]
    t_row = int(step[1])
    t_col = int(step[2])
    t_sector = ((t_row - 1) // 3) * 3 + ((t_col - 1) // 3)
    print(f"A kiválasztott sor: {t_row} oszlop: {t_col} a szám: {t_val}")
    if table[t_row-1][t_col-1] != '0':
        print("A helyet már kitöltötték.")
    elif t_val in table[t_row-1]:
        print("Az adott sorban már szerepel a szám.")
    else:
        # oszlopbeli előfordulás vizsgálata
        in_col = False
        for i in range(0,9):
            if table[i][t_col-1] == t_val:
                in_col = True
        if in_col:
            print("Az adott oszlopban már szerepel a szám.")
        else:
            # szektorbeli előfordulás vizsgálata

            if t_val in sectors[t_sector] :
                print("Az adott résztáblázatban már szerepel a szám.")
            else:
                print("A lépés megtehető.")
    print()

