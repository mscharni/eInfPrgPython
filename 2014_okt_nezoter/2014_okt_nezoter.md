# Emelt Informatika Érettségi - 2014 október - Nézőtér

## Online forráskódok
1. [Megoldás váz](https://replit.com/@mscharni/2014oktnezoterstarter)
2. [Megoldás](https://replit.com/@mscharni/2014oktnezoter)

## Feladat
A Fregoli Színházban a jegyeladásokat elektronikusan rögzítik. A színházban 15 sor, és soronként 20 szék van. A sorokat 1-től 15-ig számozzák, a sorokon belül pedig a székeket 1-től 20-ig. Egy előadásra a pillanatnyilag eladott jegyek eloszlását a **_foglaltsag.txt_** szöveges állomány tartalmazza, melyben „**x**” jelzi a foglalt és „**o**” a szabad helyeket.

### Például:
```
ooxxxoxoxoxoxxxooxxx
xxxxxxxxxxxxxxxxxxxx
oxxxxxoooxxxxxxxxxxo
...
```

Az első sor 1-2. széke például még szabad, míg a 2. sorba az összes jegyet eladták. A jegyek ára nem egyforma, összege a helytől függően ötféle lehet. Azt, hogy az adott szék az öt közül melyik árkategóriába tartozik, a **_kategoria.txt_** fájl tartalmazza az alábbi formában:

### Például:
```
33222111111111122233
43322221111112222334
44433322222222333444
...
```

A példa szerint az 1. sor 2. széke a 3. kategóriába, a 2. sor 1. széke a 4. kategóriába esik. Készítsen programot **_nezoter_** néven a következő feladatok megoldására! A program futása során a képernyőre való kiíráskor, illetve az adatok billentyűzetről való beolvasásakor utaljon a feladat sorszámára (például: 3. feladat), és a kiírandó, illetve bekérendő tartalomra! Az ékezetmentes kiírás is elfogadott.

1. Olvassa be és tárolja el a **_foglaltsag.txt_** és a **_kategoria.txt_** fájl adatait!

2. Kérje be a felhasználótól egy sor, és azon belül egy szék számát, majd írassa ki a képernyőre, hogy az adott hely még szabad-e vagy már foglalt!

3. Határozza meg, hogy hány jegyet adtak el eddig, és ez a nézőtér befogadóképességének hány százaléka! A százalékértéket kerekítse egészre, és az eredményt a következő formában írassa ki a képernyőre:
Például:
`Az előadásra eddig 156 jegyet adtak el, ez a nézőtér 42%-a.`

4. Határozza meg, hogy melyik árkategóriában adták el a legtöbb jegyet! Az eredményt írassa ki a képernyőre az alábbi formában:
Például:
`A legtöbb jegyet a(z) 3. árkategóriában értékesítették.`

5. A jegyek árát kategóriánként a következő táblázat tartalmazza:

| árkategória | 1 | 2 | 3 | 4 | 5 |
| ---: | :---: | :---: | :---: | :---: | :---: |
| ár (Ft) | 5000 | 4000 | 3000 | 2000 | 1500 |

Mennyi lenne a színház bevétele a pillanatnyilag eladott jegyek alapján? Írassa ki az eredményt a képernyőre!

6. Mivel az emberek általában nem egyedül mennek színházba, ha egy üres hely mellett nincs egy másik üres hely is, akkor azt nehezebben lehet értékesíteni. Határozza meg, és írassa ki a képernyőre, hogy hány ilyen „**egyedülálló**” üres hely van a nézőtéren!

7. A színház elektronikus eladási rendszere az érdeklődőknek az üres helyek esetén a hely árkategóriáját jeleníti meg, míg a foglalt helyeket csak egy „**x**” karakterrel jelzi. Készítse el ennek megfelelően a fenti adatokat tartalmazó **_szabad.txt_** fájlt!
Például:
```
33xxx1x1x1x1xxx22xxx
xxxxxxxxxxxxxxxxxxxx
4xxxxx222xxxxxxxxxx
```

