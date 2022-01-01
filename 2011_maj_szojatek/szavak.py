# 1. Kérjen be a felhasználótól egy szót, és döntse el, hogy tartalmaz-e magánhangzót!
#   Amennyiben tartalmaz, írja ki, hogy „Van benne magánhangzó.”! Ha nincs, akkor írja ki, hogy „Nincs benne magánhangzó.”!
#   A begépelendő szóról feltételezheti, hogy csak az angol ábécé kisbetűit tartalmazza.
#   (Az angol ábécé magánhangzói: a, e, i, o, u.)
print("\n1. feladat")
def count_maganhangzo(szo):
    magan = 0
    magan += szo.count('a')
    magan += szo.count('e')
    magan += szo.count('i')
    magan += szo.count('o')
    magan += szo.count('u')
    return magan

szo = input("Adjon meg egy szót: ")
if count_maganhangzo(szo) == 0:
    print("Nincs benne magánhangzó.")
else:
    print("Van benne magánhangzó.")

# 2. Írja ki a képernyőre, hogy melyik a leghosszabb szó a szoveg.txt állományban, és az hány karakterből áll!
#   Ha több azonos leghosszabb hosszúságú szó is van a szógyűjteményben, akkor azok közül elegendő egyetlen szót kiírnia.
#   A feladatot úgy oldja meg, hogy tetszőleges hosszúságú szövegállomány esetén működjön, azaz a teljes szöveget ne tárolja a memóriában!
print("\n2. feladat")
hosszu_szo = ""
magan_szavak = ""
magan_szo = 0
ossz_szo = 0
ot_szo = []
with open("szoveg.txt", "r") as file:
    for line in file:
        ossz_szo += 1
        szo = line.strip()
        if len(szo) < count_maganhangzo(szo) * 2:
            magan_szo += 1
            magan_szavak += szo + " "
        # 3. feladathoz
        if len(szo) > len(hosszu_szo):
            hosszu_szo = line
        # 4. feladathoz
        if len(szo) == 5:
            ot_szo.append(szo)

print(f"A leghosszabb szó: '{hosszu_szo}'")

# 3. A magyar nyelv szavaiban általában kevesebb a magánhangzó, mint a mássalhangzó.
#   Határozza meg, hogy az állomány mely szavaiban van több magánhangzó, mint egyéb karakter!
#   Ezeket a szavakat írja ki a képernyőre egy-egy szóközzel elválasztva! A szavak felsorolása után a mintának megfelelően az alábbi adatokat adja meg:
#       • hány szót talált;
#       • hány szó van összesen az állományban;
#       • a talált szavak hány százalékát teszik ki az összes szónak!
#           A százalékot két tizedessel szerepeltesse!
print("\n3. feladat")
print(magan_szavak)
print(f"Talált szavak száma: {magan_szo}")
print(f"Összes szavak száma: {ossz_szo}")
print(f"A talált szavak száma {magan_szo/ossz_szo:.2%}-a z összes szónak")

#
# 4. Hozzon létre egy tömb vagy lista adatszerkezetet, és ebbe gyűjtse ki a fájlban található ötkarakteres szavakat!
#   A szoveg.txt állomány legfeljebb 1000 darab ötkarakteres szót tartalmaz.
#   Kérjen be a felhasználótól egy 3 karakteres szórészletet!
#   Írja ki a képernyőre a szólétra építés szabályai szerint hozzá tartozó ötkarakteres szavakat a tárolt adathalmazból!
#   A kiírásnál a szavakat egy-egy szóköz válassza el!
#   (Teszteléshez használhatja például az „isz” vagy „obo” szórészleteket, mert ezekhez a megadott szövegállományban több létraszó is tartozik.)
print("\n4. feladat")
szo_resz = input("Adjon meg egy három betűs szórészletet = ")
def get_letra(szo_resz):
    letra_szavak = ""
    for szo in ot_szo:
        if szo[1:4] == szo_resz:
            letra_szavak += szo + " "
    return letra_szavak
print(get_letra(szo_resz))

# 5. Az eltárolt ötkarakteres szavakból csoportosítsa azokat a szavakat, melyek ugyanannak a hárombetűs szórészletnek a létraszavai!
#   Hozzon létre egy letra.txt állományt, amelybe ezeket a szavakat írja az alábbiak szerint:
#       • minden szó külön sorba kerüljön;
#       • csak olyan szó szerepeljen az állományban, aminek van legalább egy párja, amivel egy létrát alkotnak (azaz első és utolsó karakter nélkül megegyeznek);
#       • az egy létrához tartozó szavak közvetlenül egymás után helyezkedjenek el;
#       • két létra szavai között egy üres elválasztó sor legyen!
print("\n5. feladat")
# rendezzük az ötbetűs szavak középső három betűje szerint (így egymás után szerepelnek a létraszavak)
def letrarendez(szo):
    return szo[1:4]
ot_szo.sort(key=letrarendez)

letra_count = 0
letra_idx = 0
letra_list = []
with open("letra.txt", "w") as file:
    for i in range(0, len(ot_szo)):
        if ot_szo[letra_idx][1:4] != ot_szo[i][1:4]:
            # új belsejű létraszó, letároljuk az indexét
            letra_idx = i
            # ha az eddigi gyűjtésben legalább két szó van, akkor ki kell írni és sort kell emelni
            if len(letra_list) > 1:
                for letra_szo in letra_list:
                    file.writelines(letra_szo+"\n")
                file.writelines("\n")
                letra_count +=1
            # törölni kell az eddigi listát
            letra_list = []
        # berakjuk a listába az aktuáluis szót
        letra_list.append(ot_szo[i])
print(f"Összesen {letra_count} féle létrát (csoportot) határoz meg a {len(ot_szo)} ötbetűs szó")
print("Adatok kiírva a 'letra.txt' állományba.")



