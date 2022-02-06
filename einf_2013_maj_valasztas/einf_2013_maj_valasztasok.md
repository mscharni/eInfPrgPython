# Emelt Informatika Érettségi - 2013 május - Választások

## Feladat
Eszemiszom városában időközi helyhatósági választásokat írtak ki. A városban összesen 12 345 szavazásra jogosult állampolgár van, akiket nyolc választókerületbe soroltak.

Minden választókerületben több jelölt is indul, de egy jelölt csak egy választókerületben indulhat. Egy választókerület szavazói az adott választókerületben induló jelöltek közül egy jelöltre adhatnak le szavazatot, de nem kötelező részt venniük a szavazáson. Minden választókerületben az a jelölt nyer, aki a legtöbb szavazatot kapja. (Feltételezheti, hogy egyetlen választókerületben sem alakult ki holtverseny.)

A jelöltek vagy egy párt támogatásával, vagy független jelöltként indulhatnak. Az idei évben a Gyümölcsevők Pártja (GYEP), a Húsevők Pártja (HEP), a Tejivók Szövetsége (TISZ) vagy a Zöldségevők Pártja (ZEP) támogatja a jelölteket.

A szavazás eredményét a **_szavazatok.txt_** szóközökkel tagolt fájl tartalmazza, amelynek minden sorában egy-egy képviselőjelölt adatai láthatók.

### Például:
```
8 149 Zeller Zelma ZEP
6 63 Zsoldos Zsolt -
```

Az első két adat a választókerület sorszáma és a képviselőjelöltre leadott szavazatok száma. Ezt a jelölt vezeték- és utóneve, majd a jelöltet támogató párt hivatalos rövidítése követi. Független jelöltek esetében a párt rövidítése helyett egy kötőjel szerepel. Minden képviselőjelöltnek pontosan egy utóneve van.

Készítsen programot **_valasztas_** néven, amely az alábbi kérdésekre válaszol!

Minden részfeladat feldolgozása során írja ki a képernyőre a részfeladat sorszámát, (például: `2. feladat`)! Ahol a felhasználótól kér be adatot, ott írja ki a képernyőre azt is, hogy milyen adatot vár! Az ékezetmentes kiírás is elfogadott.

1. Olvassa be a _szavazatok.txt_ fájl adatait, majd ezek felhasználásával oldja meg a következő feladatokat! Az adatfájlban legfeljebb 100 képviselőjelölt adatai szerepelnek.

2. Hány képviselőjelölt indult a helyhatósági választáson? A kérdésre egész mondatban válaszoljon az alábbi mintához hasonlóan:
`A helyhatósági választáson 92 képviselőjelölt indult.`

3. Kérje be egy képviselőjelölt vezetéknevét és utónevét, majd írja ki a képernyőre, hogy az illető hány szavazatot kapott! Ha a beolvasott név nem szerepel a nyilvántartásban, úgy jelenjen meg a képernyőn az „`Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!`” figyelmeztetés! A feladat megoldása során feltételezheti, hogy nem indult két azonos nevű képviselőjelölt a választáson.

4. Határozza meg, hányan adták le szavazatukat, és mennyi volt a részvételi arány! (A részvételi arány azt adja meg, hogy a jogosultak hány százaléka vett részt a szavazáson.) A részvételi arányt két tizedesjegy pontossággal, százalékos formában írja ki a képernyőre!
Például:
`A választáson 5001 állampolgár, a jogosultak 40,51%-a vett részt.`

5. Határozza meg és írassa ki a képernyőre az egyes pártokra leadott szavazatok arányát az összes leadott szavazathoz képest két tizedesjegy pontossággal! A független jelölteket együtt, „`Független jelöltek`” néven szerepeltesse!
Például:
```
Zöldségevők Pártja= 12,34%
Független jelöltek= 23,40%
```

6. Melyik jelölt kapta a legtöbb szavazatot? Jelenítse meg a képernyőn a képviselő vezeték- és utónevét, valamint az őt támogató párt rövidítését, vagy azt, hogy `független`! Ha több ilyen képviselő is van, akkor mindegyik adatai jelenjenek meg!

7. Határozza meg, hogy az egyes választókerületekben kik lettek a képviselők! Írja ki a választókerület sorszámát, a győztes vezeték- és utónevét, valamint az őt támogató párt     rövidítését, vagy azt, hogy független egy-egy szóközzel elválasztva a **_kepviselok.txt_** nevű szöveges fájlba! Az adatok a választókerületek száma szerinti sorrendben jelenjenek meg! Minden sorba egy képviselő adatai kerüljenek!
