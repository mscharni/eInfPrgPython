# Emelt Informatika Érettségi - 2018 október - Kerítés

## Feladat
Egy üdülőfalu újonnan nyitott utcájában a telkeket a saroktól kiindulva egymás után folyamatosan, kihagyások nélkül adják el. A vásárló kiválaszthatja az oldalt, amelyen vásárolni akar (ott csak a soron következő telket vásárolhatja meg), valamint megadhatja a telek utcafronti szélességét. Sok telket vettek meg az utcában, a legtöbben már kerítést is építettek, azok majd’ mindegyikét be is festették.

A **_kerites.txt_** fájl az utca telkeinek jelenlegi állapotát írja le. A telkek a vásárlás sorrendjében szerepelnek. Minden sorban három adat található. Az első szám megadja, hogy a telek a **páros (0)** vagy a **páratlan (1)** oldalán van az utcának; a második a telek szélességét adja meg méterben (egész szám, értéke 8 és 20 között lehet); a harmadik pedig az utcafronti kerítés színét leíró karakter. A szín az angol ábécé nagybetűje. Ha a kerítést már elkészítették, de nem festették be, akkor a „ **#** ” karakter, ha még nem készült el, akkor a „ **:** ” (kettőspont) karakter szerepel. Az utca hossza legfeljebb 1000 méter. Mindkét oldalon elkelt legalább 3-3 telek.

### Például:
```
0 10 P
1 8 K
1 10 :
1 9 S
0 10 P
...
```

Az első telket a páros oldalon vették (házszáma: 2), 10 méter széles és már a kerítés is elkészült, amelyet P színnel festettek be. A második vásárló az első, aki a páratlan oldalon vett telket (házszáma: 1), 8 méter széles, K színű kerítése van. A harmadik vásárló is a páratlan oldalt választotta, ezért házszáma 3, 10 méteres a telke, de a kerítés még nem készült el.

Készítsen programot, amely a **_kerites.txt_** állomány adatait felhasználva az alábbi kérdésekre válaszol! A program forráskódját mentse **_utca_** néven! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például `5. feladat`)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Az ékezetmentes kiírás is elfogadott.

1. Olvassa be és tárolja el a **_kerites.txt_** fájl tartalmát!

2. Írja a képernyőre, hogy hány telket adtak el az utcában!

3. Jelenítse meg a képernyőn, hogy az utolsó eladott telek
a. melyik (páros / páratlan) oldalon talált gazdára!
b. milyen házszámot kapott!

4. Írjon a képernyőre egy házszámot a páratlan oldalról, amely melletti telken ugyanolyan színű a kerítés! (A hiányzó és a festetlen kerítésnek nincs színe.) Feltételezheti, hogy van ilyen telek, a több ilyen közül elég az egyik ház számát megjeleníteni.

5. Kérje be a felhasználótól egy eladott telek házszámát, majd azt felhasználva oldja meg a következő feladatokat!
>**a.)** Írja ki a házszámhoz tartozó kerítés színét, ha már elkészült és befestették, egyébként az állapotát a „ **#** ” vagy „ **:** ” karakter jelöli!
>**b.)** A házszámhoz tartozó kerítést szeretné tulajdonosa be- vagy átfesteni. Olyan színt akar választani, amely különbözik a mellette lévő szomszéd(ok)tól és a jelenlegi színtől is. Adjon meg egy lehetséges színt! A színt a teljes palettából (A–Z) szabadon választhatja meg.

6. Jelenítse meg az **_utcakep.txt_** fájlban a páratlan oldal utcaképét az alábbi mintának megfelelően!
```
KKKKKKKK::::::::::SSSSSSSSSBBBBBBBBFFFFFFFFFKKKKKKKKKKIIIIIIII
1       3         5        7       9        11        13
```
Az első sorban a páratlan oldal jelenjen meg, a megfelelő méternyi szakasz kerítésszínét (vagy állapotát) jelző karakterrel! A második sorban a telek első karaktere alatt kezdődően a házszám álljon!

### Minta a szöveges kimenetek kialakításához:
```
2. feladat
Az eladott telkek száma: 98

3. feladat
A páros oldalon adták el az utolsó telket.
Az utolsó telek házszáma: 78

4. feladat
A szomszédossal egyezik a kerítés színe: 73

5. feladat
Adjon meg egy házszámot! 83
A kerítés színe / állapota: A
Egy lehetséges festési szín: D
```