### Emelt Informatika Érettségi - 2012 Október - Színkép

# 1. Feladat: Olvassa be a fájlból egy megfelelő adatszerkezetbe az egyes képpontok RGB kódját!
print("\n1. feladat:")
# üres kép létrehozása
rows = 50
cols = 50
kep = [["0 0 0" for i in range(0, cols)] for j in range(0, rows)]
with open("kep.txt") as fileBe:
    datas =  fileBe.readlines()
    idx = 0
    for line in datas:
        col = idx % cols
        row = idx // rows
        kep[row][col] = line.strip()
        idx += 1
print("Adatok beolvasva a 'kep.txt' állományból.")

# 2. Feladat: Kérjen be a felhasználótól egy RGB kódot!
#   Állapítsa meg a program segítségével, hogy a bekért szín megtalálható-e a képen!
#   A megállapítás eredményét írja ki a képernyőre!
print("\n2. feladat:")
# RGB = input("Adjon meg egy RGB kódot szóközzel elválasztva (pl: '200 96 64'):")
RGB = '200 96 64'
is_rgb = False
for i in range(0, rows):
    for j in range(0, cols):
        if kep[i][j] == RGB:
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
color = kep[row-1][col-1]
# Az adott sorban addig megyünk, amíg egyezik a szín
col_idx = col
while color == kep[row-1][col_idx] and col_idx < cols-1:
    col_idx +=1
# Az adott oszlopban addig megyünk, amíg egyezik a szín
row_idx = col
while color ==  kep[row_idx][col-1] and row_idx < rows-1:
    row_idx +=1
print(f"Sorban: {col_idx-col + 1} Oszlopban: {row_idx-row + 1}")

# 4.  Feladat: Állapítsa meg, hogy a vörös, kék és zöld színek közül melyik szín fordul elő legtöbbször a képen!
#   Az (egyik) legtöbbször előforduló szín nevét írja ki a képernyőre!
#     A színek kódjai: Vörös 255, 0, 0; Zöld 0, 255, 0; Kék 0, 0, 255:
print("\n4. feladat:")
R_count = 0
G_count = 0
B_count = 0
for i in range(0, rows):
    for j in range(0, cols):
        if kep[i][j] == "255 0 0":
            R_count += 1
        elif kep[i][j] == "0 255 0":
            G_count += 1
        elif kep[i][j] == "0 0 255":
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

print("\n5. feladat:")
keretszin = "0 0 0"       # keret színe: fekete
keretszel = 3             # keret szélessége: 3

# felső és alsó, valamint bal és jobb 'keretszel'-nyi sor ill oszlop pontjai színének felülírása
for i in range(0,keretszel):
    for j in range(0, cols):
        kep[i][j] = keretszin      # TOP
        kep[-i][j] = keretszin     # BOTTOM
    for j in range(0, rows):
        kep[j][i] =  keretszin     # LEFT
        kep[j][-i-1] = keretszin   # RIGHT
print("Keret elkészítve")

# 6.  Feladat: A kép képpontjainak színét írja ki a _keretes.txt_ nevű szövegfájlba a bemeneti fájl formátumával egyezően!
#   A képet sorfolytonosan tárolja, minden képpontot új sorba, a képpontok RGB kódját szóközzel elválasztva írja ki!
print("\n6. feladat:")
with open("keretes.txt", "w") as fileKi:
    for i in range(0, rows):
        for j in range(0, cols):
            fileKi.write(kep[i][j] +"\n")
print("Adatok kiírva a 'keretes.txt' állományba")

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
while i < rows and is_szin == False:
    j = 0
    while j < cols and is_szin == False:
        if kep[i][j] == szin:
            top = i
            left = j
            is_szin = True
        j += 1
    i += 1
# kihasználjuk, hogy téglalap, azaz a talált sorban lévő utolsó keresett színű pont a jobb oldali
i = top
j = left
while j < cols and kep[i][j] == szin:
    j += 1
right = j-1
# kihasználjuk, hogy téglalap, azaz a talált oszlopban lévő utolsó keresett színű pont a lenti
i = top
j = left
while i < rows and kep[i][j] == szin:
    i += 1
bottom = i-1
szin_count = (bottom - top + 1) * (right - left + 1)
print(f"Kezd: {top+1}, {left+1}")
print(f"Vége: {bottom+1}, {right+1}")
print(f"Képpontok száma: {szin_count}")
