# Emelt Informatika Érettségi - 2009 október - Útépítés

## Feladat
Az Alsó és Felső várost összekötő út 1 000 m hosszú részének a felújításán dolgoznak. Ennek a szakasznak a forgalmát figyeljük egy nap néhány óráján keresztül. Az említett szakaszon előzési tilalom van érvényben.

A forgalmat a **_forgalom.txt_** állomány tartalmazza. Első sorában a megfigyelési időszakban áthaladó járművek száma (legfeljebb 2000) látható, a továbbiakban pedig soronként egy áthaladó jármű adatai olvashatók időrendben. Egy sorban az első három szám azt az időpontot jelöli (óra, perc, másodperc), amikor a jármű belép a vizsgált útszakaszra. A következő szám jelöli, hogy a jármű az érintett távolságot hány másodperc alatt tenné meg (legfeljebb 300) – a belépéskor mért sebességgel –, ha haladását semmi nem akadályozná. Ezt egy betű követi, amely jelzi, hogy a jármű melyik város irányából érkezett. Ennek megfelelően a betű **A** vagy **F** lehet. Az egyes adatokat pontosan egy szóköz választja el egymástól.

Ha az útszakaszon egyik jármű utoléri a másikat, akkor az előzési tilalom miatt úgy tekintjük, hogy változatlan sorrendben, ugyanabban az időpillanatban hagyják el a szakasz, mint ahogy a lassabb jármű tenné.
### Például:
**_forgalom.txt_**
```
1105
7 21 1 60 F
7 21 58 69 F
7 22 4 117 F
7 22 39 155 A
7 23 11 99 A
...
```

A 3. sor megmutatja, hogy a 7 óra 21 perc 58 másodperckor a Felső város felől érkező jármű 69 másodperc alatt tenné meg ezt az 1 km hosszú távolságot. Ez a jármű – ha más járművek nem akadályozzák – 7 óra 23 perc 7 másodperckor lép ki az útszakaszról, tehát akkor már nem tartózkodik ott.

Készítsen programot, amely az alábbi kérdésekre válaszol! A program forráskódját **_ut_** néven mentse! Ügyeljen arra, hogy programjának más bemeneti állomány esetén is működnie kell!

Minden részfeladat megoldása előtt írja a képernyőre annak sorszámát! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár (például a 2. feladat esetén: „`2. feladat Adja meg a jármű sorszámát!`”)!

1. Olvassa be a **_forgalom.txt_** állományban talált adatokat, s azok felhasználásával oldja meg a következő feladatokat! Ha az állományt nem tudja beolvasni, akkor az első 10 sorának adatait jegyezze be a programba és dolgozzon azzal!

2. Írja ki a képernyőre, hogy az n-edikként belépő jármű melyik város felé haladt! Ehhez kérje be a felhasználótól az n értékét!

3. Írja a képernyőre, hogy a Felső város irányába tartó utolsó két jármű hány másodperc különbséggel érte el az útszakasz kezdetét!

4. Határozza meg óránként és irányonként, hogy hány jármű érte el a szakaszt! Soronként egy-egy óra adatait írja a képernyőre! Az első érték az órát, a második érték az `Alsó`, a harmadik a `Felső` város felől érkező járművek számát jelentse! A kiírásban csak azokat az órákat jelenítse meg, amelyekben volt forgalom valamely irányban!

5. A belépéskor mért értékek alapján határozza meg a 10 leggyorsabb járművet! Írassa ki a képernyőre ezek belépési idejét, a várost (`Alsó`, illetve `Felső`), amely felől érkezett, és m/s egységben kifejezett sebességét egy tizedes pontossággal, sebességük szerinti csökkenő sorrendben! Ha több azonos sebességű járművet talál, bármelyiket megjelenítheti. Soronként egy jármű adatait jelenítse meg, és az egyes adatokat szóközzel tagolja! (A feladat megoldásakor figyeljen arra, hogy a következő feladatban az adatok eredeti sorrendjét még fel kell használni!)

6. Írassa ki az **_also.txt_** állományba azokat az időpontokat, amikor az Alsó város felé tartók elhagyták a kérdéses útszakaszt! Ha egy jármű utolér egy másikat, akkor a kilépésük időpontja a lassabb kilépési ideje legyen! A fájl minden sorába egy-egy időpont kerüljön óra perc másodperc formában! A számokat pontosan egy szóköz válassza el egymástól!
