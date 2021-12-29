# Emelt Informatika Érettségi - 2019 október - eUtazás

## Online forráskódok
1. [Megoldás váz](https://replit.com/@mscharni/2019okteutazasstarter)
2. [Megoldás](https://replit.com/@mscharni/2019okteutazas)

## Feladat
Egyre több országban fordul elő, hogy a közlekedési eszközökön használatos bérleteket és jegyeket valamilyen elektronikus eszközön (például: chipes kártya) tárolják. Egy nagyváros ilyen rendszert szeretne bevezetni a helyi közlekedésben, amelyet néhány buszjáraton tesztelnek. Ezekre a buszokra csak az első ajtónál lehet felszállni, ahol egy ellenőrző eszközhöz kell érinteni a kártyát, amelynek chipje tartalmazza a jegy vagy bérlet információkat.

A busz ellenőrző eszköze statisztikai és fejlesztési célból rögzíti a felszállók kártyájának adatait. Az **_utasadat.txt_** szóközökkel tagolt állomány egy, a tesztelésben részt vevő busz végállomástól-végállomásig tartó útjának adatait tartalmazza.

Az **_utasadat.txt_** állomány legfeljebb 2000 sort tartalmaz és minden sorában 5 adat szerepel. Ezek:
- a megálló sorszáma (0-29; 0 az indulás helye és a 30 a végállomás, ahol már nem lehet felszállni.)
- a felszállás dátuma és időpontja (ééééhhnn-óópp formátumban, kötőjellel elválasztva a dátum és az idő)
- a kártya egyedi azonosítója (hétjegyű szám), egy utas a járaton legfeljebb egyszer utazik
- a jegy vagy bérlet típusa:

| Azonosító | Megnevezés |
| :--- | :--- |
| FEB | Felnőtt bérlet |
| TAB | Tanulóbérlet (kedvezményes) |
| NYB | Nyugdíjas bérlet (kedvezményes) |
| NYP | 65 év feletti bérlet (ingyenes) |
| RVS | Rokkant, vak, siket vagy kísérő bérlet (ingyenes) |
| GYK | Iskolakezdés előtti gyerekbérlet (ingyenes) |
| JGY | Jegy |

- a bérlet érvényességi ideje, vagy a felhasználható jegyek száma. A bérlet esetén a dátum ééééhhnn formátumban szerepel, jegy esetén egy 0-10 közötti szám szerepel.
Például:
```
0 20190326-0700 6572582 RVS 20210101
0 20190326-0700 8808290 JGY 7
0 20190326-0700 1680423 TAB 20190420
12 20190326-0716 3134404 FEB 20190301
12 20190326-0716 9529716 JGY 0
```
A fenti példában szereplő adatoknál látható, hogy az induló állomáson (0. állomás) 2019. 03. 26-án 7:00-kor a 1680423 kártyaazonosítójú utas tanulóbérlettel szállt fel, amely 2019. 04. 20-ig érvényes. A 12. állomáson 2019. 03. 26-án 7:16-kor a 9529716 kártyaazonosítójú utas jeggyel szállt volna fel, de már elhasználta az összes jegyét (0).

Készítsen programot, amely az **_utasadat.txt_** állomány felhasználásával a következő kérdésekre válaszol! A program forráskódját **_eutazas_** néven mentse! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például `2. feladat`)! A részfeladatok eredményeit a mintán látható formában jelenítse meg! Az ékezetmentes kiírás is elfogadott.

1. Olvassa be és tárolja el az **_utasadat.txt_** fájl tartalmát!

2. Adja meg, hogy hány utas szeretett volna felszállni a buszra!

3. A közlekedési társaság szeretné, ha a járművőn csak az érvényes jeggyel vagy bérlettel rendelkezők utaznának. Ezért a jegyeket és bérleteket a buszvezető a felszálláskor ellenőrzi. (A bérlet még érvényes a lejárat napján.) Adja meg, hogy hány esetben kellett a buszvezetőnek elutasítania az utas felszállását, mert lejárt a bérlete vagy már nem volt jegye!

4. Adja meg, hogy melyik megállóban próbált meg felszállni a legtöbb utas! (Több azonos érték esetén a legkisebb sorszámút adja meg!)

5. A közlekedési társaságnak kimutatást kell készítenie, hogy hányszor utaztak valamilyen kedvezménnyel a járművön. Határozza meg, hogy hány kedvezményes és hány ingyenes utazó szállt fel a buszra! (Csak az érvényes bérlettel rendelkező szállhatott fel a buszra!)

6. Készítsen függvényt **napokszama** néven az alábbi algoritmus alapján. Az algoritmus a paraméterként megadott két dátumhoz (év, hónap, nap) megadja a közöttük eltelt napok számát! (A MOD a maradékos osztást, a DIV az egészrészes osztást jelöli.) Az algoritmust a **_fuggveny.txt_** fájlban is megtalálja. A függvényt a következő feladat megoldásához     felhasználhatja.
```
Függvény napokszama(e1:egész, h1:egész, n1: egész, e2:egész,
	h2: egész, n2: egész): egész
	h1 = (h1 + 9) MOD 12
	e1 = e1 - h1 DIV 10
	d1 = 365*e1 + e1 DIV 4 - e1 DIV 100 + e1 DIV 400 + (h1*306 + 5) DIV 10 + n1 - 1
	h2 = (h2 + 9) MOD 12
	e2 = e2 - h2 DIV 10
	d2 = 365*e2 + e2 DIV 4 - e2 DIV 100 + e2 DIV 400 + (h2*306 + 5) DIV 10 + n2 - 1
	napokszama:= d2-d
Függvény vége
```

7. A közlekedési társaság azoknak az utasoknak, akiknek még érvényes, de 3 napon belül lejár a bérlete, figyelmeztetést szeretne küldeni e-mailben. (Például, ha a felszállás időpontja 2019. február 5., és a bérlet érvényessége 2019. február 8., akkor már kap az utas levelet, ha 2019. február 9. az érvényessége, akkor még nem kap levelet.) Válogassa ki és írja a **_figyelmeztetes.txt_** állományba ezen utasok kártyaazonosítóját és a bérlet érvényességi idejét (éééé-hh-nn formátumban) szóközzel elválasztva!

### Minta a szöveges kimenetek kialakításához:
```
2. feladat
A buszra 699 utas akart felszállni.

3. feladat
A buszra 21 utas nem szállhatott fel.

4. feladat
A legtöbb utas (39 fő) a 8. megállóban próbált felszállni.

5. feladat
Ingyenesen utazók száma: 133 fő
A kedvezményesen utazók száma: 200 fő
```

### Minta a _figyelmeztetes.txt_ állomány kialakításához:
```
3023275 2019-03-29
2960983 2019-03-26
1581897 2019-03-27
2761792 2019-03-28
...
```