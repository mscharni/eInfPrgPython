import time
abc = ['0','1','2','3','4','5','6','7','8','9','a','á','b','c','cs','d','dz','dzs','e','é','f','g','gy','h','i','í','j','k','l','ly','m','n','ny','o','ó','ö','ő','p','q','r','s','sz','t','ty','u','ú','ü','ű','v','w','x','y','z','zs']
irasjel = ['.',',',';',':','?','!']
noabc = [' ','-'] + irasjel
hosszuak = {'css': 'cscs', 'dzz': 'dzdz','ggy': 'gygy', 'lly': 'lyly', 'nny':'nyny', 'ssz': 'szsz','tty': 'tyty', 'zzs': 'zszs'}

# betűje sorrendisége
def betu_rel(betu):
    if betu in abc:
        return abc.index(betu)
    else:
        return -1

# szórészlet első abc-beli betűje
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
        # a rendezés szempontjából felesleges betűket kihagyjuk
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
        # ha az egyik szó eleje megegyezik a másik szóval, akkor a hossz dönt
        if ci == szo_hossz:
            return len(a_betuk) < len(b_betuk)
        else:
            return betu_rel(a_betuk[ci]) < betu_rel(b_betuk[ci])

# Buborékos rendezés a név alapján
def rendez_bub(_adatok):
    for i in range(0, len(_adatok) - 1):
        for j in range(1, len(_adatok)-i):
            if not szo_rel(_adatok[j - 1], _adatok[j]):
                cs = _adatok[j]
                _adatok[j] = _adatok[j - 1]
                _adatok[j - 1] = cs
    return _adatok

# Maximumkiválasztásos rendezés a név alapján
def rendez_max(_adatok):
    for i in range(len(_adatok)-1,0,-1):
        maxi = i
        for j in range(0, i-1):
            if szo_rel(_adatok[maxi], _adatok[j]):
                maxi = j
        print
        cs = _adatok[maxi]
        _adatok[maxi] = _adatok[i]
        _adatok[i] = cs
    return _adatok

# Shell rendezés név alapján
def rendez_shell(_adatok):
    gap = 1
    n = len(_adatok)
    while gap*2 <= n:
        gap *= 2
    gap = gap - 1
    while gap > 0:
        i = 0
        while i <= gap and i + gap < n:
            j = i + gap
            while j < n:
                elem = _adatok[j]
                index = j - gap
                while index > -1 and szo_rel(elem,_adatok[index]):
                    _adatok[index + gap] = _adatok[index]
                    index = index - gap
                _adatok[index + gap] = elem
                j += gap
            i += 1
        gap = gap // 2
    return _adatok

# adatok beolvasása
filename = "szoveg.txt"
print(f"\nAdatok beolvasása a(z) '' állományból")
adatok = []
with open(filename, "r", encoding="utf-8") as file:
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
print(f"Adatok beolvasva")

# a szó duplikátumok kiszűrése: halmazzá alakítás 
adatok = set(adatok)
adatok = list(adatok)

print(f"\nAdatok rendezése folyamatban")
ido1 = time.time()
rend = "shell"
filename = "szavak_" + rend + ".txt"
if rend == "bub": 
    rendezett = rendez_bub(adatok)
elif rend == "max": 
    rendezett = rendez_max(adatok)
elif rend == "shell": 
    rendezett = rendez_shell(adatok)
ido2 = time.time()
print(f"{len(adatok)} adat rendezve {rend} módszerrel: {ido2-ido1} másodperc alatt")

with open(filename,"w", encoding="utf-8") as file:
    file.writelines('\n'.join(rendezett) + '\n')
print(f"\nAdatok kiírva a '{filename}' állományba.")    