### Emelt Informatika Érettségi - 2006 május - Fehérje

# fehérjéket tartalmazó lista
feherjek = []
# fehérjéket tartalmazó szótár: kulcs a fehérje betűjele, értéke a fehérje objektum
f_dict = {}


# 1., Töltse be az aminosav.txt fájlból az aminosavak adatait!
#   A fájlban minden adat külön sorban található, a fájl az aminosavak nevét nem tartalmazza.
print("\n1. feladat")
with open("aminosav.txt", "r") as fileBe:
    lines = fileBe.readlines()
# hetesével végigmegyünk az adatokon és letároljuk a fehérjék összetartozó adatait egy szótárban
for i in range(0, len(lines), 7):
    # szótárban tároljuk el egy-egy fehérje adatait
    feherje = {
        'rov' : lines[i+0].strip(),
        'betu' : lines[i+1].strip(),
        'C' : int(lines[i+2].strip()),
        'H' : int(lines[i+3].strip()),
        'O' : int(lines[i+4].strip()),
        'N' : int(lines[i+5].strip()),
        'S' : int(lines[i+6].strip()),
    }
    feherje['moltom'] = feherje['C'] *12 + feherje['H'] + feherje['O']*16 + feherje['N']*14 + feherje['S']*32
    # amelyet egy listába szervezünk
    feherjek.append(feherje)
    # valamint letároljuk egy szótárban, ahol a kulcs a fehérje azonosítója, az érték pedig maga a fehérje objektuma
    f_dict[feherje['betu']] = feherje
print("Adatok beolvasva az 'aminosavak.txt' állományból")


# 2. Határozza meg az aminosavak relatív molekulatömegét, ha a szén atomtömege 12, a hidrogéné 1, az oxigéné 16, a nitrogéné 14 és a kén atomtömege 32!
# Például a Glicin esetén a relatív molekulatömeg 2·12 + 5·1 + 2·16 + 1·14 + 0·32 = 75.
print("\n2. feladat")
print("A 'feherje' szótár létrehozása során")


# 3. Rendezze növekvő sorrendbe az aminosavakat a relatív molekulatömeg szerint!
# Írja ki a képernyőre és az eredmeny.txt fájlba az aminosavak hárombetűs azonosítóját és a molekulatömeget!
# Az azonosítót és hozzátartozó molekulatömeget egy sorba, szóközzel elválasztva írja ki!
print("\n3. feladat")
# a molekulatömeg szerinti rendezéshez szükséges egyedi rendezőfüggvény
def sort_by_moltom(feherje):
    return feherje['moltom']
# fehérjéket tartalmazó lista rendezése (molekulatömeg szerint)
feherjek.sort(key = sort_by_moltom)
with open("eredmeny_dict.txt", "w") as fileKi:
    for feherje in feherjek:
        fileKi.write(f"{feherje['rov']} {feherje['moltom']}\n")
print("Adatok kiírva az 'eredmeny_dict.txt' állományba.")


# 4. A bsa.txt a BSA nevű fehérje aminosav sorrendjét tartalmazza – egybetűs jelöléssel.
#   (A fehérjelánc legfeljebb 1000 aminosavat tartalmaz.)
#   Határozza meg a fehérje összegképletét (azaz a C, H, O, N és S számát)!
#   A meghatározásánál vegye figyelembe, hogy az aminosavak összekapcsolódása során minden kapcsolat létrejöttekor egy vízmolekula (H2O) lép ki!
#   Az összegképletet a képernyőre és az eredmeny.txt fájlba az alábbi formában írja ki:
#   Például: C 16321 H 34324 O 4234 N 8210 S 2231
print("\n4. feladat")
# bsa üres fehérje létrehozása, amelyet feltöltünk a résztvevő fehérjék adatai alapján 
bsa = {
    'rov' : 'bsa',
    'betu' : '-',
    'C' : 0,
    'H' : 0,
    'O' : 0,
    'N' : 0,
    'S' : 0,
}

bsa_seq = ""  # 5. feladathoz
with open("bsa.txt", "r") as fileBe:
    for f in fileBe:
        f_kod = f.strip()
        bsa_seq += f_kod    # 5. feladathoz
        feherje = f_dict[f_kod] 
        bsa['C'] += feherje['C']
        bsa['H'] += feherje['H'] - 2 # H2O kilépés miatt
        bsa['O'] += feherje['O'] - 1 # H2O kilépés miatt
        bsa['N'] += feherje['N']
        bsa['S'] += feherje['S']
    # eggyel több H2O-t vontunk ki
    bsa['H'] += 2 
    bsa['O'] += 1 
print(f"C {bsa['C']} H {bsa['H']} O {bsa['O']} N {bsa['N']} S {bsa['S']}")

# hozzáfűzésre nyitjuk meg a kimeneti állományt
with open("eredmeny_dict.txt", "a") as fileKi:
    fileKi.write(f"C {bsa['C']} H {bsa['H']} O {bsa['O']} N {bsa['N']} S {bsa['S']}\n")
print("Adatok hozzáírva az 'eredmeny_dict.txt' állományhoz.")


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
