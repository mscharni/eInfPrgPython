# Emelt Informatika Érettségi - 2011 május - Szójáték

## Feladat
Sok szórakoztató szójátékkal lehet elütni az időt. Ezek közül némelyekhez segítségül hívhatjuk a technikát is. Az alábbiakban szójátékokhoz kapcsolódó problémákat kell megoldania.

A feladatok megoldásához rendelkezésére áll a **_szoveg.txt_** fájl, amelybe Gárdonyi Géza Egri csillagok című regényéből gyűjtöttünk ki szavakat. Az állományban csak olyan szavak szerepelnek, melyek az angol ábécé betűivel leírhatók, és minden szó csak egyszer szerepel. A könnyebb feldolgozhatóság érdekében valamennyi szó csupa kisbetűvel szerepel, szavanként külön sorban. Tudjuk, hogy ebben az állományban a szavak 20 karakternél nem hosszabbak.

Készítsen programot, amely az alábbi feladatokat megoldja! A program forráskódját **_szavak_** néven mentse!

Minden – képernyőre írást igénylő – részfeladat megoldása előtt írja a képernyőre a feladat sorszámát! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár (például a 1. feladat esetén: „`1. feladat Adjon meg egy szót: `”)! Az ékezetmentes
kiírás is elfogadott.

1. Kérjen be a felhasználótól egy szót, és döntse el, hogy tartalmaz-e magánhangzót! Amennyiben tartalmaz, írja ki, hogy „`Van benne magánhangzó.`”! Ha nincs, akkor írja ki, hogy „`Nincs benne magánhangzó.`”! A begépelendő szóról feltételezheti, hogy csak az angol ábécé kisbetűit tartalmazza. (Az angol ábécé magánhangzói: a, e, i, o, u.)

2. Írja ki a képernyőre, hogy melyik a leghosszabb szó a **_szoveg.txt_** állományban, és az hány karakterből áll! Ha több azonos leghosszabb hosszúságú szó is van a szógyűjteményben, akkor azok közül elegendő egyetlen szót kiírnia. A feladatot úgy oldja meg, hogy tetszőleges hosszúságú szövegállomány esetén működjön, azaz a teljes szöveget ne tárolja a memóriában!

3. A magyar nyelv szavaiban általában kevesebb a magánhangzó, mint a mássalhangzó. Határozza meg, hogy az állomány mely szavaiban van több magánhangzó, mint egyéb karakter! Ezeket a szavakat írja ki a képernyőre egy-egy szóközzel elválasztva! A szavak felsorolása után a mintának megfelelően az alábbi adatokat adja meg:
- hány szót talált;
- hány szó van összesen az állományban;
- a talált szavak hány százalékát teszik ki az összes szónak!
A százalékot két tizedessel szerepeltesse!
Például:
`130/3000 : 4,33%`

A következőkben a szólétra játékkal kapcsolatos feladatokat kell megoldania.

A szólétra építés egy olyan játék, amikor adott egy szó közepe, például *_isz_* , amit a létra fokának nevezünk. Ennek a szócsonknak az elejére és a végére kell egy-egy betűt illesztenünk úgy, hogy értelmes szót hozzunk létre, például *_hiszi_* vagy *_liszt_*. Ezt az értelmes szót a játékban létraszónak nevezzük. Az adott szórészlethez minél több létraszót tudunk kitalálni, annál magasabb lesz a szólétra. A cél az, hogy egy megadott szócsonkhoz a lehető legmagasabb szólétrát építsük.
### Például:
Szórészlet: **isz**
A hozzá tartozó létraszavak:
h **isz** i
l **isz** t
v **isz** i
t **isz** t
...

4. Hozzon létre egy tömb vagy lista adatszerkezetet, és ebbe gyűjtse ki a fájlban található ötkarakteres szavakat! A **_szoveg.txt_** állomány legfeljebb 1000 darab ötkarakteres szót tartalmaz. Kérjen be a felhasználótól egy 3 karakteres szórészletet! Írja ki a képernyőre a szólétra építés szabályai szerint hozzá tartozó ötkarakteres szavakat a tárolt adathalmazból! A kiírásnál a szavakat egy-egy szóköz válassza el! (Teszteléshez használhatja például az **„isz”** vagy **„obo”** szórészleteket, mert ezekhez a megadott szövegállományban több létraszó is tartozik.)

5. Az eltárolt ötkarakteres szavakból csoportosítsa azokat a szavakat, melyek ugyanannak a hárombetűs szórészletnek a létraszavai! Hozzon létre egy **_letra.txt_** állományt, amelybe ezeket a szavakat írja az alábbiak szerint:
- minden szó külön sorba kerüljön;
- csak olyan szó szerepeljen az állományban, aminek van legalább egy párja, amivel egy létrát alkotnak (azaz első és utolsó karakter nélkül megegyeznek);
- az egy létrához tartozó szavak közvetlenül egymás után helyezkedjenek el;
- két létra szavai között egy üres elválasztó sor legyen!
### Például:
**letra.txt**
```
megye
vegye
hegyi
tegye
```
```
lehet
teher
mehet
```
```
tejes
fejet
fejen
```
```
neked
nekem
reked
...
```