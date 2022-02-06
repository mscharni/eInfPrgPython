### Emelt Informatika Érettségi - 2006 Február - Telefonszámla

class Hivas():
    def __init__(self, line1, line2):
        self.ido = line1.strip()                # hívás tól-ig eredeti formában
        self.kora = int(self.ido.split(" ")[0]) # hívás kezdetének órája
        self.perc = idotartam(self.ido)         # hívás időtartama percben
        self.tszam = line2.strip()              # telefonszám
        self.tkor = self.tszam[0:2]             # körzetszám
        self.ttip = 0 if self.tkor in mobilkorzet else 1  # 0 = Mobilszám | 1 = egyéb szám
        
        
def idotartam(ido):
    datas = ido.split(" ")
    o1 = int(datas[0])
    p1 = int(datas[1])
    m1 = int(datas[2])
    o2 = int(datas[3])
    p2 = int(datas[4])
    m2 = int(datas[5])
    tartam = 1 + ((o2*60*60+p2*60+m2) - (o1*60*60+p1*60+m1)) // 60
    return tartam

mobilkorzet = ["39", "41", "71"]
hivasok = []

# 1. Kérjen be a felhasználótól egy telefonszámot!
# Állapítsa meg a program segítségével, hogy a telefonszám mobil-e vagy sem! A megállapítást írja ki a képernyőre!
print("\n1. feladat")

szam = input("Telefonszám = ")
if szam[0:2] in mobilkorzet:
    print(f"A {szam} mobil telefonszám")
else:
    print(f"A {szam} nem mobil telefonszám")

# 2. Kérjen be továbbá egy hívás kezdeti és hívás vége időpontot óra perc másodperc formában!
#   A két időpont alapján határozza meg, hogy a számlázás szempontjából hány perces a beszélgetés! A kiszámított időtartamot írja ki a képernyőre!
print("\n2. feladat")
ido = input("Hívás kezdete és vége 'oo pp mm oo pp mm' formában = ")
print(f"A beszélgetés {idotartam(ido)} perces volt a számlázás szempontjából.")

# 3. Állapítsa meg a hivasok.txt fájlban lévő hívások időpontja alapján, hogy hány számlázott percet telefonált a felhasználó hívásonként!
#   A kiszámított számlázott perceket írja ki a percek.txt fájlba a következő formában!
#   perc telefonszám
print("\n3. feladat")
with open("hivasok.txt", "r") as fileBe:
    while True:
        line1 = fileBe.readline()   # időadat
        if line1 != "":
            line2 = fileBe.readline()   # telefonszám
            hivas = Hivas(line1, line2)
            hivasok.append(hivas)
        else:
            break
print("Adatok beolvasva a 'hivasok.txt' állományból.")
with open("percek.txt", "w") as fileKi:
    for hivas in hivasok:
        fileKi.write(f"{hivas.perc} {hivas.tszam}\n")
print("Adatok kiírva a 'percek.txt' állományba.")        

# 4. Állapítsa meg a hivasok.txt fájl adatai alapján, hogy hány hívás volt csúcsidőben és csúcsidőn kívül! Az eredményt jelenítse meg a képernyőn!
print("\n4. feladat")
csucs_db = 0
ossz_db = len(hivasok)
for hivas in hivasok:
    # ha csúcsidőbe esik a kezdés (órája)
    if 7 <= hivas.kora  and hivas.kora < 18:
        csucs_db += 1
print(f"{csucs_db} hivas volt csúcsidőben és {ossz_db-csucs_db} csúcsidőn kívül.")

# 5. A hivasok.txt fájlban lévő időpontok alapján határozza meg, hogy hány percet beszélt a felhasználó mobil számmal és hány percet vezetékessel!
# Az eredményt jelenítse meg a képernyőn!
print("\n5. feladat")
perc_ossz = [0,0]   # 0. mobil, 1. egyéb
for hivas in hivasok:
    perc_ossz[hivas.ttip] += hivas.perc
print(f"{perc_ossz[0]} percet beszélt mobil számmal és {perc_ossz[1]} percet vezetékes számmal.")


# 6. Összesítse a hivasok.txt fájl adatai alapján, mennyit kell fizetnie a felhasználónak a csúcsdíjas hívásokért! Az eredményt a képernyőn jelenítse meg!
print("\n6. feladat")
csucs_dijak = [69.175, 30]  # 0.= mobil percdíj, 1.= vezetékes percdíj
ossz_csucs_dij = 0
for hivas in hivasok:
    # ha csúcsidőbe esik a kezdés (órája)
    if 7 <= hivas.kora  and hivas.kora < 18:
        ossz_csucs_dij += hivas.perc * csucs_dijak[hivas.ttip]
print(f"{ossz_csucs_dij:.0f} Forintot kell fizetnie a felhasználónak a csúcsdíjas hívásokért.")
