### Emelt Informatika Érettségi - 2010 Május - Helyjegy
class Jegy():
    def __init__(self, idx, line):
        global ossz_bevetel
        global megallok
        datas = line.strip().split(" ")
        self.azo = idx
        self.ules = int(datas[0])
        self.fel = int(datas[1])
        self.le = int(datas[2])
        self.tav = self.le - self.fel       # megtett távolság
        self.tav10 = self.get_tav10()       # megkezedett 10km-ek száma
        self.dij = self.get_dij()           # fizetendő
        ossz_bevetel += self.dij            # az összbevétel növelése
        if megallok.count(self.fel) == 0:   # megállók kigyűjtése
            megallok.append(self.fel)

    def get_tav10(self):
        tiz_km = (self.tav) // 10
        if (self.tav) % 10 != 0:
            tiz_km += 1
        return tiz_km

    def get_dij(self):
        dij_ft = self.tav10 * ut_dij
        dij_tizes = 10*(dij_ft//10)
        dij_egyes = dij_ft - dij_tizes
        dij_otos = dij_tizes
        if dij_egyes <= 2:      # 0, 1, 2
            # lefele kerekítünk
            pass
        elif dij_egyes > 2  and dij_egyes < 8:   # 3, 4, 5, 6, 7
            # 5-re kerekítünk
            dij_otos += 5
        elif dij_egyes != 0:    # 8, 9
            # felfele kerekítünk
            dij_otos += 10
        return dij_otos

# az adatokat tartalmazó lista
jegyek = []
ossz_bevetel = 0
megallok = []

# 1. Olvassa be az eladott.txt állományban talált adatokat, s azok felhasználásával oldja meg a következő feladatokat!
#   Ha az állományt nem tudja beolvasni, az állomány első 10 sorának adatait jegyezze be a programba és dolgozzon azzal!
print("\n1. feladat")
with open("eladott.txt", "r") as fileBe:
    # első sorban lévő adatok beolvasása
    datas = fileBe.readline().strip().split(" ")
    jegy_db = int(datas[0])
    ut_hossz = int(datas[1])
    ut_dij = int(datas[2])
    idx = 1
    # többi sor beolvasása és eltárolása
    for line in fileBe:
        jegy = Jegy(idx, line)
        idx += 1
        jegyek.append(jegy)
print("Adatok beolvasva a 'eladott.txt' állományból.")

# 2. Adja meg a legutolsó jegyvásárló ülésének sorszámát és az általa beutazott távolságot!
print("\n2. feladat")
print(f"Legutolsó jegyvásárló - Ülés: {jegyek[-1].ules}, Táv: {jegyek[-1].tav}")

# 3. Listázza ki, kik utazták végig a teljes utat!
#   Az utasok sorszámát egy-egy szóközzel elválasztva írja a képernyőre!
print("\n3. feladat")
teljes_utazok = "Teljes utat megtettek sorszáma: "
for jegy in jegyek:
    if jegy.tav == ut_hossz:                    # akik megtették a teljes távot
        teljes_utazok += str(jegy.azo) + " "
print(f"{teljes_utazok[:-1]}")

# 4. Határozza meg, hogy a jegyekből mennyi bevétele származott a társaságnak!
print("\n4. feladat")
print(f"Összbevétel: {ossz_bevetel:,} Ft".replace(',', ' '))

# 5. Írja a képernyőre, hogy a busz végállomást megelőző utolsó megállásánál hányan szálltak fel és le!
print("\n5. feladat")
# megállók rendezése után az utolsó kell
megallok.sort()
fel_db = 0
le_db = 0
for jegy in jegyek:
    if jegy.fel == megallok[-1]:
        fel_db +=1
    if jegy.le == megallok[-1]:
        le_db +=1
print(f"Az utolsó köztes megállóban leszállók = {le_db} fő, felszállók = {fel_db} fő.")

# 6. Adja meg, hogy hány helyen állt meg a busz a kiinduló állomás és a célállomás között!
print("\n6. feladat")
print(f"Összesen {len(megallok)-1} köztes megálló van")     # a kezdőállomást nem kell beleszámolni

# 7. Készítsen „utaslistát” az út egy pontjáról!
#   A listában ülésenként tüntesse fel, hogy azt az adott pillanatban melyik utas foglalja el!
#   A pontot, azaz a kiindulási állomástól mért távolságot, a felhasználótól kérje be!
#   Ha a beolvasott helyen éppen megálló lett volna, akkor a felszálló utasokat vegye figyelembe, a leszállókat pedig hagyja figyelmen kívül!
#   Az eredményt az ülések sorszámának sorrendjében írja a kihol.txt állományba!
#   Az üres helyek esetén az „üres” szót jelenítse meg! Minden ülés külön sorba kerüljön!
print("\n7. feladat")
ulesek = ["üres" for i in range(0, 49)]             # a nullás sorszámút nem használjuk
tav = int(input("Adja meg a keresett távolságot = "))
for jegy in jegyek:
    if jegy.fel <= tav and tav < jegy.le:
        ulesek[jegy.ules] = f"{jegy.azo:3}. utas"

with open("kihol.txt", "w", encoding="UTF-8") as fileKi:
    for i in range(1,49):
        fileKi.writelines(f"{i:2}. ülés: {ulesek[i]}\n")
print("Adatok kiírva a 'kihol.txt' állományba.")
