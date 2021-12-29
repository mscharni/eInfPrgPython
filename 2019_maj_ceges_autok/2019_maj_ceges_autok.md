# Emelt Informatika Érettségi - 2019 május - Céges autók

## Online forráskódok
1. [Megoldás váz](https://replit.com/@mscharni/2019majcegesautokstarter)
2. [Megoldás](https://replit.com/@mscharni/2019majcegesautok)

## Feladat
Egy cég 10 olyan autóval rendelkezik, amelyet a dolgozók igénybe vehetnek az üzleti ügyeik intézésére. Az autókat akár többnapos útra is elvihetik, illetve egy autót egy nap több dolgozó is elvihet. A rendszer az autók parkolóból való ki- és behajtását rögzíti. A parkoló a hónap minden napján 7-23 óra között van nyitva, csak ebben az időszakban lehet elvinni és visszahozni az autókat. Az autót mindig annak a dolgozónak kell visszahoznia, amelyik elvitte. Egyszerre csak egy autó lehet minden dolgozónál.

Az **_autok.txt_** fájl egy hónap (30 nap) adatait rögzíti. Egy sorban szóközökkel elválasztva 6 adat található az alábbi sorrendben.

| nap | egész szám (1-30) | a hónap adott napja |
| --- |--- | --- |
| óra:perc | szöveg (óó:pp formátumban) | a ki- vagy a behajtás időpontja |
| rendszám | 6 karakteres szöveg (CEG300-CEG309) | az autó rendszáma
| személy azonosítója | egész szám (500-600) | az autót igénybe vevő dolgozó azonosítója |
| km számláló | egész szám | a km számláló állása |
| ki/be hajtás | egész szám (0 vagy 1)|  a parkolóból kihajtáskor 0, a behajtáskor 1 |

A sorok száma legfeljebb 500. Az adatok a napok szerint, azon belül óra és perc szerint rendezettek. Továbbá tudjuk, hogy a hónap első napján a cég mind a tíz autója a parkolóban volt.

### Például:
```
...
5 07:30 CEG300 590 30580 0
5 14:16 CEG300 590 30656 1
5 17:00 CEG300 534 30656 0
5 19:03 CEG300 534 30784 1
...
15 09:53 CEG308 543 35048 0
17 11:16 CEG308 543 35746 1
```

A példában látható, hogy a CEG300 rendszámú autót az 5. napon kétszer is elvitték. Először 7:30-kor vitték el és 14:16-kor hozta vissza az 590-es dolgozó. A kivitelkor a kilométerszámláló állása 30 580 km volt, amikor visszahozta 30 656 km volt. Másodszor 17:00-kor vitte el az 534-es dolgozó az autót és 19:03-kor hozta vissza. A CEG308 rendszámú autót pedig a 15. napon vitte el az 543-as dolgozó és a 17. napon hozta vissza.

Készítsen programot, amely az **_autok.txt_** állomány adatait felhasználva az alábbi kérdésekre válaszol! A program forráskódját mentse **_cegesauto_** néven! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: `3. feladat`)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Az ékezetmentes kiírás is elfogadott.

Az eredmény megjelenítését és a felhasználóval való kommunikációt a feladatot követő minta alapján valósítsa meg!

1. Olvassa be és tárolja el az **_autok.txt_** fájl tartalmát!

2. Adja meg, hogy melyik autót vitték el utoljára a parkolóból! Az eredményt a mintának megfelelően írja a képernyőre!

3. Kérjen be egy napot és írja ki a képernyőre a minta szerint, hogy mely autókat vitték ki és hozták vissza az adott napon!

4. Adja meg, hogy hány autó nem volt bent a hónap végén a parkolóban!

5. Készítsen statisztikát, és írja ki a képernyőre mind a 10 autó esetén az ebben a hónapban megtett távolságot kilométerben! A hónap végén még kint lévő autók esetén az utolsó rögzített kilométerállással számoljon! A kiírásban az autók sorrendje tetszőleges lehet.

6. Határozza meg, melyik személy volt az, aki az autó egy elvitele alatt a leghosszabb távolságot tette meg! A személy azonosítóját és a megtett kilométert a minta szerint írja a képernyőre! (Több legnagyobb érték esetén bármelyiket kiírhatja.)

7. Az autók esetén egy havi menetlevelet kell készíteni! Kérjen be a felhasználótól egy rendszámot! Készítsen egy **_X_menetlevel.txt_** állományt, amelybe elkészíti az adott rendszámú autó menetlevelét! (Az **X** helyére az autó rendszáma kerüljön!) A fájlba soronként **tabulátorral** elválasztva a személy azonosítóját, a kivitel időpontját (nap. óra:perc), a kilométerszámláló állását, a visszahozatal időpontját (nap. óra:perc), és a kilométerszámláló állását írja a minta szerint! (**A tabulátor karakter ASCII-kódja: 9.**)

## Minta a szöveges kimenetek kialakításához:

```
2. feladat
30. nap rendszám: CEG300

3. feladat
Nap: 4
Forgalom a(z) 4. napon:
12:50 CEG303 561 ki
19:17 CEG308 552 be

4. feladat
A hónap végén 4 autót nem hoztak vissza.

5. feladat
CEG300 6751 km
CEG301 5441 km
CEG302 5101 km
CEG303 7465 km
CEG304 6564 km
CEG305 5232 km
CEG306 7165 km
CEG307 6489 km
CEG308 6745 km
CEG309 1252 km

6. feladat
Leghosszabb út: 1551 km, személy: 506

7. feladat
Rendszám: CEG304
Menetlevél kész.
```

### A _CEG304_menetlevel.txt_ fájl tartalma:
```
...
588	21.	16:58	13452 km	23. 20:28	14335 km
512	24.	16:58	14335 km	26. 22:21	15041 km
504	27.	13:47	15041 km
```