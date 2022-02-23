import math
# 1. Feladat adatok beolvasása
lines = []
with open("abpm.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
print(lines)

# 'Codes\tMessage' típusú adatok a végéről
joadatok =[]
adatok = []
kodok = {}

hatarIndex = lines.index("\n")
print(hatarIndex)
for i in range(hatarIndex+2, len(lines)):
    line = lines[i].strip().split("\t")
    # Codes	Message
    kodok[line[0]] = line[1]     

print(kodok)

# 'Time\tCode\tSystole\tDiastole\tPulse\n' típusú adatok az elejéről
for i in range(1, hatarIndex-1):
    line = lines[i].strip().split("\t")
    if len(line) == 5:
        # 5 --> jó adatok
        ido = line[0].split(":")
        adat = {
            'ora' : int(ido[0]),
            'perc' : int(ido[1]),
            'systole': int(line[2]),
            'diastole': int(line[3]),
            'pulse': int(line[4]),
            'message': kodok[line[1]]
            }
        joadatok.append(adat)
    else:
        # 2 --> hibás mérés
        pass

# print(joadatok)
# 2., Állapítsa meg a legmagasabb és legalacsonyabb Sys és Dia vérnyomás és pulzus értékeket.
minSysElem = joadatok[0]
maxSysElem = joadatok[0]
minDiaElem = joadatok[0]
maxDiaElem = joadatok[0]
minPulElem = joadatok[0]
maxPulElem = joadatok[0]

osszSys = 0
osszDia = 0
osszPul = 0
osszDb = len(joadatok)

for joadat in joadatok:
    if joadat['systole'] < minSysElem['systole']: minSysElem = joadat
    if joadat['systole'] > maxSysElem['systole']: maxSysElem = joadat
    if joadat['diastole'] < minDiaElem['diastole']: minDiaElem = joadat
    if joadat['diastole'] > maxDiaElem['diastole']: maxDiaElem = joadat
    if joadat['pulse'] < minPulElem['pulse']: minPulElem = joadat
    if joadat['pulse'] > maxPulElem['pulse']: maxPulElem = joadat
    osszSys += joadat['systole']
    osszDia += joadat['diastole']
    osszPul += joadat['pulse']

print(f"systole min: {minSysElem['systole']}")
print(f"systole max: {maxSysElem['systole']}")
print(f"diastole min: {minSysElem['diastole']}")
print(f"diastole max: {maxSysElem['diastole']}")
print(f"pulse min: {minPulElem['pulse']}")
print(f"pulse max: {maxPulElem['pulse']}")

# 3., Állapítsa meg a vérnyomás és pulzus értékek átlagát, móduszát, mediánját, terjedelmét, szórását.
print(f"systole terjedelem: {maxSysElem['systole']- minSysElem['systole']}")
print(f"diastole terjedelem: {maxDiaElem['diastole']- minDiaElem['diastole']}")
print(f"pulse terjedelem: {maxPulElem['pulse']- minPulElem['pulse']}")

SysAtlag = osszSys/osszDb
print(f"systole átlag: {SysAtlag:.2f}")
print(f"diastole átlag: {osszDia/osszDb:.2f}")
print(f"pulse átlag: {osszPul/osszDb:.2f}")

SysEltOssz = 0
gyakTabla = {}
for joadat in joadatok:
    joadat['SysElteres'] = (SysAtlag - joadat['systole'])**2
    SysEltOssz += joadat['SysElteres']
    if joadat['systole'] in gyakTabla:
        # már szerepel, ezért növelem eggyel
        gyakTabla[joadat['systole']] += 1
    else:
        # nincs benne, hozzáadom
        gyakTabla[joadat['systole']] = 1

SysSzoras = math.sqrt(SysEltOssz/osszDb)
print(f"systole szórás: {SysSzoras:.2f}")

# gyakTabla max értékének kiválasztása
maxErtek = max(gyakTabla.values())
maxok = []
print(gyakTabla)
for i in gyakTabla:
    if gyakTabla[i] == maxErtek:
        maxok.append(i)

if len(maxok) == 1 :
    print(f"Módusz: {maxok[0]}")
else:
    print(f"Nincs egyértelmű módusz, a legtöbbször előforduló elemek: {maxok}")

