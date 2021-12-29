# Emelt Informatika Érettségi - 2017 október - Hiányzások

## Online forráskódok
1. [Megoldás váz](https://replit.com/@mscharni/2017okthianyzasokstarter)
2. [Megoldás](https://replit.com/@mscharni/2017okthianyzasok)

## Feladat
Egy osztály második félévi hiányzásai állnak rendelkezésére a **_naplo.txt_** fájlban. A hiányzások naponként csoportosítva szerepelnek, minden napot a **#** karakter kezd, majd egy-egy szóközzel elválasztva a hónap és a nap sorszáma következik. Az aznapi hiányzások tanulónként külön sorokban vannak, a tanuló napi hiányzásait egy hét karakterből álló karaktersorozat írja le. A karaktersorozat minden karaktere egy-egy órát ad meg. Értéke az **O** betű, ha a tanuló jelen volt az adott órán, az **X** utal az igazolt, az **I** az igazolatlan távollétre, végül **N** betű jelzi, ha a tanulónak akkor nem volt órája. Például:
```
	# 01 15
	Galagonya Alfonz OXXXXXN
	# 01 16
	Alma Hedvig OOOOOIO
	Galagonya Alfonz XXXXXXX
```

A fenti példa a január 15-16-i hiányzásokat tartalmazza. Galagonya Alfonznak január 15-én hat órája lett volna, de csak az első órán volt jelen, utána igazoltan hiányzott. Alma Hedvignek január 16-án hét órája lett volna, de a 6. óráról igazolatlanul távol maradt.

Az állomány legfeljebb 600 sort tartalmaz, az osztályba pedig legfeljebb 50 tanuló jár. Feltételezheti, hogy az osztályban nincs két azonos nevű tanuló, továbbá hogy minden tanulónak egy vezeték és egy utóneve van. Felhasználhatja, hogy a jelenlétre vonatkozó bejegyzés mindig 7 karakterből áll.

Készítsen programot, amely az állomány adatait felhasználva az alábbi kérdésekre válaszol! A program forráskódját **_hianyzasok_** néven mentse! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, és feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: `3. feladat:`)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Az eredmények kiírásánál utaljon a kiírt adat jelentésére! A mintától eltérő, valamint az ékezetmentes kiírás is elfogadott.

1. Olvassa be és tárolja el a **_naplo.txt_** fájl tartalmát!

2. Határozza meg és írassa ki, hogy hány sor van a fájlban, ami hiányzást rögzít! (A fenti példában 3 ilyen bejegyzés van.)

3. Számolja meg és írassa ki, hogy összesen hány óra igazolt és hány óra igazolatlan hiányzás volt a félév során!

Néhány tanár azt feltételezi, hogy a tanulók bizonyos órákról gyakrabban hiányoznak.
A következő három feladatban ennek vizsgálatát kell előkészítenie.

4. Készítsen függvényt **hetnapja** néven, amely a paraméterként megadott dátumhoz (hónap, nap) megadja, hogy az a hét melyik napjára esik (hétfő, kedd...). Tudjuk, hogy az adott év nem volt szökőév, továbbá azt is, hogy január elseje hétfőre esett. Használhatja az alábbi   algoritmust is, ahol a tömbök indexelése 0-val kezdődik, de ettől eltérő megoldású függvényt is készíthet.
```
	Függvény hetnapja(honap:egesz, nap:egesz): szöveg
		napnev[]:= ("vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat")
		napszam[]:= (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
		napsorszam:= (napszam[honap-1]+nap) MOD 7
		hetnapja:= napnev[napsorszam]
	Függvény vége
```

5. Kérjen be egy dátumot (hónap, nap), és a **hetnapja** függvény felhasználásával írassa ki, hogy az a hét melyik napjára esett!

6. Kérje be a hét egy tanítási napjának nevét és egy aznapi tanítási óra óraszámát (például: kedd 3)! Írassa ki a képernyőre, hogy a félév során az adott tanítási órára összesen hány hiányzás jutott!

7. Írassa ki a képernyőre a legtöbb órát hiányzó tanuló nevét! Ha több ilyen tanuló is van, akkor valamennyi neve jelenjen meg szóközzel elválasztva!

## Minta a szöveges kimenetek kialakításához:
```
2. feladat
A naplóban 139 bejegyzés van.

3. feladat
Az igazolt hiányzások száma 788, az igazolatlanoké 18 óra.

5. feladat
A hónap sorszáma=2
A nap sorszáma=3
Azon a napon szombat volt.

6. feladat
A nap neve=szerda
Az óra sorszáma=3
Ekkor összesen 49 óra hiányzás történt.

7. feladat
A legtöbbet hiányzó tanulók: Kivi Adrienn Jujuba Ibolya
```