# Emelt Informatika Érettségi - 2012 május - Futár

## Feladat
A nagyvárosokon belül, ha csomagot gyorsan kell eljuttatni egyik helyről a másikra, akkor sokszor a legjobb választás egy kerékpáros futárszolgálat igénybevétele. A futárszolgálat a futárjainak a megtett utak alapján ad fizetést. Az egyik futár egy héten át feljegyezte fuvarjai legfontosabb adatait, és azokat eltárolta egy állományban. Az állományban az adatok rögzítése nem mindig követi az időrendi sorrendet. Azokra a napokra, amikor nem dolgozott, nincsenek adatok bejegyezve az állományba.

A fájlban legalább 10 sor van, és minden sor egy-egy út adatait tartalmazza egymástól szóközzel elválasztva. Az első adat a nap sorszáma, ami 1 és 7 közötti érték lehet. A második szám a napon belüli fuvarszám, ami 1 és 40 közötti érték lehet. Ez minden nap 1-től kezdődik, és az aznapi utolsó fuvarig egyesével növekszik. A harmadik szám az adott fuvar során megtett utat jelenti kilométerben, egészre kerekítve. Ez az érték nem lehet 30-nál nagyobb.

### Például:
```
1 1 5
1 2 9
3 2 12
1 4 3
3 1 7
...
```

A 3. sor például azt mutatja, hogy a hét harmadik napján a második fuvar 12 kilométeres távolságot jelentett.

Készítsen programot, amely a **_tavok.txt_** állomány adatait felhasználva az alábbi kérdésekre válaszol! A program forráskódját mentse **_futar_** néven! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: `3. feladat:`)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Az ékezetmentes kiírás is elfogadott.

1. Olvassa be a **_tavok.txt_** állományban talált adatokat, s annak felhasználásával oldja meg a következő feladatokat!

2. Írja ki a képernyőre, hogy mekkora volt a hét legelső útja kilométerben! Figyeljen arra, hogy olyan állomány esetén is helyes értéket adjon, amiben például a hét első napján a futár nem dolgozott!

3. Írja ki a képernyőre, hogy mekkora volt a hét utolsó útja kilométerben!

4. Tudjuk, hogy a futár minden héten tart legalább egy szabadnapot. Írja ki a képernyőre, hogy a hét hányadik napjain nem dolgozott a futár!

5. Írja ki a képernyőre, hogy a hét melyik napján volt a legtöbb fuvar! Amennyiben több nap is azonos, maximális számú fuvar volt, elegendő ezek egyikét kiírnia.

6. Számítsa ki és írja a képernyőre a mintának megfelelően, hogy az egyes napokon hány kilométert kellett tekerni!
```
1. nap: 124 km
2. nap: 0 km
3. nap: 75 km
...
```

7. A futár az egyes utakra az út hosszától függően kap fizetést az alábbi táblázatnak megfelelően:

| út hossza  | fizetés  |
| ---------: | -------: |
|  1 –  2 km |   500 Ft |
|  3 –  5 km |   700 Ft |
|  6 – 10 km |   900 Ft |
| 11 – 20 km | 1 400 Ft |
| 21 – 30 km | 2 000 Ft |

Kérjen be a felhasználótól egy tetszőleges távolságot, és határozza meg, hogy mekkora díjazás jár érte! Ezt írja a képernyőre!

8. Határozza meg az összes rögzített út ellenértékét! Ezeket az értékeket írja ki a **_dijazas.txt_** állományba nap szerint, azon belül pedig az út sorszáma szerinti növekvő sorrendben az alábbi formátumban:
```
1. nap 1. út: 700 Ft
1. nap 2. út: 900 Ft
1. nap 3. út: 2000 Ft
...
```

9. Határozza meg, és írja ki a képernyőre, hogy a futár mekkora összeget kap a heti munkájáért!
