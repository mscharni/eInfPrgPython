# Emelt Informatika Érettségi - 2017 május - Tesztverseny

## Feladat
Egy közismereti versenyen a versenyzőknek 13+1, azaz összesen 14 tesztfeladatot tűznek ki. A versenyzőknek minden feladat esetén négy megadott lehetőség (**A**, **B**, **C**, **D**) közül kell a helyes választ megjelölniük. A versenybizottság garantálja, hogy tesztlapon minden kérdéshez pontosan egy helyes válasz tartozik. A kitöltött tesztlapokat elektronikusan rögzítik, a visszaélések elkerülése végett a versenyzőket betűkből és számokból álló kóddal azonosítják.

A helyes megoldást és a versenyzők válaszait a **_valaszok.txt_** szöveges állomány tartalmazza. A fájlban legfeljebb 500 versenyző adatai szerepelnek. A fájl első sorában a helyes válaszok szerepelnek. A fájl többi sora a versenyzők kódjával kezdődik, ezt egy szóköz, majd az adott versenyző által adott válaszok sorozata követi. A versenyzők kódja legfeljebb 5 karakterből áll. A válaszok a feladatokkal egyező sorrendben, elválasztójel nélkül, nagybetűvel szerepelnek. Ha a versenyző egy kérdésre nem válaszolt, akkor annak helyén **X** betű szerepel. Például:

```
BCCCDBBBBCDAAA
AB123 BXCDBBACACADBC
AH97 BCACDBDDBCBBCA
...
```

A 2. kérdésre a helyes válasz a C volt, de erre a kérdésre az AB123 kódú versenyző nem válaszolt.

Készítsen programot **_tesztverseny_** néven az alábbi feladatok megoldására! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: `2. feladat:`)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! A képernyőn megjelenő üzenetek az adott környezet nyelvi sajátosságainak megfelelően a mintától eltérhetnek (pl. ékezetmentes betűk, tizedespont használata).

1. Olvassa be és tárolja el a **_valaszok.txt_** szöveges állomány adatait!

2. Jelenítse meg a képernyőn a mintának megfelelően, hogy hány versenyző vett részt a tesztversenyen!

3. Kérje be egy versenyző azonosítóját, és jelenítse meg a mintának megfelelően a hozzá eltárolt válaszokat! Feltételezheti, hogy a fájlban létező azonosítót adnak meg.

4. Írassa ki a képernyőre a helyes megoldást! A helyes megoldás alatti sorba „**+**” jelet tegyen, ha az adott feladatot az előző feladatban kiválasztott versenyző eltalálta, egyébként egy **szóköz**t! A kiírást a mintának megfelelő módon alakítsa ki!

5. Kérje be egy feladat sorszámát, majd határozza meg, hogy hány versenyző adott a feladatra helyes megoldást, és ez a versenyzők hány százaléka! A százalékos eredményt a mintának megfelelően, két tizedesjeggyel írassa ki!

6. A verseny feladatai nem egyenlő nehézségűek: az 1-5. feladat 3 pontot, a 6-10. feladat 4 pontot, a 11-13. feladat 5 pontot, míg a 14. feladat 6 pontot ér. Határozza meg az egyes versenyzők pontszámát, és a listát írassa ki a _pontok.txt_ nevű állományba! Az állomány minden sora egy versenyző kódját, majd szóközzel elválasztva az általa elért pontszámot tartalmazza!

7. A versenyen a három legmagasabb pontszámot elérő összes versenyzőt díjazzák. Például 5 indulónál előfordulhat, hogy 3 első és 2 második díjat adnak ki. Így megtörténhet az is, hogy nem kerül sor mindegyik díj kiadására. Írassa ki a mintának megfelelően a képernyőre a díjazottak kódját és pontszámát pontszám szerint csökkenő sorrendben!

## Minta a szöveges kimenetek kialakításához:

(A képernyőre írt üzeneteknek tartalmilag meg kell felelniük az alábbi mintának.
Képernyőre írást nem igénylő feladatok esetén nem szükséges a feladat számát sem kiíratnia.)

```
1. feladat: Az adatok beolvasása

2. feladat: A vetélkedőn 303 versenyző indult.

3. feladat: A versenyző azonosítója = AB123
BXCDBBACACADBC (a versenyző válasza)

4. feladat:
BCCCDBBBBCDAAA (a helyes megoldás)
+ +  +   +     (a versenyző helyes válaszai)

5. feladat: A feladat sorszáma = 10
A feladatra 111 fő, a versenyzők 36,63%-a adott helyes választ.

6. feladat: A versenyzők pontszámának meghatározása

7. feladat: A verseny legjobbjai:
1. díj (56 pont): JO001
2. díj (52 pont): DG490
2. díj (52 pont): UA889
3. díj (49 pont): FX387
```