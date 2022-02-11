import random
abc = ['a','á','b','c','cs','d','dz','dzs','e', 'é','f','g','gy','h','i','í','j','k','l','ly','m','n','ny','o','ó','ö','ő','p','q','r','s','sz','t','ty','u','ú','ü','ű','v','w','x','y','z','zs']

szavak = ["alma", "arany", "álmos", "cica", "csalán", "cukor", "elefánt", "éled", "nyár","ólom", "öröm", "üröm", "tátika", "tyúk", "zuza", "zúzmara", "zsanér", "zsurló"]

# adatok generálása, amelyet rendezni fogunk
adatok = szavak.copy()
random.shuffle(adatok)

def betu_rel(betu):
    if betu in abc:
        return abc.index(betu)
    else:
        return -1

def elso_betu(szo):
    if len(szo) >= 3 and szo[0:2] in abc:
        return szo[0:2]
    elif len(szo) >= 2 and szo[0:1] in abc:
        return szo[0:1]
    else:
        return szo[0]
    

# szavak betűi listában
def betuz(szo):
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

print("\nRendezendő adatok:")
for adat in adatok:
  print(adat)


print(f"\nBuborékos rendezés a név alapján")
for i in range(0, len(adatok) - 1):
    for j in range(1, len(adatok)-i):
        if szo_rel(adatok[j - 1], adatok[j]):
            cs = adatok[j]
            adatok[j] = adatok[j - 1]
            adatok[j - 1] = cs

for adat in adatok:
  print(adat)
