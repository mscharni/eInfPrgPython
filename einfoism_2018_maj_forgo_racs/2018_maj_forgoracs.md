# Emelt Informatika Ismeretek Érettségi - 2018 Május - Forgó rács

## Feladat

A forgó rács egy titkosítási módszer, melyet az I. világháborúban táviratoknál és tábori telefonoknál használtak. Ebben a feladatban egy 8x8-as táblázatot fogunk használni a szöveg titkosítására. A táblázat fölé egy kódlemezt helyezve a lemezen található „ablakokba” egy-egy betűt írunk, felülről lefelé haladva, majd az oszlop végén a következő, jobbra lévő oszlopban
folytatjuk a betűk írását. A kódlemezen 16 ablak található. Ha minden ablakba betű került, akkor a kódlemezt 90°-kal balra elforgatva folytatjuk a betűk írását a megismert szabályok alapján. Ezzel a módszerrel a kódlemezt négyszer elforgatva maximum 4x16, azaz 64 betűből álló üzenet titkosítható.

A következő példában egy 4x4-es táblázatban titkosítjuk egy 4 ablakos kódlemez felhasználásával „AZ INFORMATIKAI.” szöveget. A titkosítást a szöveg átalakításával kezdjük. A szóközöket és írásjeleket eltávolítjuk az eredeti szövegből, majd a táblázat cellaszámának megfelelően (4x4) 16 karakterre egészítjük ki a titkosítandó szöveget jobbról az „X” karakterekkel: „AZINFORMATIKAIXX”. 

A továbbiakban egy 8x8-as „forgó rács” titkosítási eljárással kapcsolatos feladatokat kell megoldania.

A megoldás során vegye figyelembe a következőket:
	- A program készítése során törekedjen az objektum orientált (OOP) megoldásra, amire a feladatsor ajánlásokat is tartalmaz. Amennyiben a programot ilyen módon nem tudja elkészíteni, akkor a feladatokat saját osztály létrehozása nélkül is megoldhatja, de így kevesebb pontot ér a megoldása. Ebben az esetben, ha a feladat jellemző vagy metódus létrehozását kéri, akkor Önnek saját alprogramot (függvényt, eljárást) kell készítenie, amely  **_paramétereken keresztül_** kommunikál a hívó programmal!
	- A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például:_ 5. feladat: _)!
	- Az egyes feladatokban a kiírásokat a minta szerint készítse el!
	- A megoldását úgy készítse el, hogy az azonos szerkezetű, de tetszőleges input adatok mellett is megfelelően működjön!

1. Készítsen programot a következő feladatok megoldására, amelynek a forráskódját **Forgoracs** néven mentse el!

2. Hozzon létre saját osztályt Fracs azonosítóval és definiáljon benne két karakter típusú mátrixot (kétdimenziós tömböt) **Kodlemez** és **Titkositott** azonosítóval, illetve egy karakterlánc típusú, csak olvasható jellemzőt **Titkositando** azonosítóval melyekben az adatokat tudja a feladat megoldása során tárolni! A mátrixok sorai és oszlopai 0-tól 7-ig legyenek indexelve!

3. Készítse el az osztály kétparaméteres konstruktorát, ami a következő feladatokat hajtja végre:
       a. Inicializálja a Kodlemez és Titkositott mátrixokat 8×8-as mérettel!
       b. Feltölti a Kodlemez mátrixot a „#” és „A” karakterekkel egy szöveges állományból. A feldolgozandó szövegesfájl nevét a konstruktor paramétereként adjuk át! A feladat megoldásához használandó kodlemez.txt állomány 8 sora, soronként 8 karakterrel tárolja a kódlemez felépítését. A kódlemez „ablakait” az „A” karakterekkel jelöltük. Ahol nincs ablak, ott a „#” karakter szerepel a fájlban.
       c. A Titkositando azonosítójú karakterlánc típusú változó értékét meghatározza a konstruktor másik paraméterében megadott paraméterrel!
       d. A Titkositando változó értékét átalakítja az Atalakit() metódus (függvény) hívásával, mely működését a következő (4.) feladatban írtuk le!

4. Hozzon létre az Fracs osztályban **Atalakit()** azonosítóval metódust, ami a következő feladatokat hajtja végre:
       a. A Titkositando változóból törli a szóközöket, pontokat és vesszőket!
       b. Kivételt dob „ _Túl hosszú a titkosítandó szöveg!_ ” üzenettel, ha a törlések után a szöveg hossza nagyobb, mint 64 karakter!
       c. A Titkositando változó étékét jobbról „X” karakterekkel tölti fel úgy, hogy a titkosítandó szöveg hossza pontosan 64 karakter legyen!

5. Töltse be és tárolja egy szöveges változóban a titkosítandó szöveget a **szoveg.txt** állományból, majd írja ki a képernyőre a minta szerint!

6. Hozzon létre egy Fracs típusú osztálypéldányt (objektumot), melynek a konstruktora a **kodlemez.txt** forrásállomány nevét és a titkosítandó szöveget kapja aktuális paraméterként feldolgozásra!

7. Készítsen az Fracs osztályba **KiirKodlemez** azonosítóval metódust, ami a minta szerint megjeleníti a Kodlemez mátrixban eltárolt karaktereket!

8. Jelenítse meg a képernyőn az átalakított titkosítandó szöveget a minta szerint!

9. Definiáljon az Fracs osztályban metódust (függvényt) a következő algoritmus kódolásával! (Ha nem az Fracs osztályban kódolja a metódust, akkor a Kodlemez mátrix a függvény paramétere legyen!)
	``` 
	Függvény ForgatKodlemez(): Karakter típusú mátrix
		Változó ujKodlemez: Karakter típusú 8x8-as mátrix
		Ciklus sor:=0-tól 7-ig egyesével
			Ciklus oszlop:=0-tól 7-ig egyesével
				ujKodlemez[7-oszlop, sor] = Kodlemez[sor, oszlop]
			Ciklus vége
		Ciklus vége
		Térj vissza ujKodlemez
	Függvény vége
	```
	
10. Készítsen az Fracs osztályban metódust **Titikosit()** azonosítóval, ami a bevezetőben ismertetett eljárással titkosítja az átalakított Titkositando változó értékét a Titkositott karakter típusú mátrixba a Kodlemez mátrix felhasználásával! A Kodlemez mátrixot minden 16 karakter titkosítása után el kell forgatnia balra 90°-kal a 9. feladatban definiált ForgatKodlemez() metódus hívásával! A titkosított szöveget (mátrixot) jelenítse meg a képernyőn a minta szerint!


## Minta a szöveges kimenetek kialakításához:
	```
	5. feladat
	I WILL BE AT THE OPERA TONIGHT, BUT WILL MEET YOU FOR DINNER LATER, IF YOU LIKE.

	 7. feladat
	A###A###
	A###A###
	##A###AA
	##A#####
	A###A###
	####A###
	A#A#A#A#
	##A#####

	 8. feladat
	IWILLBEATTHEOPERATONIGHTBUTWILLMEETYOUFORDINNERLATERIFYOULIKEXXX

	 10. feladat
	ITIYTREX
	WEGYTDWN
	AELOULPR
	AOBUBTIE
	IRFOHIXX
	ETHTENLM
	LIEFOIER
	TNAOUKLL
	```

**Forrás:**
_Paul Lunde: Titkos kódok, Kossuth Kiadó 2010, 80-81.p_


