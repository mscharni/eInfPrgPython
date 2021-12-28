# Emelt Informatika Érettségi - 2014 május — IPv6
A számítógépes hálózatok üzemeltetésében az IPv4-es címeket lassan leváltja az IPv6-os címzési rendszer, amely az eddigi 32 bit hosszúságú címek helyett 128 bit hosszúságú címeket használ.
Az IPv6-os címeket hexadecimális alakban ábrázoljuk, nyolc darab négyes csoportba osztva. Az egyes számjegyek a tízes számrendszerben is használt számjegyek, valamint az _a_ , _b_ , _c_ , _d_ , _e_ , _f_ betűk lehetnek. Az egyes csoportokat kettősponttal választjuk el. Ezek alapján formailag megfelelő IPv6-os cím a következő:
`2001:0db8:03cd:0000:0000:ef45:0006:0123`

Egy nagyvállalatnál készítettek egy programot, ami a cég szerverén tárolt összes dokumentumból kigyűjtötte az IPv6-címeket. Az így keletkezett gyűjteményt az _ip.txt_ fájl tárolja. Minden IP-címet csak az első előfordulásakor rögzítettek. Az állomány legalább 20, de legfeljebb 500 adatsort, soronként egy IP-címet tartalmaz a következő példának megfelelően:

```
2001:0db8:03cd:0000:0000:ef45:0006:0123
2001:0e10:0000:aabc:0000:01ac:0000:0001
fdf8:f53b:82e4:0000:0000:0000:0000:0053
fc00:0000:0000:ad65:0124:33ab:0100:6543
...
```
A vállalatnál háromféle IP-cím fordul elő. A feladat megoldásában csak ezekkel a címekkel kell foglalkozni:

- A `2001:0db8` kezdetű címek a _dokumentációs cím_ ek, eszközöknek nincsenek kiosztva.
- A `2001:0e` kezdetű címek az informatikai eszközöknek kiosztott _globális egyedi_ _cím_ ek.
- Az `fc`, valamint az `fd` kezdetű címek az eszközöknek kiosztott _helyi egyedi cím_ ek.
Több szabály vonatkozik a címek rövidebb leírásának lehetőségére:
- Az egyes csoportokban a bevezető nullák elhagyhatók. Például így leírva a fenti cím: `2001:db8:3cd:0:0:ef45:6:123`
- Kettő vagy több csak nullákból álló csoportot le lehet egyszerűsíteni két kettőspont közötti üres csoportra. Ezzel a szabállyal tovább egyszerűsítve az előző címet: `2001:db8:3cd::ef45:6:123`
- Ha egy címben több helyen is vannak csak nullákból álló csoportok, akkor is csak egyszer lehet ez utóbbi módszerrel rövidítést végrehajtani. Ilyen esetben mindig a több nullás csoportot kell rövidíteni. Ha azonos számú nullás csoport található a címen belül több helyen is, akkor balról az elsőt kell rövidíteni.
Például: `2001:0000:0000:00f5:0000:0000:0000:0123`
Rövidítve: `2001:0:0:f5::123`
Készítsen programot, amely az _ip.txt_ állomány adatait felhasználva az alábbi kérdésekre válaszol! A program forráskódját mentse _cimek_ néven! (A program megírásakor a megadott adatok helyességét, érvényességét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: 3. feladat:)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Az ékezetmentes kiírás is elfogadott. A képernyőre írást igénylő feladatok eredményét a feladatok utáni mintának megfelelően jelenítse meg!

1. Olvassa be az _ip.txt_ állományban talált adatokat, s annak felhasználásával oldja meg a következő feladatokat!
2. Határozza meg és írja a képernyőre, hogy hány adatsor van az állományban!
3. Írja a képernyőre az állományban található legalacsonyabb IP-címet! A megoldásában felhasználhatja, hogy a betűk ASCII-kódjai a számok ASCII-kódjai után találhatók a kódtáblában.
4. Határozza meg, hogy az állományban hány darab IP-cím van az egyes fajtákból! Az eredményt jelenítse meg a képernyőn a mintának megfelelően!
5. Gyűjtse ki a _sok.txt_ állományba azokat az IP-címeket, melyek legalább 18 nullát tartalmaznak! A fájlban minden sor elején szerepeljen az eredeti állományból a cím sorszáma! Ezt kövesse egy szóközzel elválasztva a cím az _ip.txt_ állományban szereplő alakjával!
6. Kérjen be a felhasználótól egy sorszámot! Az állományban a megadott sorszámon található IP-címet rövidítse a csoportokon belüli bevezető nullák elhagyásával! Az állományban található alakot és a rövidített változatot írja a képernyőre egymás alá!
7. Az előző feladatban használt IP-címet rövidítse tovább az egymást követő nullás csoportok rövidítésére vonatkozó szabályoknak megfelelően! Az eredményt jelenítse meg a képernyőn! Amennyiben nem rövidíthető, írja ki: „Nem rövidíthető tovább.”!
## Minta a szöveges kimenetek kialakításához:
```
2. feladat:
Az állományban 372 darab adatsor van.
3. feladat:
A legalacsonyabb tárolt IP-cím:
2001:0db8:0000:00b9:0800:0f00:e02a:71ac
4. feladat:
Dokumentációs cím: 106 darab
Globális egyedi cím: 120 darab
Helyi egyedi cím: 146 darab
6. feladat:
Kérek egy sorszámot: 10
fcef:b0e7:7d20:0000:0000:0000:3b95:0565
fcef:b0e7:7d20:0:0:0:3b95:565
7. feladat:
fcef:b0e7:7d20::3b95:565
```
