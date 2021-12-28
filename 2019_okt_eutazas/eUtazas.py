class oUtas:
    def __init__(self,s):
        self.megallo = int(s[0])
        self.datumIdo = s[1]
        self.datum = s[1][0:8]
        self.ido = s[1][9:4]
        self.kID = s[2]
        self.tipus = s[3]
        if self.tipus == "JGY":
            self.jE = True
            self.jDb = int(s[4])
            self.erv = True if self.jDb > 0 else False
        else :    
            self.jE = False
            self.eDatum = s[4]
            self.erv = True if self.datum <= self.eDatum else False

utasok=[]

# 1. feladat
fileBe = open("utasadat.txt", "r")
for sor in fileBe.readlines():
    utas = oUtas(sor.strip().split(" "))
    utasok.append(utas)
fileBe.close()

# 2. feladat
print("2. feladat")
print("A buszra {} utas akart felszállni".format(len(utasok)))

# 3. feladat
print("3. feladat")
nemErvDb = 0
for utas in utasok:
    if utas.erv != True:
        nemErvDb += 1
print("A buszra {} utas nem szállhatott fel".format(nemErvDb))

# 4. feladat
print("4. feladat")
maxUtas = 0
maxMegallo = 0
aktMegallo = utasok[0].megallo
aktUtas =0
for utas in utasok:
    if utas.megallo == aktMegallo:
        aktUtas += 1
    else:
        if aktUtas > maxUtas:
            maxUtas = aktUtas
            maxMegallo = aktMegallo
        aktUtas = 1
        aktMegallo = utas.megallo
print("A legtöbb utas ({}) fő a {}. megállóban próbált felszállni".format(maxUtas, maxMegallo))

# 5. feladat
print("5. feladat")
kedvDb = 0
ingyDb = 0
for utas in utasok:
    # nem jegy
    if utas.erv == True and utas.jE == False:
        if "TAB NYB".find(utas.tipus) > -1:
            kedvDb += 1
        if "NYP RVS GYK".find(utas.tipus) > -1:
            ingyDb += 1
print("Ingyenesen utazók száma: {} fő".format(ingyDb))
print("A kedvezményesen utazók száma: {} fő".format(kedvDb))

# 6. feladat
def napokszama(e1, h1, n1, e2, h2, n2):
	h1 = (h1 + 9) % 12
	e1 = e1 - h1 // 10
	d1= 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
	h2 = (h2 + 9) % 12
	e2 = e2 - h2 // 10
	d2= 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
	return d2-d1

# 7. feladat
fileKi = open("figyelmeztetes.txt", "w")
for utas in utasok:
    if utas.erv == True and utas.jE == False:
        e1 = int(utas.datum[0:4])
        h1 = int(utas.datum[4:6])
        n1 = int(utas.datum[6:8])
        e2 = int(utas.eDatum[0:4])
        h2 = int(utas.eDatum[4:6])
        n2 = int(utas.eDatum[6:8])
        if napokszama(e1, h1, n1, e2, h2, n2) <=3:
            fileKi.writelines("{} {}-{}-{}\n".format(utas.kID, e2,h2,n2))
fileKi.flush()
fileKi.close()