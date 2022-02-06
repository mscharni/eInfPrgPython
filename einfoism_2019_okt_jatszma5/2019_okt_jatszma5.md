# Emelt Informatika Érettségi - 2019 Október - Játszma5

## Feladat
A tenisz történetének leghosszabb wimbledoni játszmája 2010-ben _John Isner_ és _Nicolas Mahut_ közötti 5. játszma (szett) volt, ahol a szokásos 6-12 játék (game) helyett több mint 100 játékon keresztül küzdöttek egymással a teniszezők.

Ebben a feladatban az **5. játszma adatai** alapján kell új információkat meghatároznia. Mivel a teniszjáték szabályai és pontozása meglehetősen összetett, így ezeket egyszerűsítve a feladatoknál írjuk le.

A feladatok megoldása során vegye figyelembe a következőket:
- A program készítése során törekedjen az objektum orientált (OOP) megoldásra, amire a feladatsor ajánlásokat is tartalmaz. Amennyiben a programot ilyen módon nem tudja elkészíteni, akkor a feladatokat saját osztály létrehozása nélkül is megoldhatja, de így kevesebb pontot ér a megoldása. Ebben az esetben, ha a feladat jellemző vagy metódus létrehozását kéri, akkor Önnek saját alprogramot (függvényt, eljárást) kell készítenie, amely_ **_paramétereken keresztül_** kommunikál a hívó programmal!
- A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például:_ 4. feladat:_)!
- Az egyes feladatokban a kiírásokat a minta szerint készítse el!
- Az azonosítóknál és a kiírásnál ékezetmentes karaktereket is használhat!
- A megoldását úgy készítse el, hogy az azonos szerkezetű, de tetszőleges input adatok mellett is megfelelően működjön!

1. Készítsen programot a következő feladatok megoldására, amelynek a forráskódját Játszma5 néven mentse el!

2. A játszma legkisebb pontozható egysége a labdamenet. Az 5. játszma labdameneteinek eredménye a labdamenetek5.txt szöveges állományban áll rendelkezésünkre a következők szerint:
	- a labdamenetet „ **A** ” betűvel kódoltuk, ha azt **adogató** játékos nyerte
	- a labdamenetet „ **F** ” betűvel kódoltuk, ha azt a **fogadó** játékos nyerte
	- soronként egy-egy labdamenet eredménye található **időrendben**
	- az állományban kódolt utolsó labdamenet az 5. játszma végét jeleni
	- az állományban lévő adatok értelmezéséhez egy táblázatot is készítettünk a feladat végén
Olvassa be a labdamenetek eredményeit a labdamenetek5.txt állományból és tárolja egy összetett adatszerkezetben!

3. Számolja meg és írja ki a minta szerint a labdamenetek számát!

4. A teniszben a labdamenetet gyakran az adogató játékos nyeri. Határozza meg és írja ki, hogy az adogató játékos hány százalékát nyerte meg a labdameneteknek!

5. Határozza meg és írja ki a minta szerint, hogy hány adogatásból állt az a leghosszabb sorozat, melyben mindig az adogató játékos nyert!


6. Játék osztály
a. Minden játszma játékokból áll, mely játékok általában 4-12 labdamenetnél nem hosszabbak. Hozzon létre saját osztályt egy játék adatainak tárolására Játék azonosítóval!
b. Egy játék aktuális eredményét a továbbiakban állás nak nevezzük. Az osztály adattagjai legyenek alkalmasak az állás (például: „AFAA”), az adogató játékos és a fogadó játékos neveinek a tárolására!
c. Készítsen a Játék osztályba konstruktort, ami paramétereken keresztül az adogató és a fogadó játékos nevét, valamint a játék aktuális állását állítja be! A konstruktorban további adattagok inicializálását is elvégezheti!
d. Készítsen metódust Hozzáad azonosítóval, ami egy paraméterben átadott labdamenet eredményét („A” vagy „F”) adja majd hozzá az aktuális játék állásához!
e. Készítsen metódust NyertLabdamenetekSzáma azonosítóval, mely segítségével a paraméterben kódolt adogató („A”) vagy fogadó („F”) játékos által megnyert labdamenetek számát határozza meg az aktuális állásból!
f. Mivel a forrás állományban nincs ténylegesen jelezve egy-egy játék vége, ezért készítsen logikai értékkel visszatérő metódust vagy jellemzőt JátékVége azonosítóval, ami a tárolt állás alapján meghatározza, hogy befejeződött-e az aktuális játék vagy még folyamatban van! A metódust a következő algoritmus szerint kódolja:
	```
	Függvény JátékVége(): logikai
		Változó nyertAdogató: egész
		Változó nyertFogadó: egész
		Változó különbség: egész
		nyertAdogató := NyertLabdamenetekSzáma(’A’)
		nyertFogadó := NyertLabdamenetekSzáma(’F’)
		különbség := AbszolútÉrték (nyertAdogató – nyertFogadó)
		Térj vissza (nyertAdogató >= 4 VAGY nyertFogadó >=4) ÉS (különbség >= 2)
	Függvény vége
	```
g. Az osztályt tetszőlegesen további tagokkal bővítheti a feladatok megoldásához!
h. A további feladatok megoldásához javasolt az osztályban definiált metódusok (jellemzők) alkalmazása!

7. Hozzon létre egy példányt a Játék osztályból PróbaJáték azonosítóval az osztály teszteléséhez. Inicializálja a példányt az alábbi adatokkal:
	```
    **adogató: ’Mahut’, fogadó: ’Isner’, állás: ’FAFAA’**
	```
    A Hozzáad metódus hívásával adja hozzá az aktuális álláshoz egy labdamenet eredményét, amiben az adogató nyert. Ezt követően írja ki a minta szerint az új állást és hogy befejeződött-e a próbajáték. Utóbbihoz használja a JátékVége metódust!
	
8. Egy játékokon belül mindig ugyanaz a teniszező adogat, majd amikor a játék befejeződik, akkor a következő játék során az adogatás joga a másik versenyzőre száll az eredménytől függetlenül. Hozzon létre egy Játék osztálypéldányt, majd töltse fel a Hozzáad metódus hívásával/hívásaival az **5. játszma** első játékának állásával! Ha az osztálypéldányban tárolt állás alapján az aktuális játéknak vége, azaz a JátékVége metódus igaz értékkel tér vissza, akkor mentse el az osztálypéldányt egy összetett adatszerkezetben, majd folytassa hasonlóan az 5. játszma többi játékának a feldolgozásával! A feladat megoldásához lényeges, hogy az 5. játszma 1. játéka **Isner** adogatásával kezdődik. Feltételezheti, hogy a labdamenetek5.txt állomány utolsó karaktere az 5. játszma utolsó játékának utolsó labdamenetét kódolja!

9. Számolja meg és írja ki a minta szerint, hogy az 5. játszmában hány játékot nyertek a teniszezők külön-külön! Egy játékot az a teniszező nyert meg, akinek több megnyert labdamenete volt az adott játékban!

### Minta a szöveges kimenetek kialakításához:
	```
	3. feladat: Labdamenetek száma:711

	4. feladat: Az adogató játékos 79.465541%-ban nyerte meg a lapdameneteket.

	5. feladat: Leghosszabb sorozat:23

	7. feladat: A próba játék
	Állás: FAFAAA
	Befejeződött a játék: igen

	9. feladat: Az 5. játszma végeredménye:
	Mahut: 68
	Isner: 70
	```

### A labdamenetek5.txt állomány értelmezése:
	**A** _1. játék, adogat: Isner, fogad: Mahut, az adogató nyeri a labdamenetet (1:0)_
	**F** _1. játék, adogat: Isner, fogad: Mahut, a fogadó nyeri a labdamenetet   (1:1)_
	**A** _1. játék, adogat: Isner, fogad: Mahut, az adogató nyeri a labdamenetet (2:1)_
	**A** _1. játék, adogat: Isner, fogad: Mahut, az adogató nyeri a labdamenetet (3:1)_
	**A** _1. játék, adogat: Isner, fogad: Mahut, az adogató nyeri a labdamenetet (4:1) és a játékot_
	**F** _2. játék, adogat: Mahut, fogad: Isner, a fogadó nyeri a labdamenetet   (0:1)_
	**A** _2. játék, adogat: Mahut, fogad: Isner, az adogató nyeri a labdamenetet (1:1)_
	**F** _2. játék, adogat: Mahut, fogad: Isner, a fogadó nyeri a labdamenetet   (1:2)_
	**A** _2. játék, adogat: Mahut, fogad: Isner, az adogató nyeri a labdamenetet (2:2)_
	**A** _2. játék, adogat: Mahut, fogad: Isner, az adogató nyeri a labdamenetet (3:2)_
	**A** _2. játék, adogat: Mahut, fogad: Isner, az adogató nyeri a labdamenetet (4:2) és a játékot_
	**A** _3. játék, adogat: Isner, fogad: Mahut, az adogató nyeri a labdamenetet (1:0)_
	**... ...**


