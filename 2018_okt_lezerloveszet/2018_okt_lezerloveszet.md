# Emelt Informatika Ismeretek - 2018 Október - Lézerlövészet

## Feladat

Egy baráti társaságban népszerű szórakozás a lézerlövészet, ahol a játékosok elektronikus fegyverrel lőnek virtuális céltáblára. Mivel csak egy fegyverük van, így minden lövés előtt kockadobással határozzák meg a soron következő játékost. A kockadobásban mindenki részt vesz, így egymás után akár több lövést is leadhat egy-egy játékos.

Ebben a feladatban a lövések adataiból kell új információkat meghatároznia. A **lovesek.txt** forrásállomány első sora tartalmazza a virtuális céltábla középpontjának koordinátáit (valós értékek). A második sortól időrendben a játékosok lövéseinek az adatai találhatók. A játékos nevét a lövésének x-y koordinátái (valós értékek) követik, az adatokat pontosvesszővel választottuk el:

A megoldás során vegye figyelembe a következőket:
- A program készítése során törekedjen az objektum orientált (OOP) megoldásra, amire a feladatsor ajánlásokat is tartalmaz. Amennyiben a programot ilyen módon nem tudja elkészíteni, akkor a feladatokat saját osztály létrehozása nélkül is megoldhatja, de így kevesebb pontot ér a megoldása. Ebben az esetben, ha a feladat jellemző vagy metódus létrehozását kéri, akkor Önnek saját alprogramot (függvényt, eljárást) kell készítenie, amely **_paramétereken keresztül_** kommunikál a hívó programmal!
	- A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például:_ 5. feladat: _)!
	- Az egyes feladatokban a kiírásokat a minta szerint készítse el!
	- A megoldását úgy készítse el, hogy az azonos szerkezetű, de tetszőleges input adatok mellett is megfelelően működjön!

1. Készítsen programot a következő feladatok megoldására, amelynek a forráskódját **LezerLoveszet** néven mentse el!

2. Hozzon létre saját osztályt JatekosLovese azonosítóval és definiáljon benne adattagokat a játékos nevének és egy lövés koordinátáinak eltárolására! A lövéseket sorszámmal kell majd ellátni, így ehhez is készítsen adattagot!

3. Készítse el az osztály konstruktorát, ami a forrásállomány egy sora alapján rögzíti a játékos nevét, a lövés koordinátáit és a lövés sorszámát. A forrásállomány egy sora és a lövés sorszáma legyenek a konstruktor paraméterei!

4. Olvassa be a lovesek.txt állományban található adatokat és tárolja el őket! A játékosok lövéseit tárolja tömbben vagy listában, melynek a típusa JatekosLovese legyen!

5. Határozza meg és írja ki a minta szerint, hogy a játékosok hány lövést adtak le a játék során!

6. Készítsen Tavolsag azonosítóval valós típusú kódtagot (jellemzőt, metódust, stb.) a JatekosLovese osztályban, mellyel meghatározza a céltábla koordinátái és a lövés koordinátái közötti távolságot a következő algoritmus szerint:
	```
    változó dx: valós := CéltáblaX - LövésX;
    változó dy: valós := CéltáblaY - LövésY;
    térj vissza Gyök(Négyzet(dx) + Négyzet(dy))
	```
A céltábla koordinátáit átadhatja a kódtag paraméterében vagy tárolhatja az osztályban statikus típusú adattagként!

7. Határozza meg a céltábla középpontjához legközelebb eső (legpontosabb) lövés adatait és írja ki a minta szerint! Feltételezheti, hogy csak egy ilyen lövés van!

8. Készítsen Pontszam azonosítóval valós típusú kódtagot (jellemzőt, metódust, stb.) a JatekosLovese osztályban, mellyel meghatározza egy-egy lövés pontszámát! A pontszámot a **10 - Tavolsag** képlettel határozza meg! A pontszámot két tizedesjegyre kell a kódtagnak kerekítenie! Negatív pontszám nem lehet, ilyenkor a kódtag nulla értékkel térjen vissza!

9. Határozza meg és írja ki a minta szerint a nulla pontos lövések számát!

10. Számolja meg és írja ki a képernyőre a játékban részvevő játékosok számát a minta szerint!

11. Határozza meg játékosonként a leadott lövések számát! Megoldását úgy készítse el, hogy a játékosok nevei és száma nem ismert, de feltételezheti, hogy a számuk 2 és 10 fő közötti!

12. Számítsa ki az átlagpontszámokat, majd jelenítse meg a minta szerint!

13. Határozza meg a legmagasabb átlagpontszám alapján a nyertes játékos nevét! Feltételezheti, hogy nem alakult ki holtverseny.

### Minta a szöveges kimenetek kialakításához:
	```
	5. feladat: lövések száma:65

	7. feladat: Legpontosabb lövés:
	52.; Ricsi; x=29.39; y= 31.08; távolság=0.6811754546370593

	9. feladat: Nulla pontos lövések száma: 14 db

	10. feladat: Játékosok száma: 3

	11. feladat: Lövések száma
	Ricsi - 16 db
	Pali - 29 db
	Gabi - 20 db

	12. feladat: Átlagpontszámok
	Ricsi - 4.49625
	Pali - 4.27448275862069
	Gabi - 3.1215

	13. feladat: A játék nyertese: Ricsi
	```
