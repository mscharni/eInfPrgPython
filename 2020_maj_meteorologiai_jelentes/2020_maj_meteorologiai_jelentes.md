# Emelt Informatika Érettségi - 2020 május - Meteorológiai jelentés

## Feladat
Az ország területén néhány városból rendszeres időközönként időjárás táviratokat küldenek. A távirat egy rövid szöveges üzenet, amely a főbb időjárási információkat tartalmazza. Rendelkezésünkre áll az ország területéről egy adott nap összes távirata.

A **_tavirathu13.txt_** szövegállomány egy adott hónap 13. napjának időjárás adatait tartalmazza. Egy távirat adatai egy sorban találhatóak egymástól szóközzel elválasztva. Egy sorban 4 adat szerepel a következőképpen.

| település | szöveg (2 karakter) | A település kétbetűs kódja |
| :--- | :--- | :--- |
| idő | szöveg (óópp formátumban) | A mérés időpontja |
| szélirány és -erősség | szöveg (5 karakter) szélirány 3 karakter, -erősség 2 karakter | A szél iránya fokban vagy szöveggel és sebessége csomóban megadva |
| hőmérséklet | egész szám (2 karakter) | Mért hőmérséklet (nem negatív) |

A sorok száma legfeljebb 500. Az adatok idő szerint rendezettek.
Például:
```
BP	0300	32007	21
PA	0315	35010	19
PR	0315	32009	19
SM	0315	01015	20
DC	0315	VRB01	21
SN	0315	00000	21
```
A példában látható, hogy 03:15-kor PR településen 320 fokos irányból 9 csomós szél fújt. A hőmérséklet 19 °C volt. Ugyanekkor DC településen változó (VRB) szélirány volt 1 csomós szélsebességgel, a hőmérséklet 21 °C volt.

Készítsen programot, amely a **_tavirathu13.txt_** állomány adatait felhasználva az alábbi kérdésekre válaszol! A program forráskódját mentse **_metjelentes_** néven! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: `3. feladat`)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Az ékezetmentes kiírás is elfogadott.

Az eredmény megjelenítését és a felhasználóval való kommunikációt a feladatot követő minta alapján valósítsa meg!

1. Olvassa be és tárolja el a **_tavirathu13.txt_** állomány adatait!

2. Kérje be a felhasználótól egy város kódját! Adja meg, hogy az adott városból mikorérkezett az utolsó mérési adat! A kiírásban az időpontot óó:pp formátumban jelenítse meg!

3. Határozza meg, hogy a nap során mikor mérték a legalacsonyabb és a legmagasabb hőmérsékletet! Jelenítse meg a méréshez kapcsolódó település nevét, az időpontot és a hőmérsékletet! Amennyiben több legnagyobb vagy legkisebb érték van, akkor elég az egyiket kiírnia.

4. Határozza meg, azokat a településeket és időpontokat, ahol és amikor a mérések idején szélcsend volt! (A szélcsendet a táviratban 00000 kóddal jelölik.) Ha nem volt ilyen, akkor a „`Nem volt szélcsend a mérések idején.`” szöveget írja ki! A kiírásnál a település kódját és az időpontot jelenítse meg.

5. Határozza meg a települések napi középhőmérsékleti adatát és a hőmérséklet-ingadozását! A kiírásnál a település kódja szerepeljen a sor elején a minta szerint! A kiírásnál csak a megoldott feladatrészre vonatkozó szöveget és értékeket írja ki!
>**a.)** A középhőmérséklet azon hőmérsékleti adatok átlaga, amikor a méréshez tartozó óra értéke 1., 7., 13., 19. Ha egy településen a felsorolt órák valamelyikén nem volt mérés, akkor a kiírásnál az „**NA**” szót jelenítse meg! Az adott órákhoz tartozó összes adat átlagaként határozza meg a középhőmérsékletet, azaz minden értéket azonos súllyal vegyen figyelembe! A középhőmérsékletet egészre kerekítve jelenítse meg!
>**b.)** A hőmérséklet-ingadozás számításhoz az adott településen a napi legmagasabb és legalacsonyabb hőmérséklet különbségét kell kiszámítania! (Feltételezheti, hogy minden település esetén volt legalább két mérési adat.)

6. Hozzon létre településenként egy szöveges állományt, amely első sorában a település kódját tartalmazza! A további sorokban a mérési időpontok és a hozzá tartozó szélerősségek jelenjenek meg! A szélerősséget a minta szerint a számértéknek megfelelő számú kettőskereszttel (#) adja meg! A fájlban az időpontokat és a szélerősséget megjelenítő kettőskereszteket szóközzel válassza el egymástól! A fájl neve **_X.txt_** legyen, ahol az **X** helyére a település kódja kerüljön!

## Minta a szöveges kimenetek kialakításához:
```
2. feladat
Adja meg egy település kódját! Település: SM
Az utolsó mérési adat a megadott településről 23:45-kor érkezett.

3. feladat
A legalacsonyabb hőmérséklet: SM 23:45 16 fok.
A legmagasabb hőmérséklet: DC 13:15 35 fok.

4. feladat
BP 01:00
DC 02:15
SN 03:15
BC 04:45
DC 04:45
SN 05:15
SN 05:45
KE 08:45
BC 11:45

5. feladat
BP Középhőmérséklet: 23; Hőmérséklet-ingadozás: 8
DC Középhőmérséklet: 29; Hőmérséklet-ingadozás: 15
SM Középhőmérséklet: 22; Hőmérséklet-ingadozás: 8
PA Középhőmérséklet: 21; Hőmérséklet-ingadozás: 7
SN Középhőmérséklet: 26; Hőmérséklet-ingadozás: 13
PR Középhőmérséklet: 21; Hőmérséklet-ingadozás: 8
BC NA; Hőmérséklet-ingadozás: 14
PP NA; Hőmérséklet-ingadozás: 6
KE NA; Hőmérséklet-ingadozás: 13

6. feladat
A fájlok elkészültek.
```

### A _BC.txt_ fájl tartalma:
```
BC
00:45 ###
01:45 ####
02:45 ######
03:45 ##
04:45
05:45 ####
11:45
17:45 ########
```