# Emelt Informatika Érettségi - 2006 május - Fehérje

## Feladat
A fehérjék óriás molekulák, amelyeknek egy része az élő szervezetekben végbemenő folyamatokat katalizálják. Egy-egy fehérje aminosavak százaiból épül fel, melyek láncszerűen kapcsolódnak egymáshoz. A természetben a fehérjék fajtája több millió. Minden fehérje húszféle aminosav különböző mennyiségű és sorrendű összekapcsolódásával épül fel.

Az alábbi táblázat tartalmazza az aminosavak legfontosabb adatait, a megnevezéseket és az őket alkotó atomok számát (az aminosavak mindegyike tartalmaz szenet, hidrogént, oxigént és nitrogént, néhányban kén is van):


| Neve | Rövidítés | Betűjele |   C   |   H   |   O   |   N   |   S   |
| ---- | :-------: | :------: | :---: | :---: | :---: | :---: | :---: |
| Glicin | Gly | G | 2 | 5 | 2 | 1 | 0 |
| Alanin | Ala | A | 3 | 7 | 2 | 1 | 0 |
| Arginin | Arg | R | 6 | 14 | 2 | 4 | 0 |
| Fenilalanin | Phe | F | 9 | 11 | 2 | 1 | 0 |
| Cisztein | Cys | C | 3 | 7 | 2 | 1 | 1 |
| Triptofán | Trp | W | 11 | 12 | 2 | 2 | 0 |
| Valin | Val | V | 5 | 11 | 2 | 1 | 0 |
| Leucin | Leu | L | 6 | 13 | 2 | 1 | 0 |
| Izoleucin | Ile | I | 6 | 13 | 2 | 1 | 0 |
| Metionin | Met | M | 5 | 11 | 2 | 1 | 1 |
| Prolin | Pro | P | 5 | 9 | 2 | 1 | 0 |
| Szerin | Ser | S | 3 | 7 | 3 | 1 | 0 |
| Treonin | Thr | T | 4 | 9 | 3 | 1 | 0 |
| Aszparagin | Asn | N | 4 | 8 | 3 | 2 | 0 |
| Glutamin | Gln | Q | 5 | 10 | 3 | 2 | 0 |
| Tirozin | Tyr | Y | 9 | 11 | 3 | 1 | 0 |
| Hisztidin | His | H | 6 | 9 | 2 | 3 | 0 |
| Lizin | Lys | K | 6 | 14 | 2 | 2 | 0 |
| Aszparaginsav | Asp | D | 4 | 7 | 4 | 1 | 0 |
| Glutaminsav | Glu | E | 5 | 9 | 4 | 1 | 0 |

Készítsen programot **feherje** néven, ami megoldja a következő feladatokat! Ügyeljen arra, hogy a program forráskódját a megadott helyre mentse!

1. Töltse be az **aminosav.txt** fájlból az aminosavak adatait! A fájlban minden adat külön sorban található, a fájl az aminosavak nevét nem tartalmazza. Ha az adatbetöltés nem sikerül, vegye fel a fenti táblázat alapján állandóként az első öt adatsort, és azzal dolgozzon!
Az első néhány adat:
```
Gly
G
2
5
2
1
0
Ala
A
3
7
2
1
0
```

2. Határozza meg az aminosavak relatív molekulatömegét, ha a szén atomtömege 12, a hidrogéné 1, az oxigéné 16, a nitrogéné 14 és a kén atomtömege 32! Például a Glicin esetén a relatív molekulatömeg 2·12 + 5·1 + 2·16 + 1·14 + 0·32 = 75.

A következő feladatok eredményeit írja képernyőre, illetve az **eredmeny.txt** fájlba! A kiírást a feladat sorszámának feltüntetésével kezdje (például: **_4. feladat_**)!

3. Rendezze növekvő sorrendbe az aminosavakat a relatív molekulatömeg szerint! Írja ki a képernyőre és az **eredmeny.txt** fájlba az aminosavak hárombetűs azonosítóját és a molekulatömeget! Az azonosítót és hozzátartozó molekulatömeget egy sorba, szóközzel elválasztva írja ki!

4. A **bsa.txt** a _BSA_ nevű fehérje aminosav sorrendjét tartalmazza – egybetűs jelöléssel. (A fehérjelánc legfeljebb 1000 aminosavat tartalmaz.) Határozza meg a fehérje összegképletét (azaz a C, H, O, N és S számát)! A meghatározásánál vegye figyelembe, hogy az aminosavak összekapcsolódása során minden kapcsolat létrejöttekor egy vízmolekula (H2O) lép ki! Az összegképletet a képernyőre és az **eredmeny.txt** fájlba az alábbi formában írja ki:
Például: 
`C 16321 H 34324 O 4234 N 8210 S 2231`
(Amennyiben a bsa.txt beolvasása sikertelen, helyette tárolja a G,A,R,F,C betűjeleket tízszer egymás után és a feladatokat erre a „láncra” oldja meg!)

5. A fehérjék szekvencia szerkezetét hasításos eljárással határozzák meg. Egyes enzimek bizonyos aminosavak után kettéhasítják a fehérjemolekulát. Például a Kimotripszin enzim a Tirozin (Y), Fenilalanin (W) és a Triptofán (F) után hasít.
Határozza meg, és írja ki képernyőre a Kimotripszin enzimmel széthasított BSA lánc leghosszabb darabjának hosszát és az eredeti láncban elfoglalt helyét (első és utolsó aminoavának sorszámát)! A kiíráskor nevezze meg a kiírt adatot, például: „kezdet helye:”!

6. Egy másik enzim (a Factor XI) az Arginin (R) után hasít, de csak akkor, ha Alinin (A) vagy Valin (V) követi. Határozza meg, hogy a hasítás során keletkező első fehérjelánc részletben hány Cisztein (C) található! A választ teljes mondatba illesztve írja ki a képernyőre!
