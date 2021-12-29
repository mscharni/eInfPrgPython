class Versenyzo :
    azon = ""
    tippek = ""
    osszpont = 0 

versenyzok = []

# 1. feladat: Olvassa be és tárolja el a valaszok.txt szöveges állomány adatait!
print("\n1. feladat: Az adatok beolvasása")
with open("valaszok.txt", "r") as fileBe:
    megoldasok = fileBe.readline().strip()
    for sor in fileBe:
        adat = sor.strip().split()
        versenyzo = Versenyzo()
        versenyzo.azon = adat[0]
        versenyzo.tippek = adat[1]
        versenyzo.osszpont = 0
        versenyzok.append(versenyzo)

# 2. feladat: Jelenítse meg a képernyőn a mintának megfelelően, hogy hány versenyző vett részt a tesztversenyen!
print(f"\n2. feladat:A vetélkedőn {len(versenyzok)} versenyző indult.")


# 3. feladat: Kérje be egy versenyző azonosítóját, és jelenítse meg a mintának megfelelően a hozzá eltárolt válaszokat!
#   Feltételezheti, hogy a fájlban létező azonosítót adnak meg.

# (A verzió)
beAzon = input(f"\n3. feladat: A versenyző azonosítója = ")
i = 0
while versenyzok[i].azon == beAzon:
    i += 1
tipp = versenyzok[i-1].tippek
print(f"{tipp:18} (a versenyző helyes válaszai)")

# (B verzió: break használata kerülendő)
# for versenyzo in versenyzok:
#     if versenyzo.azon == beAzon:
#         tipp = versenyzo.tippek
#         print(f"{tipp:18} (a versenyző helyes válaszai)")
#         break #megszakítjuk a ciklust (kilépünk a ciklusból)

# 4. feladat: Írassa ki a képernyőre a helyes megoldást!
#   A helyes megoldás alatti sorba „+” jelet tegyen, ha az adott feladatot az előző feladatban kiválasztott versenyző eltalálta, egyébként egy szóközt!
#   A kiírást a mintának megfelelő módon alakítsa ki!
print("\n4. feladat:")
tippekJo = ""
for i in range(0,len(megoldasok)):
    if (megoldasok[i] == tipp[i]):
        tippekJo += "+"
    else :
        tippekJo += " "
    
print(f"{megoldasok:18} (a helyes megoldás)")
print(f"{tippekJo:18} (a versenyző helyes válaszai)")

# 5. feladat: Kérje be egy feladat sorszámát, majd határozza meg, hogy hány versenyző adott a feladatra helyes megoldást, és ez a versenyzők hány százaléka!
# A százalékos eredményt a mintának megfelelően, két tizedesjeggyel írassa ki!
joValaszadok = 0
sorszam = int(input("\n5. feladat: A feladat sorszáma = "))-1     #sorszám 0-tól indul
for versenyzo in versenyzok:
        if versenyzo.tippek[sorszam] == megoldasok[sorszam]:
            joValaszadok += 1
arany = joValaszadok / len(versenyzok)
print(f"A feladatra {joValaszadok} fő, a versenyzők {arany:.2%}-a adott helyes választ.")

# 6. feladat: A verseny feladatai nem egyenlő nehézségűek: az 1-5. feladat 3 pontot, a 6-10. feladat 4 pontot, a 11-13. feladat 5 pontot, míg a 14. feladat 6 pontot ér.
#   Határozza meg az egyes versenyzők pontszámát, és a listát írassa ki a pontok.txt nevű állományba!
#   Az állomány minden sora egy versenyző kódját, majd szóközzel elválasztva az általa elért pontszámot tartalmazza!
print("\n6. feladat: A versenyzők pontszámának meghatározása")
# (A verzió) Kezdeti értékkel
ertek = [3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6]
with open("pontok.txt", "w") as fileKi:
    for versenyzo in versenyzok:
        osszPont = 0
        for i in range(0, len(versenyzo.tippek)):
            if versenyzo.tippek[i] == megoldasok[i]:
                    osszPont += ertek[i]
        versenyzo.osszpont = osszPont
        fileKi.writelines(f"{versenyzo.azon} {osszPont}\n")
# (B verzió) Sok elágazással
# with open("pontok.txt", "w") as fileKi:
#     for versenyzo in versenyzok:
#         osszPont = 0
#         for i in range(0, len(versenyzo.tippek)):
#             if versenyzo.tippek[i] == megoldasok[i]:
#                 if i < 5 :
#                     osszPont += 3
#                 elif i < 10:
#                     osszPont += 4
#                 elif i < 13:
#                     osszPont += 5
#                 else:
#                     osszPont += 6
#         versenyzo.osszpont = osszPont
#         fileKi.writelines(f"{versenyzo.azon} {osszPont}\n")

# 7. feladat: A versenyen a három legmagasabb pontszámot elérő összes versenyzőt díjazzák.
#   Például 5 indulónál előfordulhat, hogy 3 első és 2 második díjat adnak ki.
#   Így megtörténhet az is, hogy nem kerül sor mindegyik díj kiadására.
#   Írassa ki a mintának megfelelően a képernyőre a díjazottak kódját és pontszámát pontszám szerint csökkenő sorrendben!
print("\n7. feladat: A verseny legjobbjai:")
# megkeresessük a három legnagyobb értéket
max = [0,0,0]
for versenyzo in versenyzok:
    if versenyzo.osszpont > max[0]:
        max[2] = max[1]
        max[1] = max[0]
        max[0] = versenyzo.osszpont
    else: 
        if versenyzo.osszpont < max[0] and versenyzo.osszpont > max[1]:
            max[2] = max[1]
            max[1] = versenyzo.osszpont
        else: 
            if versenyzo.osszpont < max[1] and versenyzo.osszpont > max[2]:
                max[2] = versenyzo.osszpont
# kiiratjuk a három legmagasabb értékhez tartozó versenyzőket
for i in range(0,3):
    for versenyzo in versenyzok:
        if versenyzo.osszpont == max[i]:
            print(f"{i+1}. díj ({versenyzo.osszpont} pont): {versenyzo.azon}")
