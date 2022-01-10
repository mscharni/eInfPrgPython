# Emelt Informatika Érettségi - 2005 október - Vigenère tábla

## Feladat
Már a XVI. században komoly titkosítási módszereket találtak ki az üzenetek elrejtésére. A század egyik legjobb kriptográfusának Blaise de Vigenère-nek a módszerét olvashatja a következőkben. A kódoláshoz egy táblázatot és egy ún. kulcsszót használt.
A tábla adatait a **_vtabla.dat_** fájlban találja a következő formában.
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
BCDEFGHIJKLMNOPQRSTUVWXYZA
CDEFGHIJKLMNOPQRSTUVWXYZAB
DEFGHIJKLMNOPQRSTUVWXYZABC
EFGHIJKLMNOPQRSTUVWXYZABCD
FGHIJKLMNOPQRSTUVWXYZABCDE
```
Készítsen programot **_kodol_** néven a következő feladatok végrehajtására!

1. Kérjen be a felhasználótól egy maximum 255 karakternyi, nem üres szöveget! A továbbiakban ez a nyílt szöveg.

2. Alakítsa át a nyílt szöveget, hogy a későbbi kódolás feltételeinek megfeleljen!
### A kódolás feltételei:
- A magyar ékezetes karakterek helyett ékezetmenteseket kell használni. (Például á helyett a; ő helyett o stb.)
- A nyílt szövegben az átalakítás után csak az angol ábécé betűi szerepelhetnek.
- A nyílt szöveg az átalakítás után legyen csupa nagybetűs.

3. Írja ki a képernyőre az átalakított nyílt szöveget!

4. Kérjen be a felhasználótól egy maximum 5 karakteres, nem üres kulcsszót! A kulcsszó a kódolás feltételeinek megfelelő legyen! (Sem átalakítás, sem ellenőrzés nem kell!) Alakítsa át a kulcsszót csupa nagybetűssé!

5. A kódolás első lépéseként fűzze össze a kulcsszót egymás után annyiszor, hogy az így kapott karaktersorozat (továbbiakban kulcsszöveg) hossza legyen egyenlő a kódolandó szöveg hosszával! Írja ki a képernyőre az így kapott kulcsszöveget!

6. A kódolás második lépéseként a következőket hajtsa végre! Vegye az átalakított nyílt szöveg első karakterét, és keresse meg a **_vtabla.dat_** fájlból beolvasott táblázat első oszlopában! Ezután vegye a kulcsszöveg első karakterét, és keresse meg a táblázat első sorában! Az így kiválasztott sor és oszlop metszéspontjában lévő karakter lesz a kódolt szöveg első karaktere. Ezt ismételje a kódolandó szöveg többi karakterével is!

7. Írja ki a képernyőre és a **_kodolt.dat_** fájlba a kapott kódolt szöveget!

## Példa:

**Nyílt szöveg**: `Ez a próba szöveg, amit kódolunk!`
**Szöveg átalakítása**: `EZAPROBASZOVEGAMITKODOLUNK`
**Kulcsszó**: `auto`
**Kulcsszó nagybetűssé alakítása**: `AUTO`
**Nyílt szöveg és kulcsszöveg együtt**:
```
E Z A P R O B A S Z O V E G A M I T K O D O L U N K
A U T O A U T O A U T O A U T O A U T O A U T O A U
```
**Kódolt szöveg**:
```
E T T D R I U O S T H J E A T A I N D C D I E I N E
```
