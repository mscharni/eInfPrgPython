### Emelt Informatika Érettségi - 2011 Október - Pitypang

class Foglalas():
    def __init__(self, line):
        datas   = line.strip().split()
        self.sorsz   = int(datas[0])            # a foglalás sorszáma,
        self.szoba   = int(datas[1])            # a szoba száma (1–27),
        self.erknap  = int(datas[2])            # az érkezés napjának sorszáma,
        self.tavnap  = int(datas[3])            # a távozás napjának sorszáma,
        self.fodb    = int(datas[4])            # a vendégek száma,
        self.reggeli = int(datas[5])            # kérnek-e reggelit (1=igen vagy 0=nem),
        self.nevazo  = datas[6]                 # a foglalást végző vendég nevéből képzett azonosítója (maximum 25 karakter).
        self.napdb   = self.tavnap-self.erknap  # eltöltött éjszakák száma
        self.szobaar = self.get_szobaar()       # érkezési nap alapján a szobaár meghatározása
        self.szamla  = self.get_szamla()        # fizetendő összeg kiszámolása
        self.set_honap_stat()                   # havi statisztikához adatok feldolgozása

    def get_szobaar(self):
        if self.erknap < 121:
            return 9000
        elif self.erknap < 244:
            return 10000
        else:
            return 8000

    def get_szamla(self):
        osszeg = self.napdb * self.szobaar                  # alap szobaár
        if self.reggeli == 1:
            osszeg += self.napdb * self.fodb * 1100         # reggeli
        if self.fodb > 2:
            osszeg += self.napdb * (self.fodb-2) * 2000     # pótágy
        return osszeg

    # az év elejétől eltelt napok száma alapján visszaadja a hónap sorszámát
    def get_honap_idx(self,nap):
        i = 1
        while nap >= honap[i]:
            i +=1
        i -= 1 # a megelőző hónap kell
        return i

    # a statisztikai adatok feltöltése
    def set_honap_stat(self):
        for nap in range(self.erknap, self.tavnap):
            honap_idx = self.get_honap_idx(nap)
            honap_stat[honap_idx] += self.fodb

honap = [0 for i in range(0,14)]    # a nulladik indexűt nem használjuk, a 13. indexű segédhónap
honap_stat = [0 for i in range(0,14)]    # a nulladik indexűt nem használjuk, a 13. indexű segédhónap
foglalasok = []

# 1. feladat: Olvassa be az pitypang.txt állományban található maximum 1 000 foglalás adatát, s annak felhasználásával oldja meg a következő feladatokat!
print("\n1. feladat")
#   honap adatok betöltése
with open("honapok.txt") as fileBe:
    for i in range(1, 13):
        honap_nev = fileBe.readline().strip()
        honap_napok = int(fileBe.readline().strip())
        honap_start = int(fileBe.readline().strip())
        honap[i] = honap_start
# a legutolsó hónap fiktív, hogy az előttiként megtaláljuk az utolsót
honap[13] = 366

#   foglalasi adatok betöltése
with open("pitypang.txt") as fileBe:
    fileBe.readline()         # az első sor a foglalások számát tartalmazza (nem használjuk)
    for line in fileBe:
        foglalasok.append(Foglalas(line))
print("adatok betöltve a 'pitypang.txt' állományból")

# 2. feladat: Jelenítse meg a képernyőn a leghosszabb szállodai tartózkodást!
#   Csak az időtartamot vegye figyelembe, azaz nem számít, hogy hány vendég lakott az adott szobában!
#   Az esetlegesen azonos hosszúságú tartózkodások közül bármelyiket kiválaszthatja.
#   Az eredményt ebben a formában írja a képernyőre:
#       Név (érkezési_nap_sorszáma) – eltöltött_éjszakák_száma
#       például: Nagy_Bertalan (105) – 16
print("\n2.feladat")
max_nap_idx = 0
for i in range(0, len(foglalasok)):
    if foglalasok[i].napdb > foglalasok[max_nap_idx].napdb:
        max_nap_idx = i
max_fog = foglalasok[max_nap_idx]
print(f"{max_fog.nevazo} ({max_fog.erknap}) – {max_fog.napdb}")

# 3. feladat: Számítsa ki, hogy az egyes foglalások után mennyit kell fizetnie az egyes vendégeknek!
#   A foglalás sorszámát és a kiszámított értékeket kettősponttal elválasztva írja ki a bevetel.txt fájlba!
print("\n3.feladat")
with open("bevetel.txt", "w") as fileKi:
    for foglalas in foglalasok:
        fileKi.write(f"{foglalas.sorsz}:{foglalas.szamla}\n")
print("Adatok kiírva a 'bevetel.txt' állományba")

# 4. feladat: Készítsen statisztikát az egyes hónapokban eltöltött vendégéjszakákról!
#   Egy vendégéjszakának egy fő egy eltöltött éjszakája számít.
#   A példában szereplő Tóth család áprilisban 3, májusban pedig 9 vendégéjszakát töltött a szállodában.
#   Írassa ki a havi vendégéjszakák számát a képernyőre az alábbi formában:
#       hónap_sorszáma: x vendégéj
#       például: 8: 1059 vendégéj
for honap_idx in range(1,13):
    print(f"{honap_idx}: {honap_stat[honap_idx]} vendégéj")

# 5. feladat: Kérje be a felhasználótól egy új foglalás kezdő dátumához tartozó nap sorszámát és az eltöltendő éjszakák számát!
#   Határozza meg, hogy hány szoba szabad a megadott időszak teljes időtartamában! A választ írassa ki a képernyőre!
nap_erk = int(input("Foglalás kezdő dátumához tartozó nap sorszáma = "))
nap_db = int(input("Eltöltendő éjszakák száma = "))
nap_tav = nap_erk + nap_db
# ha az új foglalás bármely napján foglalt egy szoba, akkor az már nem szabad (nem jó)
szabad_szobak = [True for i in range(0,28)]   # a nulladik indexűt nem használjuk. Kezdetben mindegyik szabad (True)
for foglalas in foglalasok:
    if (foglalas.erknap > nap_tav) or (foglalas.tavnap < nap_erk):
        # kívül esik a vizsgált időszakon
        pass
    else:
        # valamilyen átfedés van, azaz az a szoba már nem lesz jó
        szabad_szobak[foglalas.szoba] = False
szabad_count = szabad_szobak.count(True) - 1    # a nullás sorszámű True-t levonjuk
szabadok = "  "
for i in range(1,28):
    if szabad_szobak[i]:
        szabadok += str(i) +", "
szabadok = szabadok[:-2]
print(f"{szabad_count} szoba szabad a megadott időszak teljes időtartamában: {szabadok}!")



