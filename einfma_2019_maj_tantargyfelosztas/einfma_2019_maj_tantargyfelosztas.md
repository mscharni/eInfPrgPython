# Emelt Informatika Érettségi - 2019 május - Tantárgyfelosztás

## Feladat

A tantárgyfelosztás a tanév tervezésének alapvető dokumentuma. A tantárgyfelosztás azt tartalmazza, hogy a tanárok a tantárgyaikat mely osztályokban, hány órában tanítják. Ebben a feladatban egy négy évfolyamos gimnázium tantárgyfelosztásának adatait kell elemeznie.

A tantárgyfelosztást ezúttal egy adatbázis-kezelő programmal előállított, egyszerű szerkezetű szöveges állományban kapja az alábbi minta szerint (Minden bejegyzést négy sor tárol.):

```
Albatrosz Aladin
biologia
9.a
2
Albatrosz Aladin
osztalyfonoki
9.a
1
...
Csincsilla Csilla
matematika
9.x
2
...
```
Az első bejegyzés megadja, hogy **Albatrosz Aladin** tanár úr biológiát (**biologia**) fog tanítani a **9.a** osztályban heti **2** órában. Ha az osztály betűjele **x**, akkor évfolyam szintű csoportról van szó. Példánkban **Csincsilla Csilla** tanárnő a **9.** évfolyam részére heti **2** órás **matematika** órát tart.
Az osztályfőnököket arról ismerhetjük fel, hogy ők tartják az osztályfőnöki ( **osztalyfonoki** ) órát.

A megoldás során felhasználhatja, hogy a fájl maximum 1000 bejegyzést (azaz legfeljebb 4000 sort) tartalmaz. Az iskolában legfeljebb 100 tanár és legfeljebb 50 osztály van, továbbá minden osztálynak pontosan egy osztályfőnöke van.

Készítsen programot, amely a **beosztas.txt** állomány adatait felhasználva az alábbi kérdésekre válaszol! A program forráskódját mentse **tanfel** néven! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, és feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok esetén – a mintához tartalmában hasonlóan – írja ki a képernyőre a feladat sorszámát (például: `3. feladat:`), és utaljon a kiírt tartalomra is! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Mindkét esetben az ékezetmentes kiírás is elfogadott.

1. Olvassa be és tárolja el a **beosztas.txt** állományban talált adatokat, és annak felhasználásával oldja meg a következő feladatokat!

2. Hány bejegyzés található az állományban? Az eredményt írassa ki a képernyőre!

3. A fenntartó számára fontos információ, hogy az iskolában hetente összesen hány tanítási óra van. Határozza meg ezt az adatot és írassa ki a képernyőre!

4. Kérje be a felhasználótól egy tanár nevét, és írassa ki a képernyőre, hogy hetente hány órában tanít!

5. Készítse el az **of.txt** fájlt, amely az osztályfőnökök nevét tartalmazza osztályonként az alábbi formában (az osztályok megjelenítésének sorrendje a mintától eltérhet):
```
    9.a - Albatrosz Aladin
    9.b - Hangya Hanna
    9.c - Zerge Zenina
    ...
```

6. Egyes osztályokban bizonyos tantárgyakat a tanulók csoportbontásban tanulnak: ekkor az adott tantárgyra és osztályra két bejegyzést is tartalmaz a tantárgyfelosztás. Kérje be egy osztály azonosítóját, valamint egy tantárgy nevét, és írassa ki a képernyőre, hogy az adott osztály a megadott tantárgyat csoportbontásban vagy osztályszinten tanulja-e! (Feltételezheti, hogy a megadott osztály tanulja a megadott tantárgyat.)

7. A fenntartó számára az is fontos információ, hogy hány tanár dolgozik az iskolában. Írassa ki ezt az adatot a képernyőre!

## Példa a szöveges kimenetek kialakításához:
```
2. feladat
A fájlban 329 bejegyzés van.

3. feladat
Az iskolában a heti összóraszám: 1016

4. feladat
Egy tanár neve = Albatrosz Aladin
A tanár heti óraszáma: 24

6. feladat
Osztály= 10.b
Tantárgy= kemia
Csoportbontásban tanulják.

7. feladat
Az iskolában 49 tanár tanít.
```
