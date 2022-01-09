# Emelt Informatika Érettségi - 2007 május - SMS szavak

## Feladat
Napjainkban a kommunikáció egy elterjedt formája az SMS-küldés. Az SMS-küldésre alkalmas telefonok prediktív szövegbevitellel segítik az üzenetek megírását. Ennek használatakor a szavakat úgy tudjuk beírni, hogy a telefon számbillentyűjén található betűknek megfelelő számokat kell beírnunk. A számok és betűk megfeleltetését az alábbi táblázat mutatja:

|            |          |            |
| :--------- | :------: | :--------: |
|            | 2 A B C  |   3 D E F  |
|   4 G H I  | 5 J K L  |   6 M N O  |
| 7 P Q R S  | 8 T U V  | 9 W X Y Z  |


Ha meg szeretnénk jeleníteni az „ _ablak_ ” szót, akkor a _22525_ kódot kell beírnunk. A telefon a tárolt szótára alapján a kódhoz kikeresi a megfelelő szót. Ha több szóhoz is azonos kód tartozik, akkor a kódhoz tartozó összes szót felkínálja választásra. Egy ilyen szógyűjteményt talál a **_szavak.txt_** fájlban. A fájlról a következőket tudjuk:

- Legfeljebb 600 szó található benne.
- Minden szó külön sorban található.
- A szavak hossza maximum 15 karakter.
- A szavak mindegyike csak az angol ábécé kisbetűit tartalmazza.
- Minden szó legfeljebb egyszer szerepel.

Írjon **_sms_** néven programot, ami a szógyűjtemény felhasználásával megoldja az alábbi feladatokat!

1. Kérjen be a felhasználótól egy betűt, és adja meg, hogy milyen kód (szám) tartozik hozzá! Az eredményt írassa a képernyőre!

2. Kérjen be a felhasználótól egy szót, és határozza meg, hogy milyen számsorral lehet ezt a telefonba bevinni! Az eredményt írassa a képernyőre!

3. Olvassa be a **_szavak.txt_** fájlból a szavakat, és a továbbiakban azokkal dolgozzon! Ha nem tudja az állományból beolvasni az adatokat, akkor az állományban található „**b**” kezdőbetűs szavakat gépelje be a programba, és azokkal oldja meg a feladatokat!

4. Határozza meg és írassa a képernyőre, hogy melyik a leghosszabb tárolt szó! Amennyiben több azonos hosszúságú van, elegendő csak az egyiket megjeleníteni. Adja meg ennek a szónak a hosszát is!

5. Határozza meg és írassa a képernyőre, hogy hány rövid szó található a fájlban! Rövid szónak tekintjük a legfeljebb 5 karakterből álló szavakat.

6. Írassa a **_kodok.txt_** állományba a **_szavak.txt_** fájlban található szavaknak megfelelő számkódokat! Minden szónak feleljen meg egy számkód, és minden számkód külön sorba kerüljön!

7. Kérjen be a felhasználótól egy számsort, és határozza meg, hogy melyik szó tartozhat hozzá! Amennyiben több szó is megfelelő, akkor mindegyiket írassa ki! (Teszteléshez használhatja például a **_225_** számsort, mivel ehhez egynél több szó tartozik a szógyűjteményben.)

8. Határozza meg, hogy a szógyűjteményben mely kódokhoz tartozik több szó is! Írassa ki a képernyőre ezeket a szavakat a kódjukkal együtt egymás mellé az alábbi mintának megfelelően (a szavak sorrendje ettől eltérhet):
```
baj : 225; bal : 225; arc : 272; apa : 272; eb : 32; fa : 32; dal : 325; fal : 325; eltesz : 358379; elvesz : 358379; fojt : 3658; folt : 3658; ...
```

9. Határozza meg, hogy melyik kódnak megfelelő szóból van a legtöbb! Írassa ki a képernyőre a kódot, és a kódhoz tartozó összes tárolt szót! Ha több kódhoz is azonos számú szó tartozik, akkor elegendő ezen kódok közül csak az egyikkel foglalkozni.
