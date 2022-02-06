### Emelt Informatika Érettségi - 2020 Május - Meteorológiai jelentés

# adatok
orak = ["01", "07", "13", "19"] # azon órák felsorolva, amelyket számolni kell

class Tavirat:
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

class Telep:
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

# 1. feladat: Olvassa be és tárolja el a tavirathu13.txt állomány adatait!
print("\n1. feladat")
with open("tavirathu13.txt", "r") as fileBe:
    for sor in fileBe:
        adatok = sor.split(" ")
        _hely = adatok[0].strip()
        _ido = adatok[1].strip()
        _szel = adatok[2].strip()
        _ho = int(adatok[3].strip())
        # táviratok feldolgozása
        tavirat = Tavirat(_hely, _ido, _szel, _ho)
        taviratok.append(tavirat)
        # telepek feldolgozása
        # megkeressük, hogy van-e már ilyen nevű telep
        ujTelep = True
        for telep in telepek:
            if telep.hely == _hely:
                telep.update(_ido, _szel, _ho)
                ujTelep = False
        if ujTelep:
            telep = Telep(_hely, _ido, _szel, _ho)
            telepek.append(telep)
print("Adatok beolvasva a 'tavirathu13.txt' állományból")

# 2. feladat: Kérje be a felhasználótól egy város kódját! Adja meg, hogy az adott városból mikor érkezett
# az utolsó mérési adat! A kiírásban az időpontot óó:pp formátumban jelenítse meg!
print("\n2. feladat")
varosBe = input("Adja meg egy település kódját! Település: ").strip()
i = len(taviratok)-1
while taviratok[i].hely != varosBe:
    i -= 1
print(f"Az utolsó mérési adat a megadott településről {taviratok[i].getIdo()}-kor érkezett.")

# 3. feladat: Határozza meg, hogy a nap során mikor mérték a legalacsonyabb és a legmagasabb hőmérsékletet!
#   Jelenítse meg a méréshez kapcsolódó település nevét, az időpontot és a hőmérsékletet!
#   Amennyiben több legnagyobb vagy legkisebb érték van, akkor elég az egyiket kiírnia.
print("\n3. feladat")
minHo = taviratok[0]
maxHo = taviratok[0]
Idx = 0
for tavir in taviratok:
    if minHo.ho > tavir.ho:
        minHo = tavir
    if maxHo.ho < tavir.ho:
        maxHo = tavir
print(f"A legalacsonyabb hőmérséklet: {minHo.hely} {minHo.getIdo()} {minHo.ho} fok.")
print(f"A legmagasabb hőmérséklet: {maxHo.hely} {maxHo.getIdo()} {maxHo.ho} fok.")

# 4. feladat: Határozza meg, azokat a településeket és időpontokat, ahol és amikor a mérések idején szélcsend volt!
#   (A szélcsendet a táviratban 00000 kóddal jelölik.) Ha nem volt ilyen, akkor a „Nem volt szélcsend a mérések idején.” szöveget írja ki!
#   A kiírásnál a település kódját és az időpontot jelenítse meg.
print("\n4. feladat")
nincs = True
for tavir in taviratok:
    if tavir.szel == "00000":
        print(f"{tavir.hely} {tavir.getIdo()}")
        nincs = False
if nincs:
    print("Nem volt szélcsend a mérések idején.")        

# 5. feladat: Határozza meg a települések napi középhőmérsékleti adatát és a hőmérséklet-ingadozását!
#   A kiírásnál a település kódja szerepeljen a sor elején a minta szerint!
#   A kiírásnál csak a megoldott feladatrészre vonatkozó szöveget és értékeket írja ki!
#   a. A középhőmérséklet azon hőmérsékleti adatok átlaga, amikor a méréshez tartozó óra értéke 1., 7., 13., 19.
#       Ha egy településen a felsorolt órák valamelyikén nem volt mérés, akkor a kiírásnál az „NA” szót jelenítse meg!
#       Az adott órákhoz tartozó összes adat átlagaként határozza meg a középhőmérsékletet, azaz minden értéket azonos súllyal vegyen figyelembe!
#       A középhőmérsékletet egészre kerekítve jelenítse meg!
#   b. A hőmérséklet-ingadozás számításhoz az adott településen a napi legmagasabb és legalacsonyabb hőmérséklet különbségét kell kiszámítania!
#       (Feltételezheti, hogy minden település esetén volt legalább két mérési adat.)
print("\n5. feladat")
for telep in telepek:
    if telep.checkOrak():
        print(f"{telep.hely} Középhőmérséklet: {telep.getAtlagHo()}; Hőmérséklet-ingadozás: {telep.getHoIng()}")
    else:
        print(f"{telep.hely} NA; Hőmérséklet-ingadozás: {telep.getHoIng()}")

# 6. feladat: Hozzon létre településenként egy szöveges állományt, amely első sorában a település kódját tartalmazza!
#   A további sorokban a mérési időpontok és a hozzá tartozó szélerősségek jelenjenek meg!
#   A szélerősséget a minta szerint a számértéknek megfelelő számú kettőskereszttel (#) adja meg!
#   A fájlban az időpontokat és a szélerősséget megjelenítő kettőskereszteket szóközzel válassza el egymástól!
#   A fájl neve X.txt legyen, ahol az X helyére a település kódja kerüljön!
print("\n6. feladat")
for telep in telepek:
    fileKiNev = telep.hely + ".txt"
    with open(fileKiNev, 'w') as fileKi:
        fileKi.writelines(f"{fileKiNev}\n")
        for tavirat in taviratok:
            if telep.hely == tavirat.hely:
                fileKi.write(f"{tavirat.getIdo()} {tavirat.getSzelEro()}\n")
print("A fájlok elkészültek.")
