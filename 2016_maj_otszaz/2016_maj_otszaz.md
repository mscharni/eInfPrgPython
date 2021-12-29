# Emelt Informatika Érettségi - 2016 május - Ötszáz

## Online forráskódok
1. [Megoldás váz](https://replit.com/@mscharni/2016majotszazstarter)
2. [Megoldás](https://replit.com/@mscharni/2016majotszaz)

## Feladat
Egy apróságokat árusító boltban minden árucikk darabja 500 Ft. Ha egy vásárlás során valaki egy adott árucikkből több darabot is vesz, a második ára már csak 450 Ft, a harmadik pedig 400 Ft, de a negyedik és további darabok is ennyibe kerülnek, tehát az ár a harmadik ugyanazon cikk vásárlása után már nem csökken tovább.

A pénztárhoz menők kosarában legalább 1 és legfeljebb 20 darab árucikk lehet. A kosarak tartalmát a **_penztar.txt_** fájl írja le, amelyben soronként egy-egy árucikk neve vagy az **F** karakter szerepel. A fájlban legfeljebb 1000 sor lehet. Az F karakter azt jelzi, hogy az adott vásárlónak nincs már újabb árucikk a kosarában, fizetés következik. Az árucikkek neve ékezet nélküli, több szóból is állhat, hossza legfeljebb 30 karakter.

### Példa a _penztar.txt_ fájl első néhány sorára:
```
toll
F
colostok
HB ceruza
HB ceruza
colostok
toll
szatyor
csavarkulcs
doboz
F
```

A példa alapján az első vásárló összesen 1 tollat vásárolt, ezért összesen 500 Ft-ot kell fizetnie. A második vásárlás során hatféle árucikket vásároltak – a HB ceruzából és a colostokból többet is –, összesen 3900 Ft értékben.

Készítsen programot, amely a **_penztar.txt_** állomány adatait felhasználva az alábbi kérdésekre válaszol! A program forráskódját mentse **_otszaz_** néven! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, és feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: `3. feladat:`)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Az ékezetmentes kiírás is elfogadott.

1. Olvassa be és tárolja el a **_penztar.txt_** fájl tartalmát!

2. Határozza meg, hogy hányszor fizettek a pénztárnál!

3. Írja a képernyőre, hogy az első vásárlónak hány darab árucikk volt a kosarában!

4. Kérje be a felhasználótól egy vásárlás sorszámát, egy árucikk nevét és egy darabszámot! A következő három feladat megoldásánál ezeket használja fel!

Feltételezheti, hogy a program futtasásakor csak a bemeneti állományban rögzített adatoknak megfelelő vásárlási sorszámot és árucikknevet ad meg a felhasználó.

5. Határozza meg, hogy a bekért árucikkből
a. melyik vásárláskor vettek először, és melyiknél utoljára!
b. összesen hány alkalommal vásároltak!

6. Határozza meg, hogy a bekért darabszámot vásárolva egy termékből mennyi a fizetendő összeg! A feladat megoldásához készítsen függvényt **_ertek_** néven, amely a darabszámhoz a fizetendő összeget rendeli!

7. Határozza meg, hogy a bekért sorszámú vásárláskor mely árucikkekből és milyen mennyiségben vásároltak! Az árucikkek nevét tetszőleges sorrendben megjelenítheti.

8. Készítse el az **_osszeg.txt_** fájlt, amelybe soronként az egy-egy vásárlás alkalmával fizetendő összeg kerüljön a kimeneti mintának megfelelően!

### Minta a szöveges kimenetek kialakításához:
```
2. feladat
A fizetések száma: 141

3. feladat
Az első vásárló 1 darab árucikket vásárolt.

4. feladat
Adja meg egy vásárlás sorszámát! 2
Adja meg egy árucikk nevét! kefe
Adja meg a vásárolt darabszámot! 2

5. feladat
Az első vásárlás sorszáma: 5
Az utolsó vásárlás sorszáma: 139
32 vásárlás során vettek belőle.

6. feladat
2 darab vételekor fizetendő: 950

7. feladat
1 toll
1 szatyor
1 doboz
1 csavarkulcs
2 colostok
2 HB ceruza
```

### Részlet az **_osszeg.txt_** fájlból:
```
1: 500
2: 3900
3: 2300
4: 1000
5: 2500
6: 2900
7: 950
...
```