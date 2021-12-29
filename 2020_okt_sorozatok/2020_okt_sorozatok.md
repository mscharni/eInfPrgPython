# Emelt Informatika Érettségi - 2020 október - Sorozatok

## Online forráskódok
1. [Megoldás váz](https://replit.com/@mscharni/2020oktsorozatokstarter)
2. [Megoldás](https://replit.com/@mscharni/2020oktsorozatok)

## Feladat
Sok olyan sorozatrajongó van, aki folyamatosan követi a kedvelt sorozatait. Egy, az angol nyelvű sorozatokért rajongó személy feljegyzést készített egy nyolc hónapos időszak kedvenc sorozatairól.

A **_lista.txt_** fájl a rajongó által kedvelt sorozatok adásba kerülésének dátumát, a sorozat angol címét, az évadot és az epizód számát, az epizód hosszát percben és egy jelzést tartalmaz, hogy a lista készítője megnézte-e már azt az epizódot. Ezek az adatok egymás után külön sorokban szerepelnek. A fájlban biztosan 400-nál kevesebb epizódról van adat, epizódonként 5 sorban.

### Például:
```
...
2018.01.19
Puzzles
3x10
43
0
NI
Puzzles
3x11
43
0
...
```

A példában látható, hogy a Puzzles című sorozat 3. évadának 10. epizódja 2018. 01. 19-én került adásba. Az epizód 43 perces, és még nem nézte meg a lista készítője.
- A dátumokat mindig „éééé.hh.nn” formátumban rögzítették. Vannak olyan sorozatrészek, amelyeknek a lista rögzítésekor még nem tudták az adásba kerülésük idejét. Ezeknél a dátum helyett mindig az „ **_NI_** ” rövidítés szerepel.
- Az évad jelzése vezető nullák nélkül történik, az epizód számát pedig mindig két számjeggyel rögzítették. Az évad és az epizód számát egy „ **_x_** ” választja el egymástól.
- Az egyes sorozatok epizódjai mindig ugyanolyan hosszúak.
- Az epizóddal kapcsolatos utolsó adat értéke „ **_0_** ” vagy „ **_1_** ”. Az 1-es számjegy jelöli, hogy az adott részt már megtekintette a lista készítője, a 0 pedig azt, hogy még nem látta.

Készítsen programot a **_lista.txt_** állomány adatainak feldolgozására! A program forráskódját mentse **_sorozatok_** néven! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például `2. feladat:`)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Az ékezetmentes kiírás is elfogadott.

1. Olvassa be és tárolja el a **_lista.txt_** fájl tartalmát!

2. Írassa ki a képernyőre, hogy hány olyan epizód adatait tartalmazza a fájl, amelynek ismert az adásba kerülési dátuma!

3. Határozza meg, hogy a fájlban lévő epizódok hány százalékát látta már a listát rögzítő személy! A százalékértéket a minta szerint, két tizedesjeggyel jelenítse meg a képernyőn!

4. Számítsa ki, hogy összesen mennyi időt töltött a személy az epizódok megnézésével! Az eredményt a minta szerint nap, óra, perc formában adja meg!

5. Kérjen be a felhasználótól egy dátumot „éééé.hh.nn” formában! Határozza meg, hogy az adott dátumig megjelent epizódokból melyeket nem látta még! Az aznapi epizódokat is számolja bele! A feltételnek megfelelő epizódok esetén írja a képernyőre tabulátorral elválasztva az évad- és az epizódszámot, valamint a sorozat címét a minta szerint!

6. Készítse el az alábbi algoritmus alapján a hét napját meghatározó függvényt! A függvény neve **_Hetnapja_** legyen! A függvény az év, hónap és nap megadása után szöveges    eredményként visszaadja, hogy az adott nap a hét melyik napja volt. (Az a és b egész     számok maradékos osztása esetén az a div b kifejezés adja meg a hányadost, az a mod b pedig a maradékot, például 17 div 7 = 2 és 17 mod 7 = 3.)
```
Függvény hetnapja(ev, ho, nap : Egész) : Szöveg
	napok: Tömb(0..6: Szöveg)= ("v", "h", "k", "sze",  "cs", "p", "szo")
	honapok: Tömb(0..11: Egész)= (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
	Ha ho < 3 akkor ev := ev - 1
	hetnapja := napok[(ev + ev div 4 – ev div 100 + ev div 400 + honapok[ho-1] + nap) mod 7]
Függvény vége
```

7. Kérjen be a felhasználótól egy napot az előző feladatban látható rövidített alakban! A napokat egy (h, k, p, v), kettő (cs), vagy három (sze, szo) karakterrel adja meg! Határozza meg, hogy a fájlban lévő sorozatok közül melyike(ke)t vetítik az adott napon! A sorozatok nevét a minta szerint jelenítse meg a képernyőn! Ha az adott napon egy sorozatot sem adtak adásba, akkor „`Az adott napon nem kerül adásba sorozat.`” üzenetet jelenítse meg!

8. Határozza meg sorozatonként az epizódok összesített vetítési idejét és az epizódok számát! A számításnál vegye figyelembe a vetítési dátummal nem rendelkező epizódokat is! A megoldás során felhasználhatja, hogy egy sorozat epizódjainak adatai egymást követik a forrásállományban. A listát írja ki a **_summa.txt_** fájlba! A fájl egy sorában a sorozat címe, az adott sorozatra vonatkozó összesített vetítési idő percben és az epizódok száma szerepeljen szóközzel elválasztva!

### Minta a szöveges kimenetek kialakításához:
```
2. feladat
A listában 202 db vetítési dátummal rendelkező epizód van.

3. feladat
A listában lévő epizódok 45,66%-át látta.

4. feladat
Sorozatnézéssel 2 napot 15 órát és 32 percet töltött.

5. feladat
Adjon meg egy dátumot! Dátum= 2017.10.18
7x01 The Fable
7x02 The Fable
15x04 Military Police
5x03 Spy School
5x04 Spy School
4x04 The Elite Minds

7. feladat
Adja meg a hét egy napját (például cs)! Nap= cs
The Hospital
Spectacular Power
Upper Story
Chicago Flame
Shrinktime
```

### Minta a _summa.txt_ fájl kialakításához:
```
Games 420 7
The Fable 588 14
The IT Guy 450 10
```