# adatok
orak = ["01", "07", "13", "19"] # azon órák felsorolva, amelyket számolni kell

class oTavirat:
    def __init__(self, hely, ido, szel, ho):
        self.hely = hely
        self.ido = ido
        self.szel = szel
        self.szelEro = int(szel[3:5])
        self.ho = ho
    def getIdo(self):
        return "{}:{}".format(self.ido[0:2],self.ido[2:4])
    def getSzelEro(self):
        hash = ""
        for i in range(self.szelEro):
	        hash += "#"
        return hash
taviratok = []

class oTelep:
    def __init__(self, hely, ido, szel, ho):
        self.hely = hely
        self.ido = ido
        self.szel = szel
        self.ho = ho
        self.idok = [False,False,False,False]
        self.hoSum = 0
        self.hoCount = 0
        self.hoMax = ho
        self.hoMin = ho
    def update(self,ido, szel, ho):
        oraVan = orak.count(ido[0:2])
        if oraVan > 0:
            oraI = orak.index(ido[0:2]) # hanyadik óra között
            self.idok[oraI] = True      # beállítjuk, hogy az adott órában volt mérés
            self.hoSum += ho            # összesítjük a hőt
            self.hoCount += 1           # növeljük az összesítetendő hő darabszámát
        if ho > self.hoMax:
            self.hoMax = ho
        if ho < self.hoMin:
            self.hoMin = ho
    def checkOrak(self):
        return (self.idok[0] & self.idok[1] & self.idok[2] & self.idok[3])
    def getAtlagHo(self):
        return (round(self.hoSum/self.hoCount))
    def getHoIng(self):
        return (self.hoMax - self.hoMin)

telepek = []

# 1. feladat
print("\n1. feladat")
fileBe = open("tavirathu13.txt", "r")
for sor in fileBe:
    adatok = sor.split(" ")
    _hely = adatok[0].strip()
    _ido = adatok[1].strip()
    _szel = adatok[2].strip()
    _ho = int(adatok[3].strip())
    # táviratok feldolgozása
    tavirat = oTavirat(_hely, _ido, _szel, _ho)
    taviratok.append(tavirat)
    # telepek feldolgozása
    # megkeressük, hogy van-e már ilyen nevű telep
    ujTelep = True
    for telep in telepek:
        if telep.hely == _hely:
            telep.update(_ido, _szel, _ho)
            ujTelep = False
    if ujTelep:
        telep = oTelep(_hely, _ido, _szel, _ho)
        telepek.append(telep)

# 2. feladat
print("\n2. feladat")
varosBe = input("Adja meg egy település kódját! Település: ").strip()
i = len(taviratok)-1
while taviratok[i].hely != varosBe:
    i -= 1
print("Az utolsó mérési adat a megadott településről {0}-kor érkezett.".format(taviratok[i].getIdo()))

# 3. feladat
print("\n3. feladat")
minHo = taviratok[0]
maxHo = taviratok[0]
Idx = 0
for tavir in taviratok:
    if minHo.ho > tavir.ho:
        minHo = tavir
    if maxHo.ho < tavir.ho:
        maxHo = tavir
print("A legalacsonyabb hőmérséklet: {0} {1} {2} fok.".format(minHo.hely, minHo.getIdo(), minHo.ho))
print("A legmagasabb hőmérséklet: {0} {1} {2} fok.".format(maxHo.hely, maxHo.getIdo(), maxHo.ho))

# 4. feladat
print("\n4. feladat")
nincs = True
for tavir in taviratok:
    if tavir.szel == "00000":
        print("{0} {1}".format(tavir.hely, tavir.getIdo()))
        nincs = False
if nincs:
    print("Nem volt szélcsend a mérések idején.")        

# 5. feladat
print("\n5. feladat")
for telep in telepek:
    if telep.checkOrak() :
        print("BP Középhőmérséklet: {0}; Hőmérséklet-ingadozás: {1}".format(telep.getAtlagHo(), telep.getHoIng()))
    else:
        print("{0} NA; Hőmérséklet-ingadozás: {1}".format(telep.hely, telep.getHoIng()))

# 6. feladat
print("\n6. feladat")
for telep in telepek:
    fileKiNev = telep.hely + ".txt"
    fileKi = open(fileKiNev, 'w')
    fileKi.writelines("{0}\n".format(fileKiNev))
    for tavirat in taviratok:
        if telep.hely == tavirat.hely:
            fileKi.writelines("{0} {1}\n".format(tavirat.getIdo(), tavirat.getSzelEro()))
    fileKi.close()
print("A fájlok elkészültek.")
