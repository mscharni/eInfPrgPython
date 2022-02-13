import random
abc = ['0','1','2','3','4','5','6','7','8','9','a','á','b','c','cs','d','dz','dzs','e','é','f','g','gy','h','i','í','j','k','l','ly','m','n','ny','o','ó','ö','ő','p','q','r','s','sz','t','ty','u','ú','ü','ű','v','w','x','y','z','zs']
noabc = [' ','-','.',',',';',':','?','!']
irasjel = ['.',',',';',':','?','!']
hosszuak = {'css': 'cscs', 'dzz': 'dzdz','ggy': 'gygy', 'lly': 'lyly', 'nny':'nyny', 'ssz': 'szsz','tty': 'tyty', 'zzs': 'zszs'}
szavak = ["alma", "alom", "arany", "arány", "álom", "ármány","cica", "cukor", "csalán", "dinnye", "elefánt", "éled", "faggyú", "gyújt", "gyűjt", "hattyú", "macska", "meggy", "nyár", "nyúz", "nyű", "pácsó", "pöttyös", "ólom", "öccs", "öcsi", "öröm", "üröm", "tátika", "tyúk", "vissza","zuza", "zúzmara", "zsanér", "zsurló"]


# betűje sorrendisége
def betu_rel(betu):
    if betu in abc:
        return abc.index(betu)
    else:
        return -1

# szórészlet első betűje (max három karakter hosszú)
def elso_betu(szo):
    if len(szo) >= 3 and szo[0:2] in abc:
        return szo[0:2]
    elif len(szo) >= 2 and szo[0:1] in abc:
        return szo[0:1]
    else:
        return szo[0]
    

# szavakat alkotó betűk listája
def betuz(szo):
    # hosszú (dupla) mássalhangzók cseréje két egyszerű (dupla) mássalhangzóra
    for hosszu in hosszuak.keys():
        szo = szo.replace(hosszu,hosszuak[hosszu])
    betuk = []
    # amíg nem üres a szó, betűzzük
    while len(szo) > 0:
        betu = elso_betu(szo)
        # a rendezés szempontjából felesleges betűket kidobjuk
        if betu not in noabc:
            betuk.append(betu)
        szo = szo[len(betu):]
    return betuk

# szavak összehasonlítása (relációja) a betűik alapján
def szo_rel(a,b):
    a_betuk = betuz(a)
    b_betuk = betuz(b)
    szo_hossz = len(a_betuk) if len(a_betuk) < len(b_betuk) else len(b_betuk) # a rövidebbik szó betűi számossága szerint haladunk
    if szo_hossz == 1:
        return betu_rel(a_betuk[0]) < betu_rel(b_betuk[0])
    else:
        ci = 0
        while ci <szo_hossz  and betu_rel(a_betuk[ci]) == betu_rel(b_betuk[ci]):
            ci += 1
        if ci == szo_hossz:
            return len(a_betuk) < len(b_betuk)
        else:
            return betu_rel(a_betuk[ci]) < betu_rel(b_betuk[ci])

# Buborékos rendezés a név alapján"
def rendez_buborek(adatok):
    for i in range(0, len(adatok) - 1):
        for j in range(1, len(adatok)-i):
            if not szo_rel(adatok[j - 1], adatok[j]):
                cs = adatok[j]
                adatok[j] = adatok[j - 1]
                adatok[j - 1] = cs

# adatok generálása, amelyet rendezni fogunk
# adatok = szavak.copy()
# random.shuffle(adatok)


# adatok beolvasása
print(f"\nAdatok beolvasása folyamatban")
adatok = []
with open("szoveg.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
for line in lines:
    line = line.strip()
    
    # írásjelek eltárvolítása
    for c in irasjel:
        line = line.replace(c,'')
    # sorok szavakra bontása: szóköz által határolt szövegtöredékek
    line_datas = line.split(" ")
    # a nemnulla hosszúságú betűzött szavak letárolása
    for data in line_datas:
        # kisbetűsítés
        data = data.lower()
        if len(betuz(data)) > 0:
            adatok.append(data)    
print(f"\nAdatok beolvasva")

# a szó duplikátumok kiszűrése: halmazzá alakítás 
adatok = set(adatok)
adatok = list(adatok)
"""
# szó - betű
for adat in adatok:
  print(f"{adat} = {betuz(adat)}")
"""

print(f"\nAdatok rendezése folyamatban")
rendez_buborek(adatok)
print(f"\nAdatok rendezve")
with open("szavak.txt","w", encoding="utf-8") as file:
    file.writelines('\n'.join(adatok) + '\n')