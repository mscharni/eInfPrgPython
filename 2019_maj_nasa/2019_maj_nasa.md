# Emelt Informatika Érettségi - 2019 Május - NASA

## Feladat

A web szerverek fájlokban naplózzák az ügyfelektől érkező kéréseket. Ebben a feladatban a NASA floridai webszerverének 1995.07.20-i naplójában lévő adatokkal kell feladatokat megoldania. A napló csak a JPG típusú képállományokhoz tartozó kéréseket tartalmazza. A megoldás során vegye figyelembe a következőket!
- A program készítése során törekedjen az objektumorientált (OOP) megoldásra, amire a feladatsor ajánlásokat is tartalmaz! Amennyiben a programot ilyen módon nem tudja elkészíteni, akkor a feladatokat saját osztály létrehozása nélkül is megoldhatja, de így kevesebb pontot ér a megoldása. Ebben az esetben, ha a feladat jellemző vagy metódus létrehozását kéri, akkor Önnek saját alprogramot (függvényt, eljárást) kell készítenie, amely **_paramétereken keresztül_** kommunikál a hívó programmal.
- A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: 5. feladat:)!
- Az egyes feladatokban a kiírásokat a minta szerint készítse el!
- Az ékezetmentes kiírás is elfogadott.
- Megoldását úgy készítse el, hogy az azonos szerkezetű, de tetszőleges bemenő adatok mellett is megfelelően működjön!

A NASAlog.txt állomány soronként tartalmazza az egy-egy kéréshez tartozó adatokat. Az adatokat az utolsó két adat kivételével a „*” (csillag) karakter választja el egymástól. Az utolsó két adat között pontosan egy szóköz található. Például:
	```
	rn3.swc.com*20/Jul/1995:12:55:04*GET /images/small.jpg*200 46573
	205.164.88.195*20/Jul/1995:03:07:05*/images/smal.jpg*404 -
	```
A sorokban lévő adatok rendre a következők:
	- Az ügyfél címének domain neve vagy IPv4 formátumú címe, ha nem sikerült a névfeloldás. Például: „rn3.swc.com” vagy „205.164.88.195”
	- A kérés ideje nap/hónap/év:óra:perc:másodperc formában megadva.
	Például: „20/Jul/1995:23:07:05”
	Feltételezheti, hogy a dátum és időértékek mindig azonos karakterszámmal vannak megadva a fenti minta szerint.
	- Az igényelt JPG típusú fájl. Például: „GET /images/small.jpg”
	- A kéréshez tartozó háromjegyű állapotkód. Például: „ 200 ”
	- A kérésre elküldött válasz mérete bájtokban, ha nem küldött a kérésre a szerver adatot, akkor a „-” (kötőjel) karakter található a sor végén. Például: „ 46573 ” vagy „-”

1. Készítsen programot a következő feladatok megoldására, amelynek a forráskódját NASA néven mentse el!

2. Hozzon létre saját osztályt Keres azonosítóval és definiáljon benne öt szöveges típusú adattagot, amelyben az egy kéréshez kapcsolódó adatokat tudja majd eltárolni!

3. Készítse el az osztály konstruktorát, ami a következő feladatokat hajtja végre!
	− Beállítja az ügyfél címét.
	− Beállítja a kérés idejét (dátum és idő).
	− Beállítja a GET paranccsal kezdődő kérést.
	− Beállítja a kéréshez tartozó állapotkódot.
	− Beállítja az elküldött JPG fájl méretét.
Például:
	```
	Cim: „204.239.210.188”
	DatumIdo: „20/Jul/1995:00:00:00”
	Get: „GET /shuttle/countdown/count70.jpg”
	HttpKod: „200”
	Meret: „46573”
	```

4. Olvassa be a NASAlog.txt állomány sorait, és hozzon létre osztálypéldányt (objektumot) minden egyes kéréshez és a példányokat egy összetett adatszerkezetben (pl. vektor, lista stb.) tárolja!

5. Határozza meg és írja ki a képernyőre a minta szerint, hogy hány kérés található a NASAlog.txt állományban!

6. Készítsen 32 bites egész típusú jellemzőt vagy metódust (függvényt) ByteMeret azonosítóval a saját osztályában, amely a szöveges típusban tárolt elküldött válasz méretét szám típusúra alakítja át! Ügyeljen arra, hogy ha a válasznak nem volt mérete, akkor ott „-” szerepel, ami 0 bájtot jelent! Határozza meg és írja ki a képernyőre a minta szerint a kérésekre küldött válaszok összes méretét bájtban!

7. Készítsen logikai típusú jellemzőt vagy metódust (függvényt) Domain azonosítóval a saját osztályában, mely segítségével eldönti az ügyfél címéről, hogy az rendelkezett-e domain névvel! Domain névvel rendelkező címnek tekintheti azokat a címeket, amelyek utolsó karaktere nem számjegy.

8. Határozza meg a NASAlog.txt állomány adatai alapján, hogy a kéréseknél milyen arányban rendelkezett az ügyfél címe domain névvel az összes kérésszámhoz viszonyítva! Az eredményt a minta szerint írja ki a képernyőre!

9. Készítsen statisztikát a NASAlog.txt állomány adatai alapján amely megadja, hogy az egyes állapotkódok hányszor fordultak elő! A statisztika eredményét a minta szerint jelenítse meg a képernyőn! Megoldását úgy készítse el, hogy az egy tetszőlegesen megadott állományban előforduló állapotkódokat is fel tudja dolgozni!

### Minta a szöveges kimenetek kialakításához:
	```
	5. feladat: Kérések száma: 1636

	6. feladat: Válaszok összes mérete: 160342345 byte

	8. feladat: Domain-es késérek: 69.74%

	9. feladat: Statisztika:
	200: 1558 db
	404: 5 db
	304: 73 db
	```
	
**Forrás:**
_http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html (utolsó megtekintés: 2016.09.24)_


