import random
abc = ['-','0','1','2','3','4','5','6','7','8','9','a','á','b','c','cs', 'd','dz', 'dzs','e', 'é','f','g','gy', 'h','i','í','j','k','l','ly', 'm','n','ny','o','ó','ö','ő','p','q','r','s','sz','t','ty','u','ú','ü','ű','v','w','x','y','z','zs']
hosszuak = {'css': 'cscs', 'dzz': 'dzdz','ggy': 'gygy', 'lly': 'lyly', 'nny':'nyny', 'ssz': 'szsz','tty': 'tyty', 'zzs': 'zszs'}
szavak = ["alma", "alom", "arany", "arány", "álom", "ármány","cica", "cukor", "csalán", "dinnye", "elefánt", "éled", "faggyú", "gyújt", "gyűjt", "hattyú", "macska", "meggy", "nyár", "nyúz", "nyű", "pácsó", "pöttyös", "ólom", "öccs", "öcsi", "öröm", "üröm", "tátika", "tyúk", "vissza","zuza", "zúzmara", "zsanér", "zsurló"]

# adatok generálása, amelyet rendezni fogunk
adatok = szavak.copy()
random.shuffle(adatok)

def betu_rel(betu):
    if betu in abc:
        return abc.index(betu)
    else:
        return -1

# szó első betűje (max három karakter hosszú)
def elso_betu(szo):
    if len(szo) >= 3 and szo[0:2] in abc:
        return szo[0:2]
    elif len(szo) >= 2 and szo[0:1] in abc:
        return szo[0:1]
    else:
        return szo[0]
    

# szavak betűi listában
def betuz(szo):
    # hosszú (dulpa) mássalhangzók cseréje
    for hosszu in hosszuak.keys():
        szo = szo.replace(hosszu,hosszuak[hosszu])

    betuk = []
    while len(szo) > 0:
        betu = elso_betu(szo)
        betuk.append(betu)
        szo = szo[len(betu):]
            
    return betuk

# szavak összehasonlítása (relációja)
def szo_rel(a,b):
    a_betuk = betuz(a)
    b_betuk = betuz(b)
    szo_hossz = len(a_betuk) if len(a_betuk) < len(b_betuk) else len(b_betuk)
    ci = 0
    while ci <szo_hossz  and betu_rel(a_betuk[ci]) == betu_rel(b_betuk[ci]):
        ci += 1
    return betu_rel(a_betuk[ci]) < betu_rel(b_betuk[ci])

for adat in adatok:
  print(f"{adat} = {betuz(adat)}")

"""
print("\nRendezendő adatok:")
for adat in adatok:
  print(adat)
"""

# Buborékos rendezés a név alapján"
def rendez_buborek(adatok):
    for i in range(0, len(adatok) - 1):
        for j in range(1, len(adatok)-i):
            if szo_rel(adatok[j - 1], adatok[j]):
                cs = adatok[j]
                adatok[j] = adatok[j - 1]
                adatok[j - 1] = cs

"""
rendez_buborek(adatok)
for adat in adatok:
  print(adat)
"""