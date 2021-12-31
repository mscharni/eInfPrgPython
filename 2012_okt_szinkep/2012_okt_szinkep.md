# Emelt Informatika Érettségi - 2012 október - Szín-kép

## Online forráskódok
1. [Megoldás váz](https://replit.com/@mscharni/2012oktszinkepstarter)
2. [Megoldás - alap szintű](https://replit.com/@mscharni/2012oktszinkepsimple)
2. [Megoldás - haladó szintű](https://replit.com/@mscharni/2012oktszinkepadvanced)

## Feladat
Egy digitális kép tárolásánál minden egyes képpont színét tároljuk. A képpontok színét az RGB kód adja. Az RGB kód a vörös (R), zöld (G) és a kék (B) színösszetevő értékét határozza meg. Ezen színösszetevők értéke 0 és 255 közötti egész szám lehet.

A **_kep.txt_** fájlban egy 50×50 képpontos kép képpontjainak RGB kódjai vannak a következő formában. Az állomány a képet sorfolytonosan, a képpontok RGB kódját szóközzel elválasztva tartalmazza, minden képpontot egy újabb sorban:
```
200 96 64
200 96 64
200 96 64
200 96 64
200 96 64
```

Készítsen programot **_szinkep_** néven a következő feladatok megoldására! A program futása során a képernyőre való kiíráskor, illetve az adatok billentyűzetről való beolvasásakor utaljon a feladat sorszámára és a kiírandó, illetve bekérendő adatra!

1. Olvassa be a fájlból egy megfelelő adatszerkezetbe az egyes képpontok RGB kódját!

2. Kérjen be a felhasználótól egy RGB kódot! Állapítsa meg a program segítségével, hogy a bekért szín megtalálható-e a képen! A megállapítás eredményét írja ki a képernyőre!

3. Határozza meg, hogy a kép 35. sor 8. képpontjának színe hányszor szerepel a 35. sorban, illetve a 8. oszlopban. Az értékeket írja ki a képernyőre az alábbi formában:
Például:
`Sorban: 5 Oszlopban: 10`

4. Állapítsa meg, hogy a vörös, kék és zöld színek közül melyik szín fordul elő legtöbbször a képen! Az (egyik) legtöbbször előforduló szín nevét írja ki a képernyőre!
A színek kódjai:

| Szín |   Kód     |
|:---: |   :---:   |
|Vörös | 255, 0, 0 |
| Zöld | 0, 255, 0 |
| Kék  | 0, 0, 255 |


5. Készítsen 3 képpont széles, fekete színű keretet a képnek! A keretet úgy hozza létre, hogy a kép mérete ne változzon! A fekete szín kódja RGB (0, 0, 0).

6. A kép képpontjainak színét írja ki a **_keretes.txt_** nevű szövegfájlba a bemeneti fájl formátumával egyezően! A képet sorfolytonosan tárolja, minden képpontot új sorba, a képpontok RGB kódját szóközzel elválasztva írja ki!
Például:
```
...
0 0 0
0 0 0
200 96 64
...
```

7. Az 50×50-es képen a kerettől függetlenül egy sárga **RGB(255, 255, 0)** színű téglalap van. Határozza meg a program segítségével a bal felső és a jobb alsó sárga képpontnak a helyét (sor, oszlop), majd határozza meg, hogy a sárga téglalap hány képpontból áll!
A képpontok helyét és a sárga alakzat méretét a következő formában írassa ki a képernyőre:
```
Kezd: sor, oszlop
Vége: sor, oszlop
Képpontok száma: darab
```
Például:
```
Kezd: 18, 12
Vége: 25, 19
Képpontok száma: 64
```