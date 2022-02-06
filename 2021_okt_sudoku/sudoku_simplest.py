### Emelt Informatika Érettségi - 2021 Október - Sudoku

# 1. feladat: Olvassa be egy fájl nevét, egy sor és egy oszlop sorszámát (1 és 9 közötti számot)!
# A későbbi feladatokat ezen értékek felhasználásával kell megoldania!
print("\n1. feladat")
fajl_nev = input("adja meg a bemeneti fájl nevét!")
sor = int(input("adja meg a sor számát!"))-1
oszlop =  int(input("Adja meg egy oszlop számát!"))-1


# 2. feladat: Az előző feladatban beolvasott névnek megfelelő fájl tartalmát olvassa be, és tárolja el a táblázat adatait!
tabla = []
lepesek = []
with open ( fajl_nev ,"r") as f:
    lines = f.readlines()
# tábla adatai (első kilenc sor)
for i in range(0,9):
    line = lines[i].strip()
    tabla.append(line.split(" "))
# játékos adatai (többi sor)  
for i in range(9, len(lines)):
    line = lines[i].strip()
    lepesek.append(line.split(" "))


# 3. feladat: Írja ki a képernyőre, hogy a beolvasott sor és oszlop értékének megfelelő hely…
#    a. milyen értéket tartalmaz! Ha az adott helyen a 0 olvasható, akkor az „Az adott helyet még nem töltötték ki.” szöveget jelenítse meg!
#    b. melyik résztáblázathoz tartozik!
print("\n3. feladat")
# cella értéke
if tabla[sor][oszlop] !="0":
    print(f"Az adott helyen szereplő szám: {tabla[sor][oszlop]}")
else:
    print("Az adott helyet még nem töltötték ki")
# cella résztáblázata
print(f"A ({sor+1},{oszlop+1}) hely a(z) {1 + 3*(sor // 3) + oszlop // 3} résztáblázathoz tartozik.") 


# 4. feladat: Határozza meg a táblázat hány százaléka nincs még kitöltve! Az eredményt egy tizedesjegy pontossággal jelenítse meg a képernyőn!
print("\n4. feladat")
nullak = 0
for sor in tabla:
    for cella in sor:
        if cella == '0':
            nullak += 1
print(f"Az üres helyek aránya: {nullak / 81:.1%}")            


# 5. feladat Vizsgálja meg, hogy a fájlban szereplő lépések lehetségesek-e a beolvasott táblázaton!
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
# végig kell menni az összes lépésen
for lepes in lepesek:
    szam = lepes[0]
    # korrigáljuk a sor és oszlop számát nulla kezdőindexűre
    s = int(lepes[1])-1
    o = int(lepes[2])-1
    # cella sora: kilencelemű lista
    sor = tabla[s]
    # cella oszlopa: kilencelemű lista
    oszlop = [tabla[i][o] for i in range(0,9)]
    # cella résztáblázata
    # kell hozzá a résztáblázat bal felső cellájának sor- és oszlop száma
    bf_s = 3 * (s // 3) # bal felső sarok sor koordinátája
    bf_o = 3 * (o // 3) # bal felső sarok oszlop koordinátája
    # egy kilencelemű listát készítünk a résztábla celláiból a bal-felső cellájától indulva
    rtabla = []
    for i in range(bf_s, bf_s + 3):
        for j in range(bf_o, bf_o + 3):
            rtabla.extend(tabla[i][j])

    # cella ellenőrzése
    if tabla[s][o] != '0':
        print("A helyet már kitöltötték")
    # sor ellenőrzése
    elif szam in sor:
        print("Az adott sorban már szerepel a szám")
    elif szam in oszlop:
        print("Az adott oszlopban már szerepel a szám")
    elif szam in rtabla:
        print("Az adott résztáblázatban már szerepel a szám")
    else:
        print("A lépés megtehető")
