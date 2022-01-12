### Emelt Informatika Érettségi - 2021 Október - Sudoku

# tábla osztály létrehozása
class Table():
    table = []

    def __init__(self, datas=[]):
        if datas != []:
            self.set_table(datas)

    def set_table(self, datas):
        for line in datas:
            self.table.append(line)

    def print_table(self):
        for i in range(0,9):
            s_row = ""
            for j in range(0,9):
                s_row += " " + self.table[i][j]
            print(f"{s_row}")

    def get_cell(self, row_index, col_index):
        return self.table[row_index-1][col_index-1]

    def get_sector_index(self, row_index, col_index):
        return  ((row_index-1) // 3)*3 + ((col_index-1) // 3) + 1

    def get_row(self, row_index):
        return self.table[row_index-1]

    def get_col(self, col_index):
        t_col = []
        for i in range(0,9):
            t_col.append(self.table[i][col_index-1])
        return t_col

    def get_sector(self, row_index, col_index):
        t_sector = []
        # szektor középső elemének pozíciója
        t_row = ((row_index-1) // 3)*3+1
        t_col = ((col_index-1) // 3)*3+1
        for i in range(-1,2):
            for j in range(-1,2):
                t_sector.append(self.table[t_row+i][t_col+j])
        return t_sector

    def get_empty_rate(self):
        zeros = 0
        for i in range(0, 9):
            for j in range(0, 9):
                if self.table[i][j] == '0':
                    zeros += 1
        return zeros/81

# Tábla létrehozása
table = Table()
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
with open(filename) as fileBe:
    datas = []
    for i in range(0, 9):
        # egy sor beolvasása
        lineBe = file.readline()
        # egy sor feldarabolása
        datas.append(line.split())
    # letárolás a táblázatban
    table.set_table(datas)

    # játékos lehetséges kitöltési lépéseinek letárolása
    for line in fileBe:
        steps.append(line.split())
print("Adatok letárolva")

# 3. Írja ki a képernyőre, hogy a beolvasott sor és oszlop értékének megfelelő hely…
# a. milyen értéket tartalmaz! Ha az adott helyen a 0 olvasható, akkor az „Az adott helyet még nem töltötték ki.” szöveget jelenítse meg!
# b. melyik résztáblázathoz tartozik!
print("\n3. feladat")
cell_value = table.get_cell(row,col)
cell_sector = table.get_sector_index(row,col)
if cell_value == '0':
    print("„Az adott helyet még nem töltötték ki.")
else:
    print(f"Az adott helyen szereplő szám: {cell_value}")
print(f"A hely a(z) {cell_sector} résztáblázathoz tartozik.")

# 4. Határozza meg a táblázat hány százaléka nincs még kitöltve! Az eredményt egy tizedesjegy pontossággal jelenítse meg a képernyőn!
print("\n4. feladat")
print(f"Az üres helyek aránya: {table.get_empty_rate():.1%} ")

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
    print(f"A kiválasztott sor: {t_row} oszlop: {t_col} a szám: {t_val}")
    if table.get_cell(t_row, t_col) != '0':
        print("A helyet már kitöltötték.")
    elif t_val in table.get_row(t_row):
        print("Az adott sorban már szerepel a szám.")
    elif t_val in table.get_col(t_col):
        print("Az adott oszlopban már szerepel a szám.")
    elif t_val in table.get_sector(t_row,t_col):
        print("Az adott résztáblázatban már szerepel a szám.")
    else:
        print("A lépés megtehető.")
    print()

