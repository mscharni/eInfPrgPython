# Emelt Informatika Ismeretek Érettségi - 2017 Május - Txt2Srt

## Feladat
A videókhoz a legtöbb lejátszóprogram meg tud jeleníteni feliratokat. 
A feliratokat egy külön srt kiterjesztésű feliratfájlban szokták megadni, amely tartalmazza a feliratok sorszámát, az időzítéseket és a feliratokat. 
Ebben a feladatban egy videóhoz SRT formátumú, angol nyelvű feliratfájlt kell készítenie. 
A feliratok és azok időzítése rendelkezésre állnak a **feliratok.txt** állományban, de a formátumuk nem megfelelő.
A megoldás során vegye figyelembe a következőket!
- A program készítése során törekedjen az objektumorientált (OOP) megoldásra,amire a feladatsor ajánlásokat is tartalmaz. 
Amennyiben a programot ilyen módon nem tudja elkészíteni, akkor a feladatokat saját osztály létrehozása nélkül is megoldhatja, de így kevesebb pontot ér a megoldása. 
Ebben az esetben, ha a feladat jellemző vagy metódus létrehozását kéri, akkor Önnek saját alprogramot (függvényt, eljárást) kell készítenie, amely **paramétereken keresztül** kommunikál a hívó programmal.
- A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: **5. feladat:**)!
- Az egyes feladatokban a kiírásokat és az állományba mentést a minta szerint készítse el!
- Az ékezetmentes kiírás is elfogadott.
- Megoldását úgy készítse el, hogy az azonos szerkezetű, de tetszőleges bemenőadatok mellett is megfelelően működjön!

1. Készítsen programot a következő feladatok megoldására, amelynek a forráskódját **txt2srt** néven mentse el!

2. Hozzon létre saját osztályt IdozitettFelirat azonosítóval és definiáljon benne két szöveg típusú adattagot, melyben egy felirat időzítését és magát a feliratot tudja majd tárolni!
Példa az időzítés és a felirat fogalmakra:
	```
	Időzítés: „00:01 - 00:03”
	Felirat: „So phase two - tank creation.”
	```
	A példában a felirat a videó lejátszásakor az első másodpercnél jelenik meg (00:01), a harmadik másodpercben tűnik el (00:03), és a megjelenített felirat szövege a _„So phase two - tank creation.”_

3. Készítse el az osztály konstruktorát, ami a következő feladatokat hajtja végre!
	a. Beállítja az időzítést tároló adattag értékét a konstruktor paraméterében megadott értékkel.
	b. Beállítja a felirat szövegét tároló adattag értékét a konstruktor paraméterében megadott értékkel.

4. Olvassa be a feliratok.txt állomány sorait és hozzon létre osztálypéldányt (objektumot) minden egyes időzítés−felirat párhoz! 
Az osztálypéldányokat egy összetett változóban (pl. vektor, lista stb.) tárolja!
A **feliratok.txt** állományban 2-2 soronként ismétlődve egy felirat időzítése és az ehhez tartozó felirat található.
Például:
	```
	00:01 - 00:03
	So phase two - tank creation.
	00:05 - 00:07
	So what we're going to do in this one
	...
	```

5. Határozza meg és írja ki a képernyőre a minta szerint, hogy hány felirat van a **feliratok.txt** állományban!

6. Készítsen az **IdozitettFelirat** osztályban jellemzőt vagy metódust **SzavakSzama** azonosítóval! 
A létrehozott jellemző vagy metódus segítségével határozza meg az időzített felirat szavainak a számát!
(Szónak tekintünk minden olyan karaktert vagy karaktersorozatot, amelyet egy-egy szóköz karakter választ el egymástól.) 
Feltételezheti, hogy kettő vagy több szóköz karaktert egymás mellett nem tartalmaz a felirat, és a felirat elején és a végén sincsen szóköz.

7. Határozza meg és írja ki a legtöbb szóból álló feliratot! Feltételezheti, hogy a feliratfájlban csak egy ilyen felirat van. 
Az eredményt a minta szerint jelenítse meg a képernyőn!

8. Készítsen az **IdozitettFelirat** osztályban jellemzőt vagy metódust **SrtIdozites** azonosítóval! 
A létrehozott jellemző vagy metódus az időzítéshez tartozó adattag értékét alakítsa át az SRT formátumnak megfelelően! 
A SRT formátumot a következő minta és a leírás alapján készítse el!
	```
	Időzítés: „00:01 - 00:03”
	SRT időzítés: „00:00:01 --> 00:00:03”
	Időzítés: „65:31 - 65:34”
	SRT időzítés: „01:05:31 --> 01:05:34”
	```
	Feltételezheti, hogy a feliratok.txt állományban az időértékek **perc:másodperc** formában vannak megadva, ahol a perc <=99, másodperc < 60 feltételek teljesülnek, és ezek az értékek két karakter hosszúságon vannak megadva.
	Ügyeljen rá, hogy az SRT időzítésnél az időértékeket **óra:perc:másodperc** formában kell megadni, minden időadatot két karakter hosszúságon, ahol az óra < 2, perc < 60, másodperc < 60 feltételek teljesülnek. 
	Az SRT időzítésnél a megjelenési és eltűnési időérték között a „**-**” helyett a „**-->**” jelet kell alkalmazni!


9. Készítse el a felirat.srt állományt a minta szerint! 
Az állományba kerüljön bele a felirat száma (a számozás 1-től kezdődik), az SRT időzítése és a felirat szövege! 
A feliratokat egy-egy üres sor válassza el egymástól!

## Minta a feladathoz:
	```
	5. feladat - Feliratok száma: 1514
	7. feladta - Legtöbb szóból álló felirat:
	What I want you to just notice, and we'll do this a bit a time,
	```

## Minta a _felirat.srt_ állományhoz:
	```
	1
	00:00:01 --> 00:00:03
	So phase two - tank creation.

	2
	00:00:05 --> 00:00:07
	So what we're going to do in this one

	3
	00:00:07 --> 00:00:09
	is we're going to put in our tank model

	4
	00:00:09 --> 00:00:11
	and then that tank needs a number of different
	```

**_Forrás:_**
_https://unity3d.com/learn/tutorials/projects/tanks-tutorial (utolsó megtekintés: 2016.09.24)_