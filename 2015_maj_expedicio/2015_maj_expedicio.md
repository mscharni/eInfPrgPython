# Emelt Informatika Érettségi - 2015 május - Expedíció

## Online forráskódok
1. [Megoldás váz](https://replit.com/@mscharni/2015majexpediciostarter)
2. [Megoldás](https://replit.com/@mscharni/2015majexpedicio)

## Feladat
Valamikor a távközlés hőskorában egy ritka farkasfaj tudományos megfigyelésére expedíciót szerveztek a sarkkörön túlra. A magukkal vitt rádió csak napi egy adásra volt alkalmas, arra is csak 90 időegységig, időegységenként egy karaktert továbbítva. Az expedíció rádiósának üzeneteit több rádióamatőr is igyekezett lejegyezni. A feladatban a rádióamatőrök által lejegyzett üzeneteket kell feldolgoznia.

A **_veetel.txt_** fájl tartalmazza a rádióamatőrök által feljegyzett üzeneteket. Minden sorpár egy-egy feljegyzést tartalmaz.
- A sorpár első sorában két szám áll, az első a nap sorszáma, a második pedig - az előzőtől egy szóközzel elválasztva – a rádióamatőré.
- A sorpár második sorában a feljegyzéshez tartozó pontosan 90 karakter áll. A vett karakter az angol ábécé kisbetűje, számjegy, / jel vagy szóköz lehet. Ha az adott időegységben nem volt egyértelműen azonosítható a vett jel, akkor # karakter szerepel. Ha a tényleges üzenet befejeződött, az adó a fennmaradó időegységekben $ jelet küld.
- A napok sorszáma 1 és 11, a rádióamatőrök sorszáma 1 és 20 közötti egész szám lehet.
- Ha a megfigyelés során láttak farkasokat, akkor az üzenet két, / jellel elválasztott egész számmal, a látott kifejlett és kölyök egyedek számával kezdődik, amelyet szóköz követ. Más esetben nem szám az első karakter.
### Például:
``` 
2 15
1/0 #gy#domb##l fig###tu# f#i#s ho#a##dalyoz$$...
```

A fenti sorpár első sora mutatja, hogy az üzenet a 2. napon érkezett és a 15-ös rádióamatőr rögzítette. 1 felnőtt és 0 kölyök farkast figyeltek meg. Mivel a második sorban a 45. karakter $ jel, és előtte nem # jel szerepel, ezért az üzenet biztosan 44 karakter hosszú.

Készítsen programot, amely a **_veetel.txt_** állomány adatait felhasználva az alábbi kérdésekre válaszol! A program forráskódját mentse **_radio_** néven! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: `3. feladat:`)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Az ékezetmentes kiírás is elfogadott.

1. Olvassa be és tárolja a **_veetel.txt_** fájl tartalmát!

2. Írja a képernyőre, hogy melyik rádióamatőr rögzítette az állományban szereplő első és melyik az utolsó üzenetet!

3. Adja meg az összes olyan feljegyzés napját és a rádióamatőr sorszámát, amelynek szövegében a „ **_farkas_** ” karaktersorozat szerepel!

4. Készítsen statisztikát, amely megadja, hogy melyik napon hány rádióamatőr készített feljegyzést. Azok a napok 0 értékkel szerepeljenek, amikor nem született feljegyzés! Az eredmény a képernyőn jelenjen meg a napok sorszáma szerint növekvően! A megjelenítést a feladat végén látható minta szerint alakítsa ki!


5. A rögzített üzenetek alapján kísérelje meg helyreállítani az expedíció által küldött üzenetet! Készítse el az **_adaas.txt_** fájlt, amely napok szerinti sorrendben tartalmazza a küldött üzeneteket! Ha egy időpontban senkinél nem volt vétel, akkor azon a ponton a # jel szerepeljen! (Feltételezheti, hogy az azonos üzenethez tartozó feljegyzések között nincs ellentmondás.)
Az alábbi minta az első napról tartalmaz három üzenetet:
```
1 13
#abor# #e#tun###agy#szel#2# #o##h#d#g ##rkasn#o#oka# #a#tunk
e####a#akn##$#$#$##$$$$$$####
1 19
ta###t##ertunk ##gy #zel#####ok hide##f#r##sn#omo#at ##ttu##
e#y patak#al$#$$$$$###$$$$$$$
1 9
ta#o#t#v##tu#k nag# #zel#20 fok#hi##g fa#k#snyo#okat la#tun#
#e#y#pat##na#$$###$$#$#$$$$$$$
```
A helyreállított üzenet:
```
tabort vertunk nagy szel#20 fok hideg farkasnyomokat lattunk
e#y pataknal$$$$$$$$$$$$$$$$$
```

6. Készítsen függvényt **szame** néven az alábbi algoritmus alapján! A függvény egy karaktersorozathoz hozzárendeli az igaz vagy a hamis értéket. A függvény elkészítésekor az algoritmusban megadott változóneveket használja! Az elkészített függvényt a következő feladat megoldásánál felhasználhatja.
```
Függvény szame(szo:karaktersorozat): logikai
		valasz:=igaz
		Ciklus i:=1-től hossz(szo)-ig
			ha szo[i]<'0' vagy szo[i]>'9' akkor valasz:=hamis
		Ciklus vége
		szame:=valasz
Függvény vége
```

7. Olvassa be egy nap és egy rádióamatőr sorszámát, majd írja a képernyőre a megfigyelt  egyedek számát (a kifejlett és kölyök egyedek számának összegét)! Ha nem volt ilyen feljegyzés, a „`Nincs ilyen feljegyzés`” szöveget jelenítse meg! Ha nem volt megfigyelt egyed vagy számuk nem állapítható meg, a „`Nincs információ`” szöveget jelenítse meg!
Amennyiben egy számot közvetlenül # jel követ, akkor a számot tekintse nem megállapíthatónak!

## Minta a szöveges kimenetek kialakításához:
```
2. feladat:
Az első üzenet rögzítője: 13
Az utolsó üzenet rögzítője: 18

3. feladat:
10. nap 16. rádióamatőr
...

4. feladat:
1. nap: 13 rádióamatőr
2. nap: 14 rádióamatőr
...

7. feladat:
Adja meg a nap sorszámát! 2
Adja meg a rádióamatőr sorszámát! 15
A megfigyelt egyedek száma: 1
```

