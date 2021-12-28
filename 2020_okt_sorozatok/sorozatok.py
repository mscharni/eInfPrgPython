import datetime

# struktúra
epizod = {}

# lista
epizodok = []

# feladatokhoz
epizodCount = 0
adasbaCount = 0
lattaCount = 0
lattaSum = 0

# 1. feladat
print("\n1. feladat")
fileName = 'lista.txt'
fileBe =  open(fileName, 'r')
while True:
    # a sor-ban mindig a dátum-adat szerepel string formájában
    sor = fileBe.readline().strip()
    # van még mit beolvasni a file-ból
    if sor:
        if (sor != "NI"):
            datumS = str(sor).split(".")
        else:
            datumS = ["2222","12", "31"]
        cim = str(fileBe.readline().strip())
        resz = str(fileBe.readline().strip())
        hossz = int(fileBe.readline().strip())
        latta = int(fileBe.readline().strip())
        # 2-es-hez
        if(sor != "NI"):
            adasbaCount += 1

        # 3-ashoz és 4-eshez
        if (latta == 1):
            lattaCount += 1
            lattaSum += hossz
        epizod = {
            'datum' : datetime.date(int(datumS[0]),int(datumS[1]),int(datumS[2]),),
            'cim': cim,
            'resz': resz,
            'hossz': hossz,
            'latta': latta
        }
        epizodok.append(epizod)
        epizodCount +=1
    else:
        break 
fileBe.close()
print("Adatok beolvasva a '{0}' file-ból!".format(fileName))

### 2. feladat ###
print("\n2. feladat")
print("A listában {0} db vetítési dátummal rendelkező epizód van.".format(adasbaCount))

### 3. feladat ###
print("\n3. feladat")
print("A listában lévő epizódok {0:.2f}%-át látta.".format(100*lattaCount/epizodCount))

### 4. feladat ###
print("\n4. feladat")
nap = int(lattaSum / (24*60))
ora = int((lattaSum - nap*24*60) / 60)
perc = lattaSum - nap*24*60 - ora*60
print("Sorozatnézéssel {0} napot {1} órát és {2} percet töltött.".format(nap, ora, perc))

### 5. feladat ###
print("\n5. feladat")

datumBeS = input("Adjon meg egy dátumot! Dátum = ").strip()
# datumBeS= "2017.10.18"
datumBeS = datumBeS.split('.')
datumBe = datetime.date(int(datumBeS[0]),int(datumBeS[1]),int(datumBeS[2]))    
lattaCount = 0
for epizod in epizodok:
    # adott dátum előtti
    if (epizod['datum'] <= datumBe):
        # nem látta
        if (epizod['latta'] == 0):
            print(epizod['resz'], '\t', epizod['cim'])
            lattaCount += 1
if (lattaCount == 0):
    print("{0} előtt minden epizódot látott!".format(datumBe))

### 6. feladat ###
print("\n6. feladat")

def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3 :
        ev = ev -1
    return napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho-1] + nap) % 7]


### 7. feladat ###
print("\n7. feladat")
napBe = input("Adja meg a hét egy napját (például cs)! Nap = ").strip()
# napBe = "cs"

adasban = False
lastCim = ""
for epizod in epizodok:
    lastDatum = epizod['datum']
    # ha az adott napra esik
    if (hetnapja(lastDatum.year, lastDatum.month,lastDatum.day) == napBe):
        # és még nem szerepelt
        if (epizod['cim'] != lastCim):
            print(epizod['resz'], '\t', epizod['cim'])
            adasban = True
            lastCim = epizod['cim']
if (adasban == False):
    print("Az adott napon nem kerül adásba sorozat.")

### 8. feladat ###
print("\n8. feladat")
fileName = 'summa.txt'
fileKi = open(fileName, 'w')
firstEpizod = epizodok[0]
lastCim = firstEpizod['cim']
lastSum = 0
lastCount = 0
for epizod in epizodok:
    if (epizod['cim'] == lastCim):
        lastSum += epizod['hossz']
        lastCount +=1
    else:
        fileKi.writelines("{0} {1} {2}\n".format(lastCim, lastSum, lastCount))
        lastCim = epizod['cim']
        lastSum = epizod['hossz']
        lastCount = 1

fileKi.close()
# print("adatok kiírva a '{0}' file-ba!".format(fileName))


