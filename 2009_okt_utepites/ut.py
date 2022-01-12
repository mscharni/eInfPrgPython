### Emelt Informatika Érettségi - 2009 Október - Útépítés

class Jarmu():
    def __init__(self, idx, line):
        global tav
        datas = line.strip().split(" ")
        self.azo = idx
        self.be_ora = int(datas[0])
        self.be_perc = int(datas[1])
        self.be_mperc = int(datas[2])
        self.be_ido = 60 * 60 * self.be_ora + 60 * self.be_perc + self.be_mperc     # belépési idő éjféltől számított másodpercben
        self.at_mp = int(datas[3])
        self.sebesseg = round(tav / self.at_mp,1)
        self.honnankod = datas[4].upper()
        if self.honnankod == "A":
            self.honnan = "Alsó"
            self.hova = "Felső"
        else:
            self.honnan = "Felső"
            self.hova = "Alsó"

tav = 1000      # a két város közötti távolság méterben
jarmuvek = []   # járművek adatait tartalmazó lista
sebessegek = [] # a különböző sebességeket tartalmazó segédlista
sebesek = []    # a különböző sebességű autók adatait tartalmazó lista

idx = 0
# 1. Olvassa be a forgalom.txt állományban talált adatokat, s azok felhasználásával oldja meg a következő feladatokat!
#   Ha az állományt nem tudja beolvasni, akkor az első 10 sorának adatait jegyezze be a programba és dolgozzon azzal!
print("\n1.feladat")
with open("forgalom.txt", "r") as fileBe:
    # az első sorban a bejegyzések száma szerepel
    line = fileBe.readline()
    for line in fileBe:
        idx += 1
        jarmu = Jarmu(idx, line)
        jarmuvek.append(jarmu)
print("Adatok beolvasva a 'forgalom.txt' állományból.")

# 2. Írja ki a képernyőre, hogy az n-edikként belépő jármű melyik város felé haladt!
#   Ehhez kérje be a felhasználótól az n értékét!
print("\n2.feladat")
n = int(input("Jármű sorszáma = "))
print(f"A {n}. jármű célja: {jarmuvek[n-1].hova}város")     # nullától indul az index

# 3. Írja a képernyőre, hogy a Felső város irányába tartó utolsó két jármű hány másodperc különbséggel érte el az útszakasz kezdetét!
print("\n3.feladat")
# utolsó megkeresése
utso_1_idx = len(jarmuvek)-1
while jarmuvek[utso_1_idx].hova != "Felső":
    utso_1_idx -= 1
# utolsó előtti megkeresése
utso_2_idx = utso_1_idx -1
while jarmuvek[utso_2_idx].hova != "Felső":
    utso_2_idx -= 1
print(f"Az utolsó két Felső város irányába tartó autó {jarmuvek[utso_1_idx].be_ido - jarmuvek[utso_2_idx].be_ido} másodperc különbséggel érték el az útszakasz kezdetét")

# 4. Határozza meg óránként és irányonként, hogy hány jármű érte el a szakaszt!
#   Soronként egy-egy óra adatait írja a képernyőre!
#   Az első érték az órát, a második érték az Alsó, a harmadik a Felső város felől érkező járművek számát jelentse!
#   A kiírásban csak azokat az órákat jelenítse meg, amelyekben volt forgalom valamely irányban!
print("\n4.feladat")
# első és utolsó jármű belépési órája
ora_1 = jarmuvek[0].be_ora
ora_2 = jarmuvek[-1].be_ora
# Alsóvárosból induló járművek összegzései
orak_A = [0 for i in range(0, ora_2+1)] # az ora_1 előtti indexeket nem használjuk ki
# Felsővárosból induló járművek összegzései
orak_F = [0 for i in range(0, ora_2+1)] # az ora_1 előtti indexeket nem használjuk ki
for jarmu in jarmuvek:
    # a belépsi óra számának megfelelő indexű listelemet növeljük eggyel
    if jarmu.honnankod == "A":
        orak_A[jarmu.be_ora] += 1
    else:
        orak_F[jarmu.be_ora] += 1
print(f"Óra Alsó Felső")
for ora in range(ora_1, ora_2+1):
    if orak_A[ora] + orak_F[ora] > 0:   # legalább az egyik irányból volt forgalom az adott órában
        print(f"{ora:3} {orak_A[ora]:3} {orak_F[ora]:3}")

# 5. A belépéskor mért értékek alapján határozza meg a 10 leggyorsabb járművet!
#   Írassa ki a képernyőre ezek belépési idejét, a várost (Alsó, illetve Felső), amely felől érkezett, és m/s egységben kifejezett sebességét egy tizedes pontossággal, sebességük szerinti csökkenő sorrendben!
#   Ha több azonos sebességű járművet talál, bármelyiket megjelenítheti.
#   Soronként egy jármű adatait jelenítse meg, és az egyes adatokat szóközzel tagolja!
#   (A feladat megoldásakor figyeljen arra, hogy a következő feladatban az adatok eredeti sorrendjét még fel kell használni!)
print("\n5.feladat")
# végigmegyünk az összes járművön és kigyűjtjük a különböző sebességet és a hozzájuk kapcsolódó járművet
for jarmu in jarmuvek:
    if sebessegek.count(jarmu.sebesseg) == 0:    # még nem volt ilyen sebességű jármű
        sebessegek.append(jarmu.sebesseg)       # letároljuk a sebességet a segédtáblában
        sebesek.append(jarmu)                   # letároljuk a jármű adatait
# csökkenő sorrendben rendezzük a sebes járműveket
# rendező függvény
def sort_by_sebesseg(jarmu):
    return jarmu.sebesseg
sebesek.sort(key=sort_by_sebesseg, reverse=True)
# kiiratjuk az első tizet
print("{:>2} {:>4} {:>3} {:>4} {:>5} {:>6} {:>8}".format("N", "Idx", "Óra", "Perc", "MPerc", "Honnan", "Sebesseg"))
print("="*38)
for i in range(0,10):
    s = sebesek[i]
    print(f"{i+1:2} {s.azo:4} {s.be_ora:3} {s.be_perc:4} {s.be_mperc:5} {s.honnan:>6} {s.sebesseg:8}")


# 6. Írassa ki az also.txt állományba azokat az időpontokat, amikor az Alsó város felé tartók elhagyták a kérdéses útszakaszt!
#   Ha egy jármű utolér egy másikat, akkor a kilépésük időpontja a lassabb kilépési ideje legyen!
#   A fájl minden sorába egy-egy időpont kerüljön óra perc másodperc formában! A számokat pontosan egy szóköz válassza el egymástól!
print("\n6.feladat")
# segédfüggvény az időkezeléshez (óra perc másodperc alakra hozza a másodpercben éjféltől eltelt időt)
def get_ido(ido):
    ora = ido // (60*60)
    perc = (ido - (ora*60*60)) // 60
    mperc = ido - ora * 60 * 60 - perc * 60
    return f"{ora} {perc} {mperc}"

# a legutolsó távozási (kilépési) időpont
utso_ki_ido = 0
with open("also.txt", "w") as fileKi:
    for jarmu in jarmuvek:
        if jarmu.honnankod == "F":
            ki_ido = jarmu.be_ido + jarmu.at_mp         # az elvi kilépési idő a belépési idő + áthaladás másodpercben
            if ki_ido < utso_ki_ido:
                # utolérte az előző kocsit, ezért a kilépési idejét az utolsó kilépési időre állítjuk
                ki_ido = utso_ki_ido
            fileKi.write(get_ido(ki_ido)+"\n")
            utso_ki_ido = ki_ido                        # frissítjük az utolsó kilépési időt
print("Adatok kiírva a 'also.txt' állományba")
