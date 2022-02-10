# Emelt Informatika Érettségi - 2021 május - Bányató

## Feladat

A bányató egy elhagyott külszíni bánya, amely egy idő után megtelik vízzel. Ebben a feladatban egy bányató mélységét kell elemeznie.

A tó felszínét sakktáblaszerűen 1 m oldalhosszúságú négyzetekre bontották, és minden ilyen négyzetben megmérték a tó mélységét. A mérést deciméter pontossággal végezték. A szárazföldet a 0 érték jelzi. A mérési adatokat egy téglalap alakú táblázatban rögzítették, például:

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:--:|
|**1**| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**2**| 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 8 | 10 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**3**| 0 | 0 | 0 | 0 | 0 | 19 | 10 | 0 | 11 | 16 | 18 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**4**| 0 | 0 | 0 | 9 | 17 | 35 | 5 | 11 | 11 | 22 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**5**| 0 | 0 | 0 | 19 | 75 | 64 | 53 | 61 | 25 | 0 | 10 | 4 | 11 | 17 | 17 | 0 | 27 | 61 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**6**| 0 | 2 | 0 | 18 | 75 | 58 | 64 | 25 | 49 | 0 | 0 | 34 | 74 | 73 | 67 | 20 | 55 | 75 | 3 | 15 | 2 | 10 | 0 | 0 | 0 | 
|**7**| 0 | 18 | 25 | 23 | 71 | 32 | 34 | 62 | 24 | 0 | 0 | 43 | 55 | 58 | 51 | 28 | 75 | 58 | 2 | 22 | 35 | 9 | 3 | 10 | 0 | 
|**8**| 0 | 6 | 12 | 35 | 76 | 47 | 51 | 62 | 0 | 0 | 0 | 32 | 65 | 40 | 84 | 51 | 40 | 40 | 47 | 65 | 0 | 0 | 26 | 21 | 0 | 
|**9**| 0 | 6 | 29 | 40 | 76 | 43 | 73 | 88 | 0 | 0 | 0 | 33 | 88 | 76 | 73 | 38 | 56 | 28 | 4 | 86 | 80 | 0 | 15 | 16 | 0 | 
|**10**| 0 | 0 | 14 | 31 | 24 | 42 | 52 | 63 | 42 | 27 | 0 | 50 | 50 | 42 | 67 | 84 | 51 | 53 | 33 | 46 | 0 | 0 | 7 | 3 | 0 | 
|**11**| 0 | 13 | 29 | 27 | 80 | 34 | 38 | 57 | 68 | 72 | 26 | 55 | 22 | 81 | 76 | 60 | 34 | 51 | 4 | 13 | 0 | 0 | 0 | 0 | 0 | 
|**12**| 0 | 12 | 26 | 27 | 65 | 33 | 77 | 49 | 73 | 38 | 89 | 35 | 80 | 36 | 76 | 77 | 88 | 79 | 18 | 13 | 18 | 10 | 0 | 0 | 0 | 
|**13**| 0 | 12 | 25 | 37 | 59 | 65 | 20 | 57 | 33 | 48 | 84 | 75 | 48 | 33 | 34 | 92 | 86 | 97 | 89 | 93 | 82 | 86 | 3 | 11 | 0 | 
|**14**| 0 | 0 | 0 | 35 | 53 | 59 | 38 | 37 | 69 | 36 | 54 | 52 | 55 | 36 | 36 | 96 | 81 | 92 | 95 | 98 | 82 | 90 | 0 | 0 | 0 | 
|**15**| 0 | 0 | 6 | 56 | 62 | 47 | 47 | 60 | 58 | 25 | 20 | 38 | 64 | 47 | 29 | 40 | 44 | 23 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**16**| 0 | 0 | 0 | 36 | 54 | 21 | 62 | 59 | 26 | 34 | 49 | 40 | 63 | 36 | 63 | 38 | 52 | 67 | 60 | 52 | 34 | 27 | 2 | 0 | 0 | 
|**17**| 0 | 0 | 2 | 44 | 46 | 41 | 26 | 42 | 46 | 34 | 29 | 33 | 60 | 16 | 63 | 67 | 18 | 62 | 63 | 51 | 35 | 12 | 18 | 0 | 0 | 
|**18**| 0 | 4 | 12 | 31 | 25 | 24 | 25 | 22 | 57 | 67 | 0 | 44 | 40 | 36 | 45 | 58 | 51 | 29 | 45 | 12 | 46 | 37 | 13 | 0 | 0 | 
|**19**| 0 | 5 | 19 | 10 | 58 | 40 | 42 | 41 | 20 | 41 | 0 | 13 | 19 | 19 | 27 | 24 | 53 | 54 | 27 | 29 | 55 | 0 | 0 | 0 | 0 | 
|**20**| 0 | 4 | 16 | 25 | 35 | 39 | 52 | 74 | 52 | 66 | 0 | 0 | 40 | 53 | 46 | 23 | 36 | 23 | 26 | 22 | 30 | 0 | 0 | 0 | 0 | 
|**21**| 0 | 19 | 10 | 24 | 35 | 68 | 76 | 72 | 44 | 35 | 0 | 0 | 16 | 46 | 21 | 35 | 59 | 56 | 38 | 56 | 27 | 22 | 1 | 0 | 0 | 
|**22**| 0 | 0 | 0 | 16 | 36 | 88 | 58 | 83 | 33 | 27 | 0 | 0 | 0 | 45 | 58 | 25 | 25 | 68 | 25 | 0 | 46 | 52 | 8 | 0 | 0 | 
|**23**| 0 | 0 | 0 | 17 | 38 | 80 | 55 | 67 | 96 | 77 | 0 | 0 | 0 | 0 | 61 | 76 | 52 | 36 | 25 | 0 | 30 | 21 | 9 | 0 | 0 | 
|**24**| 0 | 18 | 15 | 22 | 30 | 73 | 56 | 64 | 54 | 67 | 96 | 84 | 62 | 73 | 68 | 68 | 72 | 66 | 49 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**25**| 0 | 9 | 26 | 32 | 25 | 68 | 66 | 66 | 76 | 62 | 84 | 82 | 67 | 53 | 83 | 90 | 63 | 57 | 48 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**26**| 0 | 0 | 0 | 0 | 35 | 88 | 68 | 73 | 67 | 88 | 98 | 75 | 74 | 70 | 72 | 72 | 75 | 79 | 26 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**27**| 0 | 11 | 0 | 0 | 29 | 74 | 62 | 75 | 71 | 72 | 52 | 75 | 67 | 65 | 88 | 58 | 76 | 59 | 69 | 0 | 0 | 23 | 0 | 0 | 0 | 
|**28**| 0 | 11 | 21 | 39 | 20 | 94 | 96 | 94 | 67 | 80 | 70 | 66 | 61 | 77 | 62 | 74 | 94 | 67 | 24 | 0 | 0 | 36 | 0 | 0 | 0 | 
|**29**| 0 | 12 | 18 | 23 | 22 | 39 | 52 | 77 | 83 | 67 | 97 | 68 | 67 | 56 | 20 | 26 | 6 | 0 | 0 | 0 | 0 | 29 | 0 | 0 | 0 | 
|**30**| 0 | 0 | 18 | 35 | 32 | 45 | 83 | 58 | 80 | 57 | 84 | 86 | 68 | 60 | 49 | 25 | 20 | 5 | 11 | 26 | 14 | 11 | 0 | 0 | 0 | 
|**31**| 0 | 0 | 5 | 36 | 46 | 12 | 97 | 63 | 50 | 92 | 50 | 21 | 29 | 53 | 46 | 31 | 26 | 35 | 2 | 0 | 5 | 0 | 0 | 0 | 0 | 
|**32**| 0 | 0 | 12 | 8 | 59 | 45 | 76 | 83 | 68 | 81 | 29 | 18 | 41 | 64 | 56 | 98 | 45 | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**33**| 0 | 0 | 0 | 15 | 42 | 28 | 82 | 69 | 64 | 85 | 45 | 52 | 45 | 62 | 45 | 31 | 19 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**34**| 0 | 0 | 0 | 8 | 55 | 46 | 61 | 54 | 79 | 69 | 49 | 48 | 34 | 33 | 37 | 13 | 33 | 29 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**35**| 0 | 0 | 0 | 7 | 50 | 24 | 25 | 45 | 40 | 35 | 50 | 41 | 35 | 14 | 0 | 20 | 35 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**36**| 0 | 0 | 0 | 0 | 0 | 0 | 10 | 43 | 21 | 23 | 50 | 31 | 54 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**37**| 0 | 0 | 0 | 3 | 9 | 4 | 19 | 69 | 59 | 28 | 53 | 57 | 33 | 11 | 28 | 40 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**38**| 0 | 0 | 12 | 39 | 44 | 38 | 42 | 58 | 19 | 23 | 48 | 61 | 15 | 51 | 11 | 24 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**39**| 0 | 0 | 16 | 33 | 37 | 43 | 43 | 2 | 10 | 32 | 2 | 46 | 31 | 41 | 39 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**40**| 0 | 0 | 0 | 20 | 29 | 23 | 11 | 12 | 23 | 37 | 4 | 32 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**41**| 0 | 0 | 0 | 10 | 17 | 8 | 0 | 1 | 0 | 22 | 0 | 28 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
|**42**| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 

Az ábrán az első oszlop, illetve az első sor a mérési adatok koordinátáját adja meg, például 12. sor 6. oszlopában lévő mérési eredmény 33 dm. (A tó medrét a nemnulla értékek jelzik.)

Rendelkezésére áll a **melyseg.txt** nevű adatfájl, amelynek első két sorában az adatokat tartalmazó táblázat sorainak majd oszlopainak száma található. A fájlban ezt a mérési adatok követik soronként, az adatokat szóköz választja el egymástól. A fájlban a sorok és oszlopok azonosítói nem szerepelnek. Például egy 42 sorból és 25 oszlopból álló táblázat esetén az első 4 sor adatai a fájlban:

```
42
25
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 3 0 0 0 0 0 8 10 10 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 19 10 0 11 16 18 10 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 9 17 35 5 11 11 22 18 0 0 0 0 0 0 0 0 0 0 0 0 0 0
...
```
Készítsen programot, amely az állomány adatait felhasználva az alábbi kérdésekre válaszol!
A program forráskódját mentse **banyato** néven! A megoldás során felhasználhatja, hogy a fájl legfeljebb 99 sort és legfeljebb 99 oszlopot tartalmaz. A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, és feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.

A képernyőre írást igénylő részfeladatok esetén – a mintához tartalmában hasonlóan – írja ki a képernyőre a feladat sorszámát (például: `3. feladat`), és utaljon a kiírt tartalomra is!
Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Mindkét esetben az ékezetmentes kiírás is elfogadott.

1. Olvassa be és tárolja el a **melyseg.txt** állomány adatait, és annak felhasználásával oldja meg a következő feladatokat!

2. Kérje be egy mérési eredmény sor- és oszlopazonosítóját, majd írassa ki az adott helyen mért adatot a képernyőre! (A sorok és oszlopok számozása kezdődjön 1-gyel!)

3. Határozza meg a tó felszínének területét, valamint a tó átlagos mélységét! Írassa ki a két eredményt a mintának megfelelően a képernyőre! A tó átlagos mélysége méterben kifejezve, két tizedesjegy pontossággal jelenjen meg!

4. Mekkora a tó legnagyobb mélysége, és hol a legmélyebb a tó? Jelenítse meg a választ a képernyőn! A legmélyebb pont koordinátáit a mintának megfelelően ( **sor** ; **oszlop** ) formában írassa ki! Ha több ilyen mérési eredmény is van, mindegyik koordinátapárja jelenjen meg!

5. Milyen hosszú a tó partvonala (nemnulla és nulla értékek által határot vízszintes és függőleges vonalak száma)? A partvonalhoz vegye hozzá a tóban lévő szigetek kerületét is! Írassa ki az eredményt a mintának megfelelően a képernyőre! (A megoldás során felhasználhatja, hogy a táblázat első és utolsó sorában és oszlopában minden adat 0.)

6. Kérje be a felhasználótól egy oszlop azonosítóját, és szemléltesse a **diagram.txt** szöveges állományban „sávdiagramon” a tó mélységét az adott oszlopban a következő módon! A sor elején jelenjen meg a mérési adat sorának azonosítója pontosan két számjeggyel, majd tegyen egymás mellé annyi csillagot (\*), ahány méter az adott helyen a tó mélysége! A mérési adatokat a matematika szabályainak megfelelően kerekítse!

### Példa a szöveges kimenetek kialakításához (a tizedesjel az alkalmazott fejlesztői környezettől függően eltérhet):
```
2. feladat
A mérés sorának azonosítója = 12
A mérés oszlopának azonosítója =  6
A mért mélység az adott helyen 33 dm

3. feladat
A tó felszíne: 646 m2, átlagos mélysége: 4,28 m

4. feladat
A tó legnagyobb mélysége: 98 dm
A legmélyebb helyek sor-oszlop koordinátái:
(14; 20) (26; 11) (32; 16)

5. feladat
A tó partvonala 270 m hosszú

6. feladat
A vizsgált szelvény oszlopának azonosítója = 6 
``` 

### Példa a _diagram_. _txt_ szöveges állomány tartalmára:

```
01
02
03**
04****
05******
06******
07***
08*****
...
```

