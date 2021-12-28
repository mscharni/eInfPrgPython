class oAdat :
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

class oAuto:
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
    auto = oAuto("CEG30"+ str(i))
    autok.append(auto)


# 1. feladat
fileBe = open("autok.txt","r")
for sor in fileBe.readlines():
    adat = oAdat(sor.split(" "))
    adatok.append(adat)
fileBe.close()

# 2. feladat
print("2. feladat")
i = len(adatok) -1
while(adatok[i].ki == False):
    i -= 1
print("{}. nap rendszám: {}".format(adatok[i].nap, adatok[i].rendszam))

# 3. feladat
print("3. feladat")
napBe = int(input("Nap: "))
i = 0
print("Forgalom a(z) {}. napon:".format(napBe))
while(adatok[i].nap <= napBe):
    if (adatok[i].nap == napBe):
        if (adatok[i].ki == True):
            kibe = "ki"
        else:
            kibe = "be"
        print("{} {} {} {}".format(adatok[i].oraPerc, adatok[i].rendszam, adatok[i].dolgozo, kibe))
    i += 1

# 4. feladat
print("4. feladat")
kibeC = 0
for adat in adatok:
    if (adat.ki):
        kibeC += 1
    else:
        kibeC -= 1
print("A hónap végén {} autót nem hoztak vissza.".format(kibeC))

# 5. feladat
print("5. feladat")
for adat in adatok:
    ## első és utolsó km állás letárolása az autó adatlapjában
    if (autok[adat.ri].kmStart == 0):
        autok[adat.ri].kmStart = adat.km
    else:
        autok[adat.ri].kmEnd = adat.km
# autók adatlapjának kiiratása
for auto in autok:
    print("{} {} km".format(auto.rendszam,(auto.kmEnd - auto.kmStart)))

# 6. feladat
print("6. feladat")
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
print("Leghosszabb út: {} km, személy: {}".format(kmMax, kmMaxDolgozo))

# 7. feladat
print("7. feladat")
rszBe = input("Rendszám: ")
fileKi = open(rszBe + "_menetlevel.txt","w")
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
fileKi.close()
print("Menetlevél kész.")