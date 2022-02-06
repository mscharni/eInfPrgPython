# Emelt Informatika Érettségi - 2006 február - Telefonszámla

## Feladat
Egy új szolgáltatás keretében ki lehet kérni a napi telefonbeszélgetéseink listáját. A listát egy fájlban küldik meg, amelyben a következő adatok szerepelnek: hívás kezdete, hívás vége,
hívott telefonszám. A hívás kezdete és vége óra, perc, másodperc formában szerepel.
### Például:
```
6 15 0 6 19 0 		Óra perc mperc Óra perc mperc
395682211 			Telefonszám
9 58 15 10 3 53 	Óra perc mperc Óra perc mperc
114571155 			Telefonszám
```

A hívások listája időben rendezett módon tartalmazza az adatokat, és szigorúan csak egy napi adatot, azaz nincsenek olyan beszélgetések, amelyeket előző nap kezdtek vagy a következő napon fejeztek be. Továbbá az elmúlt időszak statisztikái alapján tudjuk, hogy a napi hívások száma nem haladja meg a kétszázat.

A telefonálás díjait a következő táblázat foglalja össze.

| Hívásirány     | Csúcsidőben  | Csúcsidőn kívül          |
|----------------|:------------:|:------------------------:|
| Vezetékes      |           30 |                       15 |
| Mobil társaság | 69,175       | 46,675                   |


További fontos információk:
- A csúcsidő reggel **7:00:00**-kor, a csúcsidőn kívüli időszak pedig **18:00:00**-kor kezdődik. A díjazás számításakor az számít, hogy mikor kezdte az illető a beszélgetést.(Például: ha 17:55-kor kezdett egy beszélgetést, de azt 18:10-kor fejezte be, akkor is csúcsidőbeli díjakkal kell számlázni.)
- Minden megkezdett perc egy egész percnek számít.
- Minden telefonszám elején egy kétjegyű körzetszám, illetve mobil hívószám található. A mobil hívószámok: 39, 41, 71 kezdődnek, minden egyéb szám vezetékes hívószámnak felel meg.

A következő feladatokat oldja meg egy program segítségével! A programot mentse **_szamla_** néven!

1. Kérjen be a felhasználótól egy telefonszámot! Állapítsa meg a program segítségével, hogy a telefonszám mobil-e vagy sem! A megállapítást írja ki a képernyőre!

2. Kérjen be továbbá egy hívás kezdeti és hívás vége időpontot óra perc másodperc formában! A két időpont alapján határozza meg, hogy a számlázás szempontjából hány perces a beszélgetés! A kiszámított időtartamot írja ki a képernyőre!

3. Állapítsa meg a **_hivasok.txt_** fájlban lévő hívások időpontja alapján, hogy hány számlázott percet telefonált a felhasználó hívásonként! A kiszámított számlázott perceket írja ki a **_percek.txt_** fájlba a következő formában!
    `perc telefonszám`

4. Állapítsa meg a **_hivasok.txt_** fájl adatai alapján, hogy hány hívás volt csúcsidőben és csúcsidőn kívül! Az eredményt jelenítse meg a képernyőn!

5. A **_hivasok.txt_** fájlban lévő időpontok alapján határozza meg, hogy hány percet beszélt a felhasználó mobil számmal és hány percet vezetékessel! Az eredményt jelenítse meg a képernyőn!

6. Összesítse a **_hivasok.txt_** fájl adatai alapján, mennyit kell fizetnie a felhasználónak a csúcsdíjas hívásokért! Az eredményt a képernyőn jelenítse meg!

