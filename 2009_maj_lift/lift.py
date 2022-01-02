import random

class Igeny():
    def __init__(self, line):
        global csapatszamok
        datas = line.strip().split(" ")
        self.ora = int(datas[0])
        self.perc = int(datas[1])
        self.mperc = int(datas[2])
        self.csapat = int(datas[3])
        self.honnan = int(datas[4])
        self.hova = int(datas[5])
        # csapat sorszámának letárolása
        if csapatszamok.count(self.csapat) == 0:
            csapatszamok.append(self.csapat)

igenyek = []
csapatszamok = []

# 1. Olvassa be az igeny.txt állományban talált adatokat, s azok felhasználásával oldja meg a következő feladatokat!
#   Ha az állományt nem tudja beolvasni, az első 8 igényhez tartozó adatokat jegyezze be a programba és dolgozzon azzal!
print("\n1.feladat")
with open("igeny.txt", "r") as fileBe:
    szintek_szama = int(fileBe.readline().strip())
    csapatok_szama = int(fileBe.readline().strip())
    igenyek_szama = int(fileBe.readline().strip())
    for line in fileBe:
        igeny = Igeny(line)
        igenyek.append(igeny)
print("Adatok beolvasva a 'igeny.txt állományból' ")

# 2. Tudjuk, hogy a megfigyelés kezdetén a lift éppen áll.
#   Kérje be a felhasználótól, hogy melyik szinten áll a lift, és a további részfeladatok megoldásánál ezt vegye figyelembe!
#   Ha a beolvasást nem tudja elvégezni, használja az igény.txt fájlban az első igény induló szintjét!
print("\n2.feladat")
lift_szint = int(input("Lift szintje = "))

# 3. Határozza meg, hogy melyik szinten áll majd a lift az utolsó kérés teljesítését követően!
#   Írja képernyőre a választ a következőhöz hasonló formában: „A lift a 33. szinten áll az utolsó igény teljesítése után.” !
print("\n3.feladat")
print(f"A lift a {igenyek[-1].hova}. szinten áll az utolsó igény teljesítése után.")

# 4. Írja a képernyőre, hogy a megfigyelés kezdete és az utolsó igény teljesítése között melyik volt a legalacsonyabb és melyik a legmagasabb sorszámú szint, amelyet a lift érintett!
print("\n4.feladat")
min_szint = lift_szint
max_szint = lift_szint
for igeny in igenyek:
    if igeny.honnan < min_szint:
        min_szint = igeny.honnan
    if igeny.hova < min_szint:
        min_szint = igeny.hova
    if igeny.honnan > max_szint:
        max_szint = igeny.honnan
    if igeny.hova > max_szint:
        max_szint = igeny.hova
print(f"Legalacsonyabb szint: {min_szint}. Legmagasabb szint:{max_szint}")

# 5. Határozza meg, hogy hányszor kellett a liftnek felfelé indulnia utassal és hányszor utas nélkül!
print("\n5.feladat")
akt_lift_szint = lift_szint
fel_ures = 0
fel_teli = 0
for igeny in igenyek:
    if akt_lift_szint < igeny.honnan:
        fel_ures += 1
    akt_lift_szint = igeny.honnan
    if igeny.honnan < igeny.hova:
        fel_teli += 1
    akt_lift_szint = igeny.hova
print(f"A lift {fel_ures} alkalommal ment felfelé utas nélkül és {fel_teli} alkalommal utassal")

# 6. Határozza meg, hogy mely szerelőcsapatok nem vették igénybe a liftet a vizsgált intervallumban!
#   A szerelőcsapatok sorszámát egymástól egy-egy szóközzel elválasztva írja a képernyőre!
print("\n6.feladat")
csapatok = [0 for i in range(0,csapatok_szama+1)]
for igeny in igenyek:
    csapatok[igeny.csapat] += 1
csapatlista = ""
for i in range(1, csapatok_szama+1):
    if csapatok[i] == 0:
        csapatlista += str(i) + " "
print(f"Szerelőcsapatok, akik nem vették igénybe a liftet: {csapatlista}")

# 7. Előfordul, hogy egyik vagy másik szerelőcsapat áthágja a szabályokat, és egyik szintről gyalog megy a másikra.
#   (Ezt onnan tudhatjuk, hogy más emeleten igényli a liftet, mint ahova korábban érkezett.)
#   Generáljon véletlenszerűen egy létező csapatsorszámot! (Ha nem jár sikerrel, dolgozzon a 3. csapattal!)
#   Határozza meg, hogy a vizsgált időszak igényei alapján lehet-e egyértelműen bizonyítani, hogy ez a csapat vétett a szabályok ellen!
#   Ha igen, akkor adja meg, hogy melyik két szint közötti utat tették meg gyalog, ellenkező esetben írja ki a Nem bizonyítható szabálytalanság szöveget!
print("\n7.feladat")
csapat = random.choice(csapatszamok)
szabalyos = True
# csapat első igényének megkeresése
i = 0
while igenyek[i].csapat != csapat and  i < len(igenyek):
    i += 1
hol = igenyek[i].hova
# az összes többi igények végigmegyünk
while i < len(igenyek)-1:
    i += 1
    if igenyek[i].csapat == csapat:         # ha a vizsgált csapaté az igény
        if igenyek[i].honnan != hol:        # ha a honnan értéke nem egyezik ahol van a csapat
            szabalyos = False
            print(f"{hol} szintről gyalog ment a {csapat}. csapat a {igenyek[i].honnan} szintre!")
        hol = igenyek[i].hova               # csapat aktuális helyzete (szintje)
if szabalyos:
    print(f"Nem bizonyítható szabálytalanság a {csapat}. csapat esetén.")

# 8. A munkák elvégzésének adminisztrálásához minden csapatnak egy blokkoló kártyát kell használnia.
#   A kártyára a liftben elhelyezett blokkolóóra rögzíti az emeletet, az időpontot.
#   Ennek a készüléknek a segítségével kell megadni a munka kódszámát és az adott munkafolyamat sikerességét.
#   A munka kódja 1 és 99 közötti egész szám lehet. A sikerességet a „befejezett” és a „befejezetlen” szavakkal lehet jelezni.
#   Egy műszaki hiba folytán az előző feladatban vizsgált csapat kártyájára az általunk nyomon követett időszakban nem került bejegyzés.
#   Ezért a csapatfőnöknek a műszak végén pótolnia kell a hiányzó adatokat.
#   Az igeny.txt állomány adatait felhasználva írja a képernyőre időrendben, hogy a vizsgált időszakban milyen kérdéseket tett fel az óra, és kérje be az adott válaszokat a felhasználótól!
#   A pótlólag feljegyzett adatokat írja a blokkol.txt állományba!
print("\n8.feladat")
# WTF: a feladatkitűzés során fogalmazásgátlót szedhetett be a feladat kitűzője...
# a  debug értékét False-ra kell állítani, hogy ne generálja, hanem bekérje a program az adatokat
debug = True
with open("blokkol.txt", "w", encoding="UTF-8") as fileKi:
    for igeny in igenyek:
        if igeny.csapat == csapat:
            if debug:
                feladatkod = str(random.randint(1,99))
                sikeresseg = random.choice(["befejezett", "befejezetlen"])
            else:
                feladatkod = input("Feladatkód = ")
                sikeresseg = input("Sikeresség = ")
            fileKi.writelines(f"Indulási emelet: {igeny.honnan}\n")
            fileKi.writelines(f"Cél emelet: {igeny.hova}\n")
            fileKi.writelines(f"Feladatkód: {feladatkod}\n")
            fileKi.writelines(f"Befejezés ideje: {igeny.ora}:{igeny.perc}:{igeny.mperc}\n")
            fileKi.writelines(f"Sikeresség: {sikeresseg}\n")
            fileKi.writelines(f"-----\n")
print(f"A {csapat}. csapat adatai kiírva a 'blokkol.txt' állományba.")