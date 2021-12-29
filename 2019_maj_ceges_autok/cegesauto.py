class Adat :
    def __init__(self, s):
        self.nap = int(s[0])
        self.oraPerc = s[1]
        self.rendszam = s[2]
        self.ri = int(s[2][5:6]) # rendszám utolsó karaktere az auto sorszáma: 0..9
        self.dolgozo = s[3]
        self.km = int(s[4])
        if (int(s[5]) == 0):
            self.ki =  True 
        else:
            self.ki =  False

adatok = []

class Auto:
    def __init__(self, s):
        self.ri = int(s[5:6]) # rendszám utolsó karaktere az auto sorszáma: 0..9
        self.rendszam = s
        self.kmStart = 0
        self.kmEnd = 0
        self.kmKi = 0
        self.kmBe = 0
autok = []
# legeneráljuk a 10 cégautó (üres) adatlapját
for i in range(0,10):
    auto = Auto("CEG30" + str(i))
    autok.append(auto)


# 1. feladat: Olvassa be és tárolja el az autok.txt fájl tartalmát!
print("\n1. feladat")
with open("autok.txt","r") as fileBe:
    for sor in fileBe.readlines():
        adat = Adat(sor.split(" "))
        adatok.append(adat)
print("Adatok beolvasva az 'autok.txt' állományból.")

# 2. feladat: Adja meg, hogy melyik autót vitték el utoljára a parkolóból!
#   Az eredményt a mintának megfelelően írja a képernyőre!
print("\n2. feladat")
i = len(adatok) -1
while(adatok[i].ki == False):
    i -= 1
print(f"{adatok[i].nap}. nap rendszám: {adatok[i].rendszam}")

# 3. feladat: Kérjen be egy napot és írja ki a képernyőre a minta szerint, hogy mely autókat vitték ki és hozták vissza az adott napon!
print("\n3. feladat")
napBe = int(input("Nap: "))
i = 0
print(f"Forgalom a(z) {napBe}. napon:")
# megkeressük az első napot
while(adatok[i].nap <= napBe):
    # kiírjuk az első naphoz tartozó adatokat (ha van ilyen nap)
    if (adatok[i].nap == napBe):
        if (adatok[i].ki == True):
            kibe = "ki"
        else:
            kibe = "be"
        print(f"{adatok[i].oraPerc} {adatok[i].rendszam} {adatok[i].dolgozo} {kibe}")
    i += 1

# 4. feladat: Adja meg, hogy hány autó nem volt bent a hónap végén a parkolóban!
print("\n4. feladat")
kibeC = 0
for adat in adatok:
    if (adat.ki):
        kibeC += 1
    else:
        kibeC -= 1
print(f"A hónap végén {kibeC} autót nem hoztak vissza.")

# 5. feladat: Készítsen statisztikát, és írja ki a képernyőre mind a 10 autó esetén az ebben a hónapban megtett távolságot kilométerben!
#   A hónap végén még kint lévő autók esetén az utolsó rögzített kilométerállással számoljon!
#   A kiírásban az autók sorrendje tetszőleges lehet.
print("\n5. feladat")
for adat in adatok:
    ## első és utolsó km állás letárolása az autó adatlapjában
    if (autok[adat.ri].kmStart == 0):
        autok[adat.ri].kmStart = adat.km
    else:
        autok[adat.ri].kmEnd = adat.km
# autók adatlapjának kiiratása
for auto in autok:
    print(f"{auto.rendszam} {auto.kmEnd - auto.kmStart} km")

# 6. feladat: Határozza meg, melyik személy volt az, aki az autó egy elvitele alatt a leghosszabb távolságot tette meg!
#   A személy azonosítóját és a megtett kilométert a minta szerint írja a képernyőre!
#   (Több legnagyobb érték esetén bármelyiket kiírhatja.)
print("\n6. feladat")
kmMax = 0
kmMaxDolgozo = 0
for adat in adatok:
    if (adat.ki):
        autok[adat.ri].kmKi = adat.km
    else:
        autok[adat.ri].kmBe = adat.km
        #  megnézzük, hogy nagyobb távolságot tett-e meg, mint az eddigi max távolság
        tav = autok[adat.ri].kmBe - autok[adat.ri].kmKi
        if ( tav > kmMax):
            kmMax = tav
            kmMaxDolgozo = adat.dolgozo
print(f"Leghosszabb út: {kmMax} km, személy: {kmMaxDolgozo}")

# 7. feladat: Az autók esetén egy havi menetlevelet kell készíteni!
#   Kérjen be a felhasználótól egy rendszámot!
#   Készítsen egy X_menetlevel.txt állományt, amelybe elkészíti az adott rendszámú autó menetlevelét!
#   (Az X helyére az autó rendszáma kerüljön!)
#   A fájlba soronként tabulátorral elválasztva a személy azonosítóját, a kivitel időpontját (nap. óra:perc), a kilométerszámláló állását, a visszahozatal időpontját (nap. óra:perc), és a kilométerszámláló állását írja a minta szerint!
#   (A tabulátor karakter ASCII-kódja: 9.)
print("\n7. feladat")
rszBe = input("Rendszám: ")
with open(rszBe + "_menetlevel.txt","w") as fileKi:
    for adat in adatok:
        if (adat.rendszam == rszBe):
            if (adat.ki):
                lastKi = True
                autoKi = adat
            else:
                lastKi = False
                autoBe = adat
                fileKi.writelines("{}\t{}.\t{}\t{} km\t{}.\t{}\t{} km\n".format(autoKi.dolgozo, autoKi.nap, autoKi.oraPerc, autoKi.km, autoBe.nap, autoBe.oraPerc, autoBe.km))
    if (lastKi):
        fileKi.writelines("{}\t{}.\t{}\t{} km\n".format(autoKi.dolgozo, autoKi.nap, autoKi.oraPerc, autoKi.km))
print("Menetlevél kész.")