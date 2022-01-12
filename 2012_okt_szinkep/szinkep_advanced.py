### Emelt Informatika Érettségi - 2012 Október - Színkép

class Szin():
   def __init__(self, line = "0 0 0"):
        self.RGB = line.strip()
        datas = self.RGB.split(" ")
        self.R = int(datas[0])
        self.G = int(datas[1])
        self.B = int(datas[2])

class Kep():
    def __init__(self, rows = 50, cols = 50, datas = None):
        self.rows = rows
        self.cols = cols
        # üres (fekete) pontokkal feltöltjük a képet
        self.pontok = [[Szin("0 0 0") for i in range(0, self.cols)] for j in range(0, self.rows)]
        # ha van adat, akkor feltöltjük a pontokat
        if datas != None:
            i = 0
            for line in datas:
                col = i % self.cols
                row = i // self.rows
                szin = Szin(line)
                self.set_point(row, col, szin)
                i += 1

    def set_point(self, row, col, szin):
        self.pontok[row][col] = szin

    # a print metódus nem része az érettségi feladatnak!
    def print(self):
        pont_char = "██"        # a pontot képviselő karakter (string)
        firstline = "   "       # az első megjelenített sorban kiírjuk az oszlopok sorszámát
        for j in range(0, self.cols):
            firstline += f"{j+1:2}"
        print(firstline)
        for i in range(0, self.rows):
            rowString = f"{i+1:3}"      # minden sor elején kiírjuk a sor sorszámát
            for j in range(0, self.cols):
                pont = self.pontok[i][j]
                C = colored(pont.R, pont.G, pont.B, pont_char)
                rowString += C
            print(rowString)
# a színezett kiiratás nem része az érettségi feladatnak!
# az RGB kódnak megfelelő színben jeleníti meg két karakter szélességben a "képpontot" képviselő karaktert
def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[38;2;255;255;255m"


# 1. Feladat: Olvassa be a fájlból egy megfelelő adatszerkezetbe az egyes képpontok RGB kódját!
print("\n1. feladat:")
with open("kep.txt") as fileBe:
    datas =  fileBe.readlines()
    kep = Kep(rows=50, cols=50, datas=datas)
print("Adatok beolvasva a 'kep.txt' állományból.")
# nem része az érettségi feladatnak:
print("A kép:")
kep.print()

# 2. Feladat: Kérjen be a felhasználótól egy RGB kódot!
#   Állapítsa meg a program segítségével, hogy a bekért szín megtalálható-e a képen!
#   A megállapítás eredményét írja ki a képernyőre!
print("\n2. feladat:")
# RGB = input("Adjon meg egy RGB kódot szóközzel elválasztva (pl: '200 96 64'):")
RGB = '200 96 64'
is_rgb = False
for i in range(0, kep.rows):
    for j in range(0, kep.cols):
        if kep.pontok[i][j].RGB == RGB:
            is_rgb = True
            break
if is_rgb:
    print(f"A képen szerepel '{RGB}' színű képpont.")
else:
    print(f"A képen nem szerepel '{RGB}' színű képpont.")

# 3. Feladat: Határozza meg, hogy a kép 35. sor 8. képpontjának színe hányszor szerepel a 35. sorban, illetve a 8. oszlopban.
#   Az értékeket írja ki a képernyőre az alábbi formában:
#        Sorban: 5 Oszlopban: 10
print("\n3. feladat:")
row = 35
col = 8
color = kep.pontok[row-1][col-1].RGB
# Az adott sorban addig megyünk, amíg egyezik a szín
col_idx = col
while color ==  kep.pontok[row-1][col_idx].RGB and col_idx < kep.cols-1:
    col_idx +=1
# Az adott oszlopban addig megyünk, amíg egyezik a szín
row_idx = col
while color ==  kep.pontok[row_idx][col-1].RGB and row_idx < kep.rows-1:
    row_idx +=1
print(f"Sorban: {col_idx-col + 1} Oszlopban: {row_idx-row + 1}")

# 4.  Feladat: Állapítsa meg, hogy a vörös, kék és zöld színek közül melyik szín fordul elő legtöbbször a képen!
#   Az (egyik) legtöbbször előforduló szín nevét írja ki a képernyőre!
#     A színek kódjai: Vörös 255, 0, 0; Zöld 0, 255, 0; Kék 0, 0, 255:
print("\n4. feladat:")
R_count = 0
G_count = 0
B_count = 0
for i in range(0, kep.rows):
    for j in range(0, kep.cols):
        if kep.pontok[i][j].RGB == "255 0 0":
            R_count += 1
        elif kep.pontok[i][j].RGB == "0 255 0":
            G_count += 1
        elif kep.pontok[i][j].RGB == "0 0 255":
            B_count += 1
# a három elemből a legnagyobb kiválasztása
if R_count > G_count  and R_count > B_count:
    print(f"Vörös a legtöbbször előforduló szín: {R_count} db")
elif G_count > R_count  and G_count > B_count:
    print(f"Zöld a legtöbbször előforduló szín: {G_count} db")
else:
    print(f"Kék a legtöbbször előforduló szín: {B_count} db")

# 5.  Feladat: Készítsen 3 képpont széles, fekete színű keretet a képnek!
#   A keretet úgy hozza létre, hogy a kép mérete ne változzon! A fekete szín kódja RGB (0, 0, 0).
#   FIXIT: A feladat meghatározása nem egyértelmű, ezért a kétféle megoldás:
#       A., a képnek 50*50-esnek kell maradnia (kép mérete ne változzon), azaz felül kell írni a kép keretnek megfelelő pontjait
#       B., a képen belüli tartalomnak (ábrának) kell 50*50-esnek maradnia, azaz ki kell bővíteni a képet leíró adatokat a keret adataival

print("\n5. feladat:")
keretszin = Szin("0 0 0")       # keret színe: fekete
keretszel = 3                   # keret szélessége: 3

print("\n5.A. megoldás:")
# az eredeti kép pontjairól másolatot készítünk
kep_a = Kep(rows=kep.rows, cols=kep.cols)
for i in range(0, kep.rows):
    for j in range(0, kep.cols):
        kep_a.pontok[i][j] = kep.pontok[i][j]
# felső és alsó, valamint bal és jobb 'keretszel'-nyi sor ill oszlop pontjai színének felülírása
for i in range(0,keretszel):
    for j in range(0,kep_a.cols):
        kep_a.set_point(i, j, keretszin)        # TOP
        kep_a.set_point(-i-1, j, keretszin)     # BOTTOM
    for j in range(0,kep_a.rows):
        kep_a.set_point(j, i, keretszin)        # LEFT
        kep_a.set_point(j, -i-1, keretszin)     # RIGHT
# a képernyőre kiiratás nem része az érettségi feladatnak
print("Bekeretezett kép (A verzió):")
kep_a.print()

print("\n5.B. megoldás:")
# létrehozunk egy új kép objektumot, amely a kerettel megnövelt méretű
kep_b = Kep(rows=kep.rows + 2 * keretszel, cols=kep.rows + 2 * keretszel)
# eredeti kép pontjainak átmásolása a kereten belülre
for i in range(0,kep.rows):
    for j in range(0,kep.cols):
        kep_b.pontok[i+keretszel][j+keretszel] = kep.pontok[i][j]

# keret elkészítése (ez most valójában felesleges, mivel alapértelmezésben (kép objektum létrehozásakor) is fekete a teljes üres kép)
# felső és alsó, valamint bal és jobb 'keretszel'-nyi sor ill oszlop pontjai színének felülírása
for i in range(0,keretszel):
    for j in range(0,kep_b.cols):
        kep_b.set_point(i, j, keretszin)        # TOP
        kep_b.set_point(-i-1, j, keretszin)     # BOTTOM
    for j in range(0,kep_b.rows):
        kep_b.set_point(j, i, keretszin)        # LEFT
        kep_b.set_point(j, -i-1, keretszin)     # RIGHT
# a képernyőre kiiratás nem része az érettségi feladatnak
print("Bekeretezett kép (B verzió):")
kep_b.print()


# 6.  Feladat: A kép képpontjainak színét írja ki a _keretes.txt_ nevű szövegfájlba a bemeneti fájl formátumával egyezően!
#   A képet sorfolytonosan tárolja, minden képpontot új sorba, a képpontok RGB kódját szóközzel elválasztva írja ki!
#   FIXIT: az 5. pontbeli A és B verziónak megfelelően két kimeneti állományt készítünk
print("\n6. feladat:")
print("\nA. megoldás:")
with open("keretes_a.txt", "w") as fileKi:
    for i in range(0, kep_a.rows):
        for j in range(0, kep_a.cols):
            fileKi.write(kep_a.pontok[i][j].RGB +"\n")
print("Adatok kiírva a 'keretes_a.txt' állományba")

# Gyakorlatilag ugyanaz a megoldás, csak másik képpel
print("\nB. megoldás:")
with open("keretes_b.txt", "w") as fileKi:
    for i in range(0, kep_b.rows):
        for j in range(0, kep_b.cols):
            fileKi.write(kep_b.pontok[i][j].RGB +"\n")
print("Adatok kiírva a 'keretes_b.txt' állományba")

# 7. Feladat: Az 50×50-es képen a kerettől függetlenül egy sárga RGB (255, 255, 0) színű téglalap van.
#     Határozza meg a program segítségével a bal felső és a jobb alsó sárga képpontnak a helyét
#     (sor, oszlop), majd határozza meg, hogy a sárga téglalap hány képpontból áll!
print("\n7. feladat:")
szin = "255 255 0"
# az eredeti képen a sárga téglalap bal felső sarkának a megkeresése
is_szin = False
top = -1
left = -1
bottom = -1
right = -1
i = 0
# addig megyünk, míg meg nem találjuk az adott szíűnű 'pixelt'
while i < kep.rows and is_szin == False:
    j = 0
    while j <  kep.cols and is_szin == False:
        if kep.pontok[i][j].RGB == szin:
            top = i
            left = j
            is_szin = True
        j += 1
    i += 1
# ha van bal felső sarok, akkor megkeressük a jobb oldali, valamint alsó koordinátát. Ez a feltétel is felesleges elvileg, mivel biztosan van adott színű pont a képen
if top != -1:
    # kihasználjuk, hogy téglalap, azaz a talált sorban lévő utolsó keresett színű pont a jobb oldali
    i = top
    j = left
    while j < kep.cols and kep.pontok[i][j].RGB == szin:
        j += 1
    right = j - 1
    # kihasználjuk, hogy téglalap, azaz a talált oszlopban lévő utolsó keresett színű pont a lenti
    i = top
    j = left
    while i < kep.rows and kep.pontok[i][j].RGB == szin:
        i += 1
    bottom = i - 1
    szin_count = (bottom - top + 1) * (right - left + 1)
    print(f"Kezd: {top+1}, {left+1}")
    print(f"Vége: {bottom+1}, {right+1}")
    print(f"Képpontok száma: {szin_count}")
else:
    print(f"Nincs '{szin}' színű téglalap!")
