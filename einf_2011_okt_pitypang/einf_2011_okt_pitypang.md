# Emelt Informatika Érettségi - 2011 október - Pitypang

## Feladat
A kerekdombi Pitypang wellness hotel nem régen nyitotta meg kapuit. A szállodában összesen 27 szoba van. A szobák egységesen kétágyasak, de minden szobában egy pótágy elhelyezésére is van lehetőség. Árképzés szempontjából három különböző időszakot határolt el a szálloda vezetősége: tavaszi, nyári és őszi szakaszt. Ennek megfelelően az árakat az alábbi táblázat tartalmazza.

|       Tavasz      |       Nyár        |         Ősz       |
| :---------------: | :---------------: | :---------------: |
| 01. 01. – 04. 30. | 05. 01. – 08. 31. | 09. 01. – 12. 31. |
|      9 000 Ft     |      10 000 Ft    |      8 000 Ft     |

A feltüntetett értékek egy szoba árát mutatják egy éjszakára. Ha csak egy fő száll meg, akkor is ki kell fizetni a teljes szobaárat. Egy adott foglalás besorolása az érkezés napjától függ.

A pótágy díja 2 000 Ft éjszakánként. Amennyiben a vendég igényel reggelit, azért a fenti áron felül személyenként és naponként 1 100 Ft-ot kell fizetni.

Ha például a két felnőttből és egy gyermekből álló Tóth család április 30. és május 4. között 4 éjszakát tölt a hotelben és kér reggelit, akkor ők az alábbi összegeket fizetik:
- 4 × 9 000 Ft-ot a szobáért,
- 4 × 2 000 Ft-ot a pótágyért,
- 4 × 3 × 1 100 Ft-ot a reggeliért.

A végső számla így 36 000 Ft + 8 000 Ft + 13 200 Ft = 57 200 Ft lesz.

A szálloda eddigi foglalásait a **_pitypang.txt_** fájl tartalmazza. Az első sor a fájlban tárolt foglalások számát mutatja. A további sorokban szóközzel elválasztva soronként az alábbi adatok találhatók:
- a foglalás sorszáma,
- a szoba száma (1–27),
- az érkezés napjának sorszáma,
- a távozás napjának sorszáma,
- a vendégek száma,
- kérnek-e reggelit (1=igen vagy 0=nem),
- a foglalást végző vendég nevéből képzett azonosítója (maximum 25 karakter).

A napok sorszámozása január 1-jétől (1-es sorszám) kezdődik. Április 30-hoz például a 31 + 28 + 31 + 30 = 120-as sorszám tartozik.

A Tóth család foglalása ebben a szerkezetben a következőképpen néz ki:
`123 21 120 124 3 1 Toth_Balint`
A fájl egy éven belül tartalmaz foglalásokat. Az adatok az érkezés napja szerint növekvő sorrendben vannak rendezve a fájlban.

Tájékoztatásul a **_honapok.txt_** fájl a hónapok neveit, a rá következő sorban az adott hónap napjainak számát, majd az ezt követő sorban pedig a hónap első napjának sorszámát tartalmazza. Az állományt forrásfájlként is felhasználhatja. A fenti táblázatnak megfelelő nyári időszak a 121. napon, míg az őszi a 244. napon kezdődik.

Készítsen programot **_szalloda_** néven, amely az alábbi kérdésekre válaszol! A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például `3. feladat:`)! Ahol a felhasználótól kér be adatot, ott írja a képernyőre, hogy milyen adatot vár!

1. Olvassa be az **_pitypang.txt_** állományban található maximum 1 000 foglalás adatát, s annak felhasználásával oldja meg a következő feladatokat! Ha az állományt nem tudja beolvasni, akkor a benne található adatok közül az 1-5, 326-330 és 695-699 foglalási sorszámú sorok adatait jegyezze be a programba, s úgy oldja meg a feladatokat!

2. Jelenítse meg a képernyőn a leghosszabb szállodai tartózkodást! Csak az időtartamot vegye figyelembe, azaz nem számít, hogy hány vendég lakott az adott szobában! Az esetlegesen azonos hosszúságú tartózkodások közül bármelyiket kiválaszthatja. Az eredményt ebben a formában írja a képernyőre:
>_Név (érkezési_nap_sorszáma) – eltöltött_éjszakák_száma_
például: `Nagy_Bertalan (105) – 16`

3. Számítsa ki, hogy az egyes foglalások után mennyit kell fizetnie az egyes vendégeknek!
A foglalás sorszámát és a kiszámított értékeket kettősponttal elválasztva írja ki a **_bevetel.txt_** fájlba!
Ez – a példában szereplő Tóth család esetén – a következő lenne:
>`123:57200`
(Amennyiben nem tudja a fájlba íratni a kiszámított értékeket, úgy az első tíz foglaláshoz tartozó értéket a képernyőre írassa ki!)
Írja a képernyőre a szálloda teljes évi bevételét!

4. Készítsen statisztikát az egyes hónapokban eltöltött vendégéjszakákról! Egy vendégéjszakának egy fő egy eltöltött éjszakája számít. A példában szereplő Tóth család áprilisban 3, májusban pedig 9 vendégéjszakát töltött a szállodában. Írassa ki a havi vendégéjszakák számát a képernyőre az alábbi formában:
>_hónap_sorszáma: x vendégéj_
például: `8: 1059 vendégéj`

5. Kérje be a felhasználótól egy új foglalás kezdő dátumához tartozó nap sorszámát és az eltöltendő éjszakák számát! Határozza meg, hogy hány szoba szabad a megadott időszak teljes időtartamában! A választ írassa ki a képernyőre!
