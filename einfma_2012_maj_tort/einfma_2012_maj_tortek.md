# Emelt Informatika Érettségi 2012 május - Törtek

## Feladat

A matematikában sokszor van szükségünk műveletvégzésre a közönséges törtekkel. A legtöbb számológép és számítógépes program csak a tizedestörteket ismeri.

Készítsen programot, amely az alábbi – közönséges törtekkel kapcsolatos – feladatokat megoldja! A program forráskódját **tort** néven mentse! A feladatban csak pozitív számokkal kell dolgoznia, és ennek a tulajdonságnak a feldolgozandó fájlban található számadatok is megfelelnek. A felhasználótól bekérendő és a feldolgozandó fájlban található számokról feltételezheti, hogy legfeljebb kétjegyűek.

Minden – képernyőre írást igénylő – részfeladat megoldása előtt írja a képernyőre a feladat sorszámát! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár (például az 1. feladat esetén: „`1. feladat Adja meg a számlálót: `”)!
Az ékezetmentes kiírás is elfogadott.

1. Kérjen be a felhasználótól két számot, amely egy közönséges tört számlálója és nevezője! Döntse el, hogy az így bevitt tört felírható-e egész számként! Ha igen, írja ki értékét egész számként, ha nem, írja ki „Nem egész”!

2. A közönséges törteket úgy tudjuk a legegyszerűbb alakra hozni, ha a számlálóját és nevezőjét elosztjuk a két szám legnagyobb közös osztójával, és az így kapott érték lesz az új számláló, illetve nevező. Az egyszerűsítéshez készítsen egy rekurzív függvényt az alább leírt euklideszi algoritmusnak megfelelően!
	```
	Függvény lnko(a, b : egész számok) : egész szám
		ha a=b akkor lnko := a
		ha a<b akkor lnko := lnko(a, b-a)
		ha a>b akkor lnko := lnko(a-b, b)
	Függvény vége
	```

3. Az első feladatban bekért törtet hozza a legegyszerűbb alakra a létrehozott függvény segítségével! Amennyiben nem sikerül az előírt függvényt elkészítenie, alkalmazhat más megoldást, hogy a további feladatokat meg tudja oldani. Az eredményt írja ki a következő formában:
	```
	24/32 = 3/4
	```
	Amennyiben a tört felírható egész számként, akkor ebben az alakban jelenjen meg:
	```
	24/6 = 4
	```
	
4. Két törtet úgy tudunk összeszorozni, hogy a két tört számlálóját összeszorozva kapjuk az eredmény számlálóját, és a két tört nevezőjét összeszorozva kapjuk az eredmény nevezőjét. Kérjen be a felhasználótól egy újabb közönséges törtet a számlálójával és a nevezőjével! Szorozza meg ezzel a törttel az első feladatban bekért törtet! Az eredményt hozza a legegyszerűbb alakra, és ezt írja ki a következő formában:
	```
	24/32 * 12/15 = 288/480 = 3/5
	```
	Amennyiben az eredmény felírható egész számként, akkor ebben az alakban jelenjen meg:
	```
	24/32 * 8/3 = 192/96 = 2
	```

5. Két közönséges tört összeadásához a következő lépésekre van szükség:
	- Mindkét számot bővíteni kell, azaz mind a számlálóját, mind a nevezőjét ugyanazzal a számmal kell megszorozni. Ezt a bővítést úgy célszerű elvégezni, hogy a közös nevező a két eredeti nevező legkisebb közös többszöröse legyen. Ez lesz az összeg      nevezője.
    - A két bővített alakú tört számlálóját összeadjuk, ez lesz az eredmény számlálója.
	
Ehhez készítsen függvényt az alábbiakban leírtak szerint – a korábban elkészített **lnko** függvény felhasználásával – a legkisebb közös többszörös meghatározására!
	```
	Függvény lkkt(a, b : egész számok) : egész szám
		lkkt := a * b / lnko(a, b)
	Függvény vége
	```

6. A függvény segítségével határozza meg a két bekért tört összegét, és ezt adja meg a következő formában! (Amennyiben nem sikerül az előírt függvényt elkészítenie, alkalmazhat más megoldást, hogy a további feladatokat meg tudja oldani.)
	```
	24/32 + 8/3 = 72/96 + 256/96 = 328/96 = 41/12
	```
	Amennyiben az eredmény felírható egész számként, akkor ebben az alakban jelenjen meg:
	```
	22/4 + 27/6 = 66/12 + 54/12 = 120/12 = 10
	```

7. Az **adat.txt** állományban található műveleteket végezze el, és az eredményeket a korábbi, képernyőre kiírt formátumnak megfelelően írja az **eredmeny.txt** állományba! Az **adat.txt** fájlnak legfeljebb 100 sora lehet; soronként 4 számot és egy műveleti jelet tartalmaz, melyeket mindenhol egy szóköz választ el egymástól. Műveleti jelként csak összeadás és szorzás szerepel.
Például:
	**adat.txt**:
	```
	24 32 8 3 +
	24 32 8 3 *
	```
	**eredmeny.txt**:
	```
	24/32 + 8/3 = 72/96 + 256/96 = 328/96 = 41/
	24/32 * 8/3 = 192/96 = 2
	```
