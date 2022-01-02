# Emelt Informatika Érettségi - 2007 október - Foci

## Feladat
Perec város sportéletében fontos szerepet játszanak a fiatalok nagypályás labdarúgó mérkőzései. Tavasszal minden csapat minden csapattal pontosan egy mérkőzést játszott. A folyamatosan vezetett eredménylista azonban eltűnt, így csak a mérkőzések jegyzőkönyvei álltak rendelkezésre. A jegyzőkönyveket ismételten feldolgozták, ehhez első lépésként a **_meccs.txt_** állományba bejegyeztek néhány adatot. Önnek ezzel az állománnyal kell dolgoz-
nia.

A **_meccs.txt_** állomány első sorában az állományban tárolt mérkőzések száma található. Alatta minden sorban egy-egy mérkőzés adatai olvashatók. Egy mérkőzést 7 adat ír le. Az első megadja, hogy a mérkőzést melyik fordulóban játszották le. A második a hazai, a harmadik a vendégcsapat góljainak száma a mérkőzés végén, a negyedik és ötödik a félidőben elért gólokat jelöli. A hatodik szöveg a hazai csapat neve, a hetedik a vendégcsapat neve. Az egyes adatokat egyetlen szóköz választja el egymástól. A sor végén nincs szóköz. A csapatok és a fordulók száma nem haladja meg a 20, a mérkőzések száma pedig a 400 értéket. Egy csapat sem rúgott meccsenként 9 gólnál többet. A csapatok neve legfeljebb 20 karakter hosszú, a névben nincs szóköz.

### Például:
```
112
14 1 2 0 2 Agarak Ovatosak
5 4 0 1 0 Erosek Agarak
4 0 2 0 2 Ijedtek Hevesek
8 1 1 0 0 Ijedtek Nyulak
8 3 2 3 1 Lelkesek Bogarak
13 0 1 0 1 Fineszesek Csikosak
2 1 0 0 0 Pechesek Csikosak
1 4 0 2 0 Csikosak Kedvesek
9 2 0 0 0 Nyulak Lelkesek
6 0 2 0 0 Ovatosak Nyulak
```

Az 2. sor mutatja, hogy a 14. fordulóban az otthon játszó Agarakat az Óvatosak 2-1-re megverték úgy, hogy a félidőben már vezettek 2-0-ra.

Készítsen programot, amely az alábbi kérdésekre válaszol! A program forráskódját mentse **_foci_** néven! (A program megírásakor a felhasználó által megadott adatok helyességét, érvé
nyességét nem kell ellenőriznie.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: **3. feladat:**). Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár!

1. Olvassa be a **_meccs.txt_** állományban talált adatokat, s annak felhasználásával oldja meg a következő feladatokat! Ha az állományt nem tudja beolvasni, az első 10 mérkőzés adata    it jegyezze be a programba és dolgozzon azzal!

2. Kérje be a felhasználótól egy forduló számát, majd írja a képernyőre a bekért forduló mérkőzéseinek adatait a következő formában: `Edes-Savanyu: 2-0 (1-0)`! Soronként egy mérkőzést tüntessen fel! A különböző sorokban a csapatnevek ugyanazon a pozíción kezdődjenek!
### Például:
>```
       Edes-Savanyu: 2-0 (1-0)
       Ijedtek-Hevesek: 0-2 (0-2)
       ...
```

3. Határozza meg, hogy a bajnokság során mely csapatoknak sikerült megfordítaniuk az állást a második félidőben! Ez azt jelenti, hogy a csapat az első félidőben vesztésre állt ugyan, de sikerült a mérkőzést megnyernie. A képernyőn soronként tüntesse fel a forduló sorszámát és a győztes csapat nevét!

4. Kérje be a felhasználótól egy csapat nevét, és tárolja el! A következő két feladat megoldásához ezt a csapatnevet használja! Ha nem tudta beolvasni, használja a _Lelkesek_ csapatnevet!

5. Határozza meg, majd írja ki, hogy az adott csapat összesen hány gólt lőtt és hány gólt kapott! Például: `lőtt: 23 kapott: 12`

6. Határozza meg, hogy az adott csapat otthon melyik fordulóban kapott ki először és melyik csapattól! Ha egyszer sem kapott ki (ilyen csapat például a _Bogarak_), akkor „`A csapat otthon veretlen maradt.`” szöveget írja a képernyőre!

7. Készítsen statisztikát, amely megadja, hogy az egyes végeredmények hány alkalommal fordultak elő! Tekintse egyezőnek a fordított eredményeket (például 4-2 és 2-4)! A nagyobb számot mindig előre írja! Az elkészült listát a **_stat.txt_** állományban helyezze el!
### Például:
```
       2-1: 18 darab
       4-0: 2 darab
       2-0: 19 darab
       ...
```