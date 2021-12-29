# Emelt Informatika Érettségi - 2015 október - Fej vagy írás

## Online forráskódok
1. [Megoldás váz](https://replit.com/@mscharni/2015oktfejvagyirasstarter)
2. [Megoldás](https://replit.com/@mscharni/2015oktfejvagyiras)

## Feladat
Ha egy szabályos pénzérmét feldobunk, ugyanannyi a valószínűsége annak, hogy leesés után az érme értéke lesz felül (írás, I), mint annak, hogy a címert tartalmazó másik oldala (fej, F). Ezért gyakran „pénzfeldobással” sorsolnak, például így döntik el, hogy melyik csapat kezdhet el egy futballmeccset.

Feladata a pénzfeldobás szimulálása, illetve pénzfeldobással kapott sorozatok elemzése lesz. A feladatok során az írást az I, a fejet az F nagybetű jelzi. Például egy 5 feldobásból álló sorozat esetén:
```
I
I
F
I
F
```

Készítsen programot **_fejvagyiras_** néven a következő feladatok megoldására! A program futása során a képernyőre való kiíráskor, illetve az adatok billentyűzetről való beolvasásakor utaljon a feladat sorszámára és a kiírandó, illetve bekérendő adatra! Az ékezetmentes kiírás is elfogadott.

1. Szimuláljon egy pénzfeldobást, ahol azonos esélye van a fejnek és az írásnak is! Az eredményt írassa ki a képernyőre a mintának megfelelően!

2. Kérjen be a felhasználótól egy tippet, majd szimuláljon egy pénzfeldobást! Írassa ki a képernyőre a felhasználó tippjét és a dobás eredményét is, majd tájékoztassa a felhasználót az eredményről következő formában: „`Ön eltalálta.`” vagy „`Ön nem találta el.`”!

A **_kiserlet.txt_** állományban egy pénzfeldobás-sorozat eredményét találja. Mivel a sorozat hossza tetszőleges lehet, ezért az **összes adat memóriában történő egyidejű eltárolása nélkül** oldja meg a következő feladatokat! Feltételezheti, hogy egymilliónál több adata nem lesz.

3. Állapítsa meg, hány dobásból állt a kísérlet, és a választ a mintának megfelelően írassa ki a képernyőre!

4. Milyen relatív gyakorisággal dobtunk a kísérlet során fejet? (A fej relatív gyakorisága a fejet eredményező dobások és az összes dobás hányadosa.) A relatív gyakoriságot a mintának megfelelően két tizedesjegy pontossággal, százalék formátumban írassa ki a képernyőre!

5. Hányszor fordult elő ebben a kísérletben, hogy egymás után pontosan két fejet dobtunk? A választ a mintának megfelelően írassa ki a képernyőre! (Feltételezheti, hogy a kísérlet legalább 3 dobásból állt.)
Például az `IFFFFIIFFIFFFIFF` sorozatban kétszer fordult elő, hogy egymás után pontosan két fejet dobtunk.

6. Milyen hosszú volt a leghosszabb, csak fejekből álló részsorozat? Írassa ki a választ a képernyőre a mintának megfelelően, és adja meg egy ilyen részsorozat első tagjának helyét is! (A minta tagjainak számozását eggyel kezdjük.)

Sokan azt hiszik, hogy ha már elég sok fejet dobtunk, akkor a következő dobás nagyobb valószínűséggel lesz írás, mint fej. Ennek ellenőrzésére vonatkozik a következő feladat.

7. Állítson elő és tároljon a memóriában 1000 db négy dobásból álló sorozatot! Számolja meg, hogy hány esetben követett egy háromtagú „tisztafej” sorozatot fej, illetve hány esetben írás! Az eredményt írassa ki a **dobasok.txt** állományba úgy, hogy az első sorba kerüljön az eredmény, a második sorban pedig egy-egy szóközzel elválasztva, egyetlen sorban szerepeljenek a dobássorozatok!
### Például:
```
FFFF: 12, FFFI: 14
FIFI IIIF IFIF IIII FFII FFFF IIFI FFII FFFI ...
```

## Minta a szöveges kimenetek kialakításához:
```
1. feladat
A pénzfeldobás eredménye: I

2. feladat
Tippeljen (F/I) = I
A tipp I, a dobás eredménye I volt.
Ön eltalálta!

3. feladat
A kísérlet 4321 dobásból állt

4. feladat
A kísérlet során a fej relatív gyakorisága 51.03% volt.

5. feladat
A kísérlet során 259 alkalommal dobtak pontosan két fejet egymás után.

6. feladat
A leghosszabb tisztafej sorozat 11 tagból áá, kezdete a(z) 947. dobás.
```
