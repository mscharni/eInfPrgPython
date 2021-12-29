# Emelt Informatika Érettségi - 2021 május - Gödrök

## Online forráskódok
1. [Megoldás váz](https://replit.com/@mscharni/2021majgodrokstarter)
2. [Megoldás](https://replit.com/@mscharni/2021majgodrok)

## Feladat
Egy teljesen sík terepen a talaj olyan anyagból van, ami nem ereszti át a vizet. Ezen a területen egy egyenes mentén munkagépekkel 10 méter széles csatornát építenek. A munka még nem készült el, ezért a csatorna mélysége nem állandó, helyenként a felszín is érintetlen. A már elkészült résszel, mint különálló gödrök sorozatával foglalkozik a feladat. Az egyszerűbb kezelés érdekében a gödröket úgy tekintjük, hogy oldalfaluk függőleges, teljes szélességben azonos mélységű, így a keresztmetszeti kép jól leírja a terepviszonyokat.

A **_melyseg.txt_** fájlban méterenként rögzítették, hogy azon a szakaszon milyen mélyen van a gödör alja. Minden sor egy-egy egész számot tartalmaz, amely a mélység értékét mutatja – szintén méterben. A fájl legfeljebb 2000 számot tartalmaz, értékük legfeljebb 30 lehet. Tudjuk, hogy az első és az utolsó méteren sértetlen a felszín, tehát ott biztosan a 0 szám áll.
### Például:

| 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 4 | 4 | 3 | 2 | 2 | 3 | 3 | 4 | 4 | 3 | 2 | 2 | 0 | 0 | 0 | 2 | 2 | 2 | 0 | 0 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|   |   |   |   |   |   | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ |   |   |   | █ | █ | █ |   |   |
|   |   |   |   |   |   | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ |   |   |   | █ | █ | █ |   |   |
|   |   |   |   |   |   |   |   |   |   | █ | █ | █ |   |   | █ | █ | █ | █ | █ |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | █ | █ |   |   |   |   |   | █ | █ |   |   |   |   |   |   |   |   |   |   |   |

A fenti példában látható keresztmetszeti képen a **_melyseg.txt_** bemeneti fájl tartalmának a kezdete látható. Az egyszerűbb szemléltetés miatt a forrásfájlban külön sorokban szereplő értékeket itt az ábrán egymás mellett szerepeltetjük. Leolvasható, hogy az első méteren 0 a mélység. Az első gödör a 7. méteren kezdődik. Az első gödör 16 méter hosszan tart, legnagyobb mélysége 4 méter, térfogata 440 m<sup>3</sup>. A második gödör a 26. méternél kezdődik, 3 méter hosszan tart, térfogata 60 m<sup>3</sup>.

Készítsen programot, amely a **_melyseg.txt_** állományt felhasználva az alábbi kérdésekre válaszol! A program forráskódját mentse **_godor_** néven! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: `2. feladat`)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Az ékezetmentes kiírás is elfogadott.

1. Olvassa be és tárolja el a **_melyseg.txt_** fájl tartalmát! Írja ki a képernyőre, hogy az adatforrás hány adatot tartalmaz!

2. Olvasson be egy távolságértéket, majd írja a képernyőre, hogy milyen mélyen van a gödör alja azon a helyen! Ezt a távolságértéket használja majd a 6. feladat megoldása során is!

3. Határozza meg, hogy a felszín hány százaléka maradt érintetlen és jelenítse meg 2 tizedes pontossággal!

4. Írja ki a **_godrok.txt_** fájlba a gödrök leírását, azaz azokat a számsorokat, amelyek egy-egy gödör méterenkénti mélységét adják meg! Minden gödör leírása külön sorba kerüljön! Az állomány pontosan a gödrök számával egyező számú sort tartalmazzon!

A godrok.txt fájl első két sorának tartalma:
```
2 2 2 2 4 4 3 2 2 3 3 4 4 3 2 2
2 2 2
...
```

5. Határozza meg a gödrök számát és írja a képernyőre!

6. Ha a 2. feladatban beolvasott helyen nincs gödör, akkor „`Az adott helyen nincs gödör.`” üzenetet jelenítse meg, ha ott gödör található, akkor határozza meg, hogy
a.) mi a gödör kezdő és végpontja! A meghatározott értékeket írja a képernyőre! (Ha nem tudja meghatározni, használja a további részfeladatoknál a 7 és 22 értéket, mint a kezdő és a végpont helyét)
b.) a legmélyebb pontja felé mindkét irányból folyamatosan mélyül-e! Azaz a gödör az egyik szélétől monoton mélyül egy pontig, és onnantól monoton emelkedik a másik széléig. Az eredménytől függően írja ki a képernyőre a „`Nem mélyül folyamatosan.`” vagy a „`Folyamatosan mélyül.`” mondatot!
c.) mekkora a legnagyobb mélysége! A meghatározott értéket írja a képernyőre!
d.) mekkora a térfogata, ha szélessége minden helyen 10 méternyi! A meghatározott értéket írja a képernyőre!
e.) a félkész csatorna esőben jelentős mennyiségű vizet fogad be. Egy gödör annyi vizet képes befogadni anélkül, hogy egy nagyobb szélvihar hatására se öntsön ki, amennyi esetén a víz felszíne legalább 1 méter mélyen van a külső felszínhez képest. Írja a képernyőre ezt a vízmennyiséget!

### Minta a szöveges kimenetek kialakításához:
```
1. feladat
A fájl adatainak száma: 694

2. feladat
Adjon meg egy távolságértéket! 9
Ezen a helyen a felszín 2 méter mélyen van.

3. feladat
Az érintetlen terület aránya 10.09%.

5. feladat
A gödrök száma: 22

6. feladat
a)
A gödör kezdete: 7 méter, a gödör vége: 22 méter.
b)
Nem mélyül folyamatosan.
c)
A legnagyobb mélysége 4 méter.
d)
A térfogata 440 m^3.
e)
A vízmennyiség 280 m^3.
