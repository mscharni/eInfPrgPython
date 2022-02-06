### Emelt Informatika Ismeretek Érettségi - 2016 Október - Bástyák
import random

tabla = []
gyalogok = []
bastyak = []

# 2. feladat: Készítsen eljárást vagy függvényt Megjelenit néven, amely a véletlenszerűen feltöltött 8×8-as mátrix tartalmát a következő oldalon lévő minta szerint megjeleníti a képernyőn! 
#    A kiírásnál az üres cellákat a „#” karakter jelölje! (A „#” karaktereket a mátrixban is tárolhatja.) 
def megjelenit():
    global tabla
    for i in range(0,8):
        row = ""
        for j in range(0,8):
            row += str(tabla[i][j])
        print(row)

# a feladatlapon látható első minta alapján
def megjelenit_2():
    global tabla
    # oszlopindexek
    cols = " "
    for i in range(0,8):
        cols += " " + str(i)
    print(cols)
    # sorok sorindex-szel
    for i in range(0,8):
        rows = str(i)
        for j in range(0,8):
            rows += " " + str(tabla[i][j])
        print(rows)


# 1. feladat: Hozzon létre egy 8×8-as karakter típusú mátrixot (kétdimenziós tömböt), és töltse fel azt véletlenszerű pozíciókban 10 db gyaloggal a következőek szerint: 
#    A gyalogok jelölésére a „G” karaktert használja! 
#    Ügyeljen arra, hogy csak üres helyre (cellába) tegyen gyalogot
print("\n1. feladat: Gyalogok elhelyezése:")
def gyalogok_elhelyez():
    global tabla, gyalogok, bastyak
    tabla = [["#" for i in range(0,8)] for i in range(0,8)]
    i = 0
    gyalogok = []
    while i < 8 :
        row = random.randint(0,7)
        col = random.randint(0,7)
        poz = (row,col)
        if poz not in gyalogok:
            gyalogok.append(poz)
            tabla[row][col] = "G"
            i += 1

gyalogok_elhelyez()
megjelenit()


# 3. feladat: Az előző feladatban létrehozott mátrixban helyezzen el véletlenszerű pozícióba további 5 db bástyát következők szerint: 
#    A bástyák jelölésére a „B” karaktert használja! 
#    Ügyeljen arra, hogy csak üres helyre (cellába) tegyen bástyát! 
#    Bástya nem kerülhet a tábla szélére. 
#    Írja ki a képernyőre feltöltött mátrix tartalmát! A megjelenítéshez a Megjelenit eljárást vagy függvényt használja!
print("\n3. feladat: Bástyák elhelyezése:")
def bastyak_elhelyez():
    global tabla, gyalogok, bastyak
    i = 0
    bastyak = []
    while i < 5 :
        row = random.randint(1,6)
        col = random.randint(1,6)
        poz = (row,col)
        if poz not in gyalogok and poz not in bastyak:
            bastyak.append(poz)
            tabla[row][col] = "B"
            i += 1
bastyak_elhelyez()
megjelenit()

# 4. feladat: Határozza meg a bástyák lépésértékeit, majd cserélje le a „B” karaktereket a lépésértéket jelző számjegyre a mátrixban a következő szabályok alapján: 
#    A bástyák négy irányba tudnak lépni (fel, le, jobbra, balra) egyenes vonalban.
#    Egy lépéssel tetszőleges számú üres mezőt (cellát) haladhatnak, ha azok a mezők üresek. 
#    A lépésérték 0-4-ig azt határozza meg, hogy hány irányba tud a bástya egy lépéssel a tábla szélére jutni.
print("\n4. feladat: Bástyák lépésértéke:")
def bastyak_lepesertek():
    global tabla, gyalogok, bastyak
    lepesek = []
    for bastya in bastyak:
        # feltesszük, hogy mind a négy irányban el tud jutni a tábla szélére
        lepes = 4

        # balra ellenőrzése
        row = bastya[0]
        for col in range(0, bastya[1]-1):
            if tabla[row][col] != "#":
                lepes -= 1
                break
        # jobbra ellenőrzése
        row = bastya[0]
        for col in range(bastya[1]+1, 8):
            if tabla[row][col] != "#":
                lepes -= 1
                break
        # fel ellenőrzése
        col = bastya[1]
        for row in range(0, bastya[0]-1):
            if tabla[row][col] != "#":
                lepes -= 1
                break
        # le ellenőrzése
        col = bastya[1]
        for row in range(bastya[0]+1, 8):
            if tabla[row][col] != "#":
                lepes -= 1
                break
        tabla[bastya[0]][bastya[1]] = lepes
        lepesek.append(lepes)
    lepesek.sort()
    return lepesek
    
ertekek = bastyak_lepesertek()
megjelenit()


    
# 5. feladat: Véletlenszerűen állítson elő mindaddig táblákat az első három feladatban leírtak szerint, amíg nem talál egy olyan állást, ahol az 5 bástya minden lehetséges lépésértéke (0-4) pontosan egyszer szerepel az adott felállásban!
#    Jelenítse meg ezt az állást is a képernyőn a minta szerint!
print("\n5. feladat: Minden érték:")
minden_ertek = [0, 1, 2, 3, 4]
while ertekek != minden_ertek:
    gyalogok_elhelyez()
    bastyak_elhelyez()
    ertekek = bastyak_lepesertek()
megjelenit()