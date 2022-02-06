# Emelt Informatika Érettségi - 2010 október - Anagramma

## Feladat
Az anagramma a szójátékok egy fajtája, melyben értelmes szavak vagy mondatok betűinek sorrendjét úgy változtatjuk meg, hogy az eredmény szintén értelmes szó vagy mondat lesz. Sok anagramma esetén az eredeti szó és a végeredmény között humoros vagy egyéb kapcsolat van, ez növeli az anagramma érdekességét, értékét. Például a satu szó anagrammái: utas, tusa, suta.
A **_szotar.txt_** ASCII kódolású állomány legfeljebb 300 különböző szót tartalmaz. A szavak legalább 2, legfeljebb 30 karakter hosszúságúak, és csak az angol ábécé kisbetűit tartalmazzák. Az állományban az egyes szavak külön sorokban szerepelnek, és minden szó csak egyszer fordulhat elő.

### Például:
**_szotar.txt_**
```
eszesen
kereszt
keretes
keretez
nyertesek
hadartam
maradhat
...
```

Készítsen programot, amely az alábbi kérdésekre válaszol! A program forráskódját **_anagram_*** néven mentse! Ügyeljen arra, hogy programjának minden helyes tartalmú bemeneti állomány esetén működnie kell!

Minden részfeladat megoldása előtt írja a képernyőre a feladat sorszámát! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár (például az 1. feladat esetén: „`Adja meg a szöveget:`”)! A képernyőn megjelenített üzenetek esetén az ékezetmentes kiírás is elfogadott.

1. Kérjen be a felhasználótól egy szöveget, majd határozza meg, hogy hány különböző karakter található a szövegben! A darabszámot és a karaktereket írja ki a képernyőre!

2. Olvassa be a **_szotar.txt_** állományból a szavakat, és a következő feladatok megoldása során ezekkel dolgozzon! Amennyiben nem tudja beolvasni az állományból a szavakat, akkor az első 10 szóval dolgozzon!

3. Az állományból beolvasott szavakat alakítsa át úgy, hogy minden szó karaktereit egyenként tegye ábécérendbe! Az így létrehozott szavakat írja ki az **_abc.txt_** állományba az eredeti állománnyal egyező sorrendben!
### Például:

| Eredeti  | Ábécé sorrendben lévő |
|----------|-----------------------|
| tervez   | eertvz                |
| nyugalom | aglmnouy              |

4. Kérjen be a felhasználótól két szót, és döntse el, hogy a két szó anagramma-e! Ha azok voltak, írja ki a képernyőre az „`Anagramma`” szót, ha nem, akkor pedig a „`Nem anagramma`” szöveget!

5. Kérjen be a felhasználótól egy szót! A **_szotar.txt_** állomány szavaiból keresse meg a szó anagrammáit (a szót önmagát is annak tekintve)! Ha van találat, azokat egymás alá írja ki a képernyőre, ha nem volt találat, akkor írja ki a „`Nincs a szótárban anagramma`” szöveget!

6. Határozza meg, hogy a **_szotar.txt_** állományban melyik a leghosszabb szó! Ha több, ugyanannyi karakterből álló leghosszabb szó volt, akkor az ugyanazokat a karaktereket tartalmazó szavakat (amelyek egymás anagrammái) közvetlenül egymás alá írja ki! A feltételnek megfelelő összes szó pontosan egyszer szerepeljen a kiírásban!

7. Rendezze a **_szotar.txt_** állományban lévő szavakat a karakterek száma szerint növekvő sorrendbe! Az egyforma hosszúságú és ugyanazokat a karaktereket tartalmazó szavak (amelyek egymás anagrammái) szóközzel elválasztva ugyanabba a sorba kerüljenek!Az egyforma hosszúságú, de nem ugyanazokat a karaktereket tartalmazó szavak külön sorba kerüljenek! A különböző hosszúságú szavakat egy üres sorral különítse el egymástól! Az így rendezett szavakat írja ki a **_rendezve.txt_** állományba!

### Például:

Eredeti 
```
halat
rakat
ajak
papi
rakta
ajka
takar
kaja
satu
vallat
tarka
pipa
paplan
```

Rendezett
```
ajak ajka kaja
papi pipa
satu suta tusa utas
```
```
halat
rakat rakta takar tarka
```
```
vallat
paplan
```