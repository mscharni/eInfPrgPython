# Emelt Informatika Érettségi - 2021 május - Gödrök

## Feladat
A sudoku egy logikai játék, melyben megadott szabályok szerint számjegyeket kell elhelyezni egy táblázatban. Ebben a feladatban **9×9**-es táblázatot használunk.

A táblázat – az alábbi ábrának megfelelően – **9 darab 3×3-as résztáblázat**ra van felosztva. Minden résztáblázatot az 1, 2, 3, 4, 5, 6, 7, 8, 9 számokkal kell kitölteni úgy, hogy az egész 9×9-es táblázat minden sorában és minden oszlopában az 1...9 számok mindegyike pontosan egyszer forduljon elő. A rejtvény készítője előre ki szokta tölteni a táblázat bizonyos celláit. A rejtvényfejtő feladata kitölteni a maradék cellákat a leírt szabályoknak megfelelően.

_A számok megadják, hogy az egyes **3×3 méretű résztáblák**at milyen számmal azonosítjuk:_

||||
| :---: | :---: | :---: |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

A bemenetet tartalmazó szövegfájlok első 9 sorának mindegyike 9 egész számot tartalmaz, a játék kiindulási állapotának megfelelően. A kitöltetlen mezők helyén a 0 szám olvasható. A következő néhány sorban a játékos egy-egy lehetséges kitöltési lépését rögzítették. Egy lépést három egész szám ír le: a számot, amelyet a játékos be akar írni, majd a sor és az oszlop számát, ahova írni szeretné. A bemeneti fájl egy-egy sorában a számokat egy-egy szóköz választja el egymástól. A táblázat ellentmondásmentes, tehát megoldható feladatot ír le. A játékos által megtett lépések száma legalább 1, legfeljebb 10, közöttük lehet hibás.

### Például:
```
0 0 0 0 0 0 0 0 6
0 0 7 0 0 0 2 0 0
3 8 9 5 0 0 0 0 0
6 0 0 0 0 0 7 0 0
1 2 8 4 9 0 0 3 0
0 0 0 0 0 0 0 0 9
0 5 1 0 0 0 0 4 0
0 0 0 0 0 3 0 9 1
0 0 0 0 8 0 0 0 0
9 2 4
1 2 1
5 9 9
7 2 2
```
A fenti példában a **_nehez.txt_** bemeneti fájl tartalma látható. A 10. sorban szereplő számok azt jelentik, hogy a 9-es értéket kell a 2. sor 4. helyére beírni. Az adott sorban és az adott oszlopban nem szerepel még a 9-es, sőt, az érintett négyzetben sem, így a lépéssel nem alakul ki hiba, megtehető. A 11. sorbeli lépés is megtehető. A 13. sor hibás lépést tartalmaz, mert a 2. sorban már szerepel a 7-es szám.

Készítsen programot, amely a bemeneti állományok egyikét felhasználva ( **_konnyu.txt_** , **_kozepes.txt_** , **_nehez.txt_** ) az alábbi kérdésekre válaszol! A program forráskódját mentse **_sudoku_** néven! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: `4. feladat`)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Az ékezetmentes kiírás is elfogadott.

1. Olvassa be egy fájl nevét, egy sor és egy oszlop sorszámát (1 és 9 közötti számot)! A későbbi feladatokat ezen értékek felhasználásával kell megoldania!

2. Az előző feladatban beolvasott névnek megfelelő fájl tartalmát olvassa be, és tárolja el a táblázat adatait! Ha ezt nem tudja megtenni, akkor használja forrásként a rendelkezésre álló állományok egyikét!

3. Írja ki a képernyőre, hogy a beolvasott sor és oszlop értékének megfelelő hely...
a.) milyen értéket tartalmaz! Ha az adott helyen a 0 olvasható, akkor az „`Az adott helyet még nem töltötték ki.`” szöveget jelenítse meg!
b.) melyik résztáblázathoz tartozik!

4. Határozza meg a táblázat hány százaléka nincs még kitöltve! Az eredményt egy tizedesjegy pontossággal jelenítse meg a képernyőn!

5. Vizsgálja meg, hogy a fájlban szereplő lépések lehetségesek-e a beolvasott táblázaton! Tekintse mindegyiket úgy, mintha az lenne az egyetlen lépés az eredeti táblázaton, de ne hajtsa azt végre! Állapítsa meg, hogy okoz-e valamilyen ellentmondást a lépés végrehajtása!
Írja ki a lépéshez tartozó három értéket, majd a következő sorba írja az alábbi     megállapítások egyikét! Ha több megállapítás is igaz, elegendő csak egyet megjelenítenie.
- „`A helyet már kitöltötték`”
- „`Az adott sorban már szerepel a szám`”
- „`Az adott oszlopban már szerepel a szám`”
- „`Az adott résztáblázatban már szerepel a szám`”
- „`A lépés megtehető`”

### Minta a szöveges kimenetek kialakításához:
```
1. feladat
Adja meg a bemeneti fájl nevét! konnyu.txt
Adja meg egy sor számát! 1
Adja meg egy oszlop számát! 1

3. feladat
Az adott helyen szereplő szám: 5
A hely a(z) 1 résztáblázathoz tartozik.

4. feladat
Az üres helyek aránya: 17.3%

5. feladat
A kiválasztott sor: 2 oszlop: 4 a szám: 9
A helyet már kitöltötték.

A kiválasztott sor: 3 oszlop: 6 a szám: 7
A lépés megtehető.

A kiválasztott sor: 6 oszlop: 6 a szám: 3
A résztáblázatban már szerepel a szám.

A kiválasztott sor: 7 oszlop: 9 a szám: 8
Az adott oszlopban már szerepel a szám.
```