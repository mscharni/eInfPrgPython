# Emelt Informatikai Alapismeretek - 2016 október - Bástyák

## Bástyák

Ebben a feladatban egy 8x8-as mátrixban mint sakktáblán a számítógép által véletlenszerűen elhelyezett bástyákkal és gyalogokkal fog dolgozni.
A megoldás során vegye figyelembe a következőket:
- A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: 3. Feladat:)!
- Az ékezetmentes kiírás is elfogadott.
- A feladat jobb megértése érdekében tanulmányozza a mintát!

Készítsen programot **bastyak** néven, amely az alábbi feladatokat oldja meg!

1. Hozzon létre egy 8×8-as karakter típusú mátrixot (kétdimenziós tömböt), és töltse fel azt véletlenszerű pozíciókban 10 db gyaloggal a következőek szerint:
  - A gyalogok jelölésére a „**G**” karaktert használja!
  - Ügyeljen arra, hogy csak üres helyre (cellába) tegyen gyalogot!

2. Készítsen eljárást vagy függvényt **Megjelenit** néven, amely a véletlenszerűen feltöltött 8×8-as mátrix tartalmát a lap alján lévő minta szerint megjeleníti a képernyőn! 
A kiírásnál az üres cellákat a „**#**” karakter jelölje! (A „#” karaktereket a mátrixban is tárolhatja.)

3. Az előző feladatban létrehozott mátrixban helyezzen el véletlenszerű pozícióba további 5 db bástyát következők szerint:
  - A bástyák jelölésére a „**B**” karaktert használja!
  - Ügyeljen arra, hogy csak üres helyre (cellába) tegyen bástyát!
  - Bástya nem kerülhet a tábla szélére.

Írja ki a képernyőre feltöltött mátrix tartalmát! A megjelenítéshez a **Megjelenit** eljárást vagy függvényt használja!

4. Határozza meg a bástyák lépésértékeit, majd cserélje le a „**B**” karaktereket a lépésértéket jelző számjegyre a mátrixban a következő szabályok alapján:
  - A bástyák négy irányba tudnak lépni (fel, le, jobbra, balra) egyenes vonalban. Egy lépéssel tetszőleges számú üres mezőt (cellát) haladhatnak, ha azok a mezők üresek.
  - A lépésérték 0-4-ig azt határozza meg, hogy hány irányba tud a bástya egy lépéssel a tábla szélére jutni.
    
    Például a következő tábla esetén a 4. sor 7. oszlopában lévő bástya értéke 2, mert felfelé és balra egy lépéssel el tudja érni a tábla szélét. 
	Másrészt a 6. sor 7. oszlopában lévő bástya értéke 0, mert nincs olyan irány, ahol szabadon haladhatna a tábla széléig.
    ```
         1 2 3 4 5 6 7 8
       1 # G # # G # # #
       2 # # # B # G # #
       3 # # # G # # # #
       4 # # # # # # B G
       5 # # # # # # # G
       6 G B # # G # B G
       7 # # B # # # # #
       8 # # # # # # G #
    ```
    Írja ki a képernyőre a lépésértékekkel módosított mátrix tartalmát!

5. Véletlenszerűen állítson elő mindaddig táblákat az első három feladatban leírtak szerint, amíg nem talál egy olyan állást, ahol az 5 bástya minden lehetséges lépésértéke (0-4) pontosan egyszer szerepel az adott felállásban! 
Jelenítse meg ezt az állást is a képernyőn a minta szerint!

## Minta a feladatokhoz:
```
1. feladat: Gyalogok elhelyezése:
GG######
######G#
#####GG#
###G###G
########
########
#G###G##
######G#

3. feladat: Bástyák elhelyezése:
GG######
######G#
##B#BGG#
###G###G
##B#####
##B#####
#G##BG##
######G#

4. feladat: Bástyák lépésértékei:
GG######
######G#
##2#1GG#
###G###G
##2#####
##3#####
#G##1G##
######G#

5. feladat: Minden érték:
###G####
G###1G##
####G##G
########
##2#0#3#
#4######
G#GGG###
#####G##
```
