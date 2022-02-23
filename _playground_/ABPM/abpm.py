import math
# 1. Feladat adatok beolvasása
lines = []
with open("abpm.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# 'Codes\tMessage' típusú adatok a végéről
joadatok =[]
adatok = []
kodok = {}

hatarIndex = lines.index("\n")
for i in range(hatarIndex+2, len(lines)):
    line = lines[i].strip().split("\t")
    # Codes	Message
    kodok[line[0]] = line[1]     


# 'Time\tCode\tSystole\tDiastole\tPulse\n' típusú adatok az elejéről
# --> joadatok listába, ha 5 adat szerepel benne,
# --> adatok listába az osszes (jó és rossz) adat
for i in range(1, hatarIndex-1):
    line = lines[i].strip().split("\t")
    if len(line) == 5:
        # 5 --> jó adatok
        ido = line[0].split(":")
        adat = {
            'ora' : int(ido[0]),
            'perc' : int(ido[1]),
            'sys': int(line[2]),
            'dia': int(line[3]),
            'pul': int(line[4]),
            'msg': kodok[line[1]]
            }
        joadatok.append(adat)
        adatok.append(adat)
    else:
        # 2 --> hibás mérés
        adat = {
            'ora' : int(ido[0]),
            'perc' : int(ido[1]),
            'msg': kodok[line[1]]
        }
        adatok.append(adat)

# 2., Állapítsa meg a legmagasabb és legalacsonyabb Sys és Dia vérnyomás és pulzus értékeket.
# Minden statisztikai adatot egy szótárban tárolunk le, s nem különálló változókban
stats = {
    'minSys' : joadatok[0],
    'maxSys' : joadatok[0],
    'minDia' : joadatok[0],
    'maxDia' : joadatok[0],
    'minPul' : joadatok[0],
    'maxPul' : joadatok[0],
    'sumSys' : 0,
    'sumDia' : 0,
    'sumPul' : 0,
    'sumDb'  : len(joadatok)
}

for joadat in joadatok:
    if joadat['sys'] < stats['minSys']['sys']: stats['minSys'] = joadat
    if joadat['sys'] > stats['maxSys']['sys']: stats['maxSys'] = joadat
    if joadat['dia'] < stats['minDia']['dia']: stats['minDia'] = joadat
    if joadat['dia'] > stats['maxDia']['dia']: stats['maxDia'] = joadat
    if joadat['pul'] < stats['minPul']['pul']: stats['minPul'] = joadat
    if joadat['pul'] > stats['maxPul']['pul']: stats['maxPul'] = joadat
    stats['sumSys'] += joadat['sys']
    stats['sumDia'] += joadat['dia']
    stats['sumPul'] += joadat['pul']

print(f"\nStatisztikai adatok:")
print(f"sys min: {stats['minSys']['sys']}")
print(f"sys max: {stats['maxSys']['sys']}")
print(f"dia min: {stats['minSys']['dia']}")
print(f"dia max: {stats['maxSys']['dia']}")
print(f"pul min: {stats['minPul']['pul']}")
print(f"pul max: {stats['maxPul']['pul']}")

# 3., Állapítsa meg a vérnyomás és pulzus értékek átlagát, móduszát, mediánját, terjedelmét, szórását.
stats['terSys'] = stats['maxSys']['sys']- stats['minSys']['sys']
stats['terDia'] = stats['maxDia']['dia']- stats['minDia']['dia']
stats['terPul'] = stats['maxPul']['pul']- stats['minPul']['pul']
print(f"sys terjedelem: {stats['terSys']}")
print(f"dia terjedelem: {stats['terDia']}")
print(f"pul terjedelem: {stats['terPul']}")

stats['atlSys'] = stats['sumSys']/stats['sumDb']
stats['atlDia'] = stats['sumDia']/stats['sumDb']
stats['atlPul'] = stats['sumPul']/stats['sumDb']
print(f"sys átlag: {stats['atlSys']:.2f}")
print(f"dia átlag: {stats['atlDia']:.2f}")
print(f"pul átlag: {stats['atlPul']:.2f}")

# köztes adatok
stats['eltSumSys'] = 0
stats['eltSumDia'] = 0
stats['eltSumPul'] = 0
stats['gytSys'] = {}
stats['gytDia'] = {}
stats['gytPul'] = {}

for joadat in joadatok:
    joadat['eltSys'] = (stats['atlSys'] - joadat['sys'])**2
    joadat['eltDia'] = (stats['atlDia'] - joadat['dia'])**2
    joadat['eltPul'] = (stats['atlPul'] - joadat['pul'])**2
    stats['eltSumSys'] += joadat['eltSys']
    stats['eltSumDia'] += joadat['eltDia']
    stats['eltSumPul'] += joadat['eltPul']
    # Sys
    if joadat['sys'] in stats['gytSys']:
        # már szerepel, ezért növelem eggyel
        stats['gytSys'][joadat['sys']] += 1
    else:
        # nincs benne, hozzáadom
        stats['gytSys'][joadat['sys']] = 1
    # Dia
    if joadat['dia'] in stats['gytDia']:
        # már szerepel, ezért növelem eggyel
        stats['gytDia'][joadat['dia']] += 1
    else:
        # nincs benne, hozzáadom
        stats['gytDia'][joadat['dia']] = 1
    # Pul
    if joadat['pul'] in stats['gytPul']:
        # már szerepel, ezért növelem eggyel
        stats['gytPul'][joadat['pul']] += 1
    else:
        # nincs benne, hozzáadom
        stats['gytPul'][joadat['pul']] = 1

stats['szorSys'] = math.sqrt(stats['eltSumSys']/stats['sumDb'])
stats['szorDia'] = math.sqrt(stats['eltSumDia']/stats['sumDb'])
stats['szorPul'] = math.sqrt(stats['eltSumPul']/stats['sumDb'])
print(f"sys szórás: {stats['szorSys']:.2f}")
print(f"dia szórás: {stats['szorDia']:.2f}")
print(f"pul szórás: {stats['szorPul']:.2f}")


# gyakorisági táblázat max értékének kiválasztása
# sys
stats['darabSys']= max(stats['gytSys'].values())
stats['modusSys'] = []
for i in stats['gytSys']:
    if stats['gytSys'][i] == stats['darabSys']:
        stats['modusSys'].append(i)
if len(stats['modusSys']) == 1 :
    print(f"Sys: Módusz: érték:{stats['modusSys'][0]} előfordulás: {stats['darabSys']}")
else:
    print(f"Sys: Nincs egyértelmű módusz, a legtöbbször előforduló elemek: {stats['modusSys']} előfordulás: {stats['darabSys']}")

# dia
stats['darabDia']= max(stats['gytDia'].values())
stats['modusDia'] = []
for i in stats['gytDia']:
    if stats['gytDia'][i] == stats['darabDia']:
        stats['modusDia'].append(i)
if len(stats['modusDia']) == 1 :
    print(f"Dia: Módusz: érték:{stats['modusDia'][0]} előfordulás: {stats['darabDia']}")
else:
    print(f"Dia:Nincs egyértelmű módusz, a legtöbbször előforduló elemek: {stats['modusDia']} előfordulás: {stats['darabDia']}")

# pul
stats['darabPul']= max(stats['gytPul'].values())
stats['modusPul'] = []
for i in stats['gytPul']:
    if stats['gytPul'][i] == stats['darabPul']:
        stats['modusPul'].append(i)
if len(stats['modusPul']) == 1 :
    print(f"Pul: Módusz: érték:{stats['modusPul'][0]} előfordulás: {stats['darabPul']}")
else:
    print(f"Pul:Nincs egyértelmű módusz, a legtöbbször előforduló elemek: {stats['modusPul']} előfordulás: {stats['darabPul']}")

