### Emelt Informatika Érettségi - 2006 május - Fehérje

class Feherje():
    def __init__(self, datas):
        self.rov = datas[0].strip()
        self.betu = datas[1].strip()
        self.C = int(datas[2].strip())
        self.H = int(datas[3].strip())
        self.O = int(datas[4].strip())
        self.N = int(datas[5].strip())
        self.S = int(datas[6].strip())
        self.moltom = self.C *12 + self.H + self.O*16 + self.N*14 + self.S*32

# fehérjéket tartalmazó lista
feherjek = []
# fehérjéket tartalmazó szótár: kulcs a fehérje betűjele, értéke a fehérje objektum
f_dict = {}


# 1., Töltse be az aminosav.txt fájlból az aminosavak adatait!
#   A fájlban minden adat külön sorban található, a fájl az aminosavak nevét nem tartalmazza.
print("\n1. feladat")
with open("aminosav.txt", "r") as fileBe:
    lines = fileBe.readlines()
# beolvasott adatok (sortöréssel)
# ['Gly', 'G', '2', '5', '2', '1', '0', 'Ala', 'A', '3', '7', '2', '1', '0', ...]
# hét egymást követő sor egy fehérje adatait tartalmazza, amely fehérje-listákból egy adatlistát képzünk:
# eredmény (sortöréssel)
# ['Gly', 'G', '2', '5', '2', '1', '0'], ['Ala', 'A', '3', '7', '2', '1', '0'],...]
datalines = [lines[line:line+7] for line in range(0,len(lines),7)]
for datas in datalines:
    # objektumban tároljuk el egy-egy fehérje adatait
    feherje = Feherje(datas)
    # amelyet egy listába szervezünk
    feherjek.append(feherje)
    # valamint letároljuk egy szótárban, ahol a kulcs a fehérje azonosítója, az érték pedig maga a fehérje objektuma
    f_dict[feherje.betu] = feherje
print("Adatok beolvasva az 'aminosavak.txt' állományból")


# 2. Határozza meg az aminosavak relatív molekulatömegét, ha a szén atomtömege 12, a hidrogéné 1, az oxigéné 16, a nitrogéné 14 és a kén atomtömege 32!
# Például a Glicin esetén a relatív molekulatömeg 2·12 + 5·1 + 2·16 + 1·14 + 0·32 = 75.
print("\n2. feladat")
print("A 'Feherje' osztály objektum-inicializációs részében")


# 3. Rendezze növekvő sorrendbe az aminosavakat a relatív molekulatömeg szerint!
# Írja ki a képernyőre és az eredmeny.txt fájlba az aminosavak hárombetűs azonosítóját és a molekulatömeget!
# Az azonosítót és hozzátartozó molekulatömeget egy sorba, szóközzel elválasztva írja ki!
print("\n3. feladat")
# a molekulatömeg szerinti rendezéshez szükséges egyedi rendezőfüggvény
def sort_by_moltom(feherje):
    return feherje.moltom
# fehérjéket tartalmazó lista rendezése (molekulatömeg szerint)
feherjek.sort(key = sort_by_moltom)
with open("eredmeny.txt", "w") as fileKi:
    for feherje in feherjek:
        fileKi.write(f"{feherje.rov} {feherje.moltom}\n")
print("Adatok kiírva az 'eredmeny.txt' állományba.")


# 4. A bsa.txt a BSA nevű fehérje aminosav sorrendjét tartalmazza – egybetűs jelöléssel.
#   (A fehérjelánc legfeljebb 1000 aminosavat tartalmaz.)
#   Határozza meg a fehérje összegképletét (azaz a C, H, O, N és S számát)!
#   A meghatározásánál vegye figyelembe, hogy az aminosavak összekapcsolódása során minden kapcsolat létrejöttekor egy vízmolekula (H2O) lép ki!
#   Az összegképletet a képernyőre és az eredmeny.txt fájlba az alábbi formában írja ki:
#   Például: C 16321 H 34324 O 4234 N 8210 S 2231
print("\n4. feladat")
# bsa üres fehérje létrehozása kétféle módon
# bsa = Feherje("bsa - 0 0 0 0 0".split(" "))
bsa = Feherje(['bsa', '-', '0', '0', '0', '0', '0'])

bsa_seq = ""
with open("bsa.txt", "r") as fileBe:
    for f in fileBe:
        f_kod = f.strip()
        bsa_seq += f_kod    # 5. feladathoz
        feherje = f_dict[f_kod] 
        bsa.C += feherje.C
        bsa.H += feherje.H - 2 # H2O kilépés miatt
        bsa.O += feherje.O - 1 # H2O kilépés miatt
        bsa.N += feherje.N
        bsa.S += feherje.S
    # eggyel több H2O-t vontunk ki
    bsa.H += 2 
    bsa.O += 1 
print(f"C {bsa.C} H {bsa.H} O {bsa.O} N {bsa.N} S {bsa.S}")

# hozzáfűzésre nyitjuk meg a kimeneti állományt
with open("eredmeny.txt", "a") as fileKi:
    fileKi.write(f"C {bsa.C} H {bsa.H} O {bsa.O} N {bsa.N} S {bsa.S}\n")
print("Adatok kiírva az 'eredmeny.txt' állományba.")


# 5. A fehérjék szekvencia szerkezetét hasításos eljárással határozzák meg.
# Egyes enzimek bizonyos aminosavak után kettéhasítják a fehérjemolekulát.
# Például a Kimotripszin enzim a Tirozin (Y), Fenilalanin (W) és a Triptofán (F) után hasít.
# Határozza meg, és írja ki képernyőre a Kimotripszin enzimmel széthasított BSA lánc leghosszabb darabjának hosszát és az eredeti láncban elfoglalt helyét (első és utolsó aminosavának sorszámát)!
# A kiíráskor nevezze meg a kiírt adatot, például: „kezdet helye:”!
print("\n5. feladat")
max_hossz = 0
max_start = 0
max_end = 0
for idx in range(0,len(bsa_seq)):
    # ha hasít
    if bsa_seq[idx] in ["Y", "W", "F"]:
        #ha hosszabb, mint eddig
        if idx-max_end + 1 > max_hossz:
            max_start = max_end
            max_end = idx + 1
            max_hossz = max_end - max_start 

# ha legutolsó szelet hosszabb, mint eddig
if len(bsa_seq)-max_end + 1 > max_hossz:
    max_start = max_end
    max_end = len(bsa_seq) + 1
    max_hossz = max_end - max_start 
print(f"Leghosszabb darab hossza: {max_hossz}, kezdete: {max_start+1}, vége: {max_end}")


# 6. Egy másik enzim (a Factor XI) az Arginin (R) után hasít, de csak akkor, ha Alinin (A) vagy Valin (V) követi.
#   Határozza meg, hogy a hasítás során keletkező első fehérjelánc részletben hány Cisztein (C) található!
#   A választ teljes mondatba illesztve írja ki a képernyőre!
print("\n6. feladat")
idx = 0
while bsa_seq[idx:idx+2] != "RA" and bsa_seq[idx:idx+2] != "RV" :
    idx += 1
print(f"A hasítás során keletkező első fehérjelánc részletben {bsa_seq[0:idx].count('C')} Cisztein (C) található.")
