### Emelt Informatika Érettségi - 2010 Október - Anagramma

# szóban szereplő betűk ábécé sorrendben
def get_szo_betui(szo):
    betuk = []
    for c in szo:
        if c not in betuk:
            betuk.append(c)
    betuk.sort()
    return betuk

# 1. Kérjen be a felhasználótól egy szöveget, majd határozza meg, hogy hány különböző karakter található a szövegben!
#   A darabszámot és a karaktereket írja ki a képernyőre!
print("\n1. feladat")
szoveg = input("Szöveg = ")
szoveg_betui = get_szo_betui(szoveg)
print(f"Különböző karakterek száma: {len(szoveg_betui)}. Különböző karakterek:{szoveg_betui}")

# 2. Olvassa be a szotar.txt állományból a szavakat, és a következő feladatok megoldása során ezekkel dolgozzon!
#   Amennyiben nem tudja beolvasni az állományból a szavakat, akkor az első 10 szóval dolgozzon!
print("\n2. feladat")
szotar = []
with open("szotar.txt", "r") as fileBe:
    for line in fileBe:
        szotar.append(line.strip())
print("Adatok beolvasva a 'szotar.txt' állományból")

# 3. Az állományból beolvasott szavakat alakítsa át úgy, hogy minden szó karaktereit egyenként tegye ábécérendbe!
#   Az így létrehozott szavakat írja ki az abc.txt állományba az eredeti állománnyal egyező sorrendben!
print("\n3. feladat")

# szó betűinek ábécé sorrendje
def get_szo_abc(szo):
    ujszolist = list(szo)
    ujszolist.sort()
    return "".join(ujszolist)

with open("abc.txt", "w") as fileKi:
    for szo in szotar:
        fileKi.writelines(get_szo_abc(szo) + "\n")
print("Adatok kiírva az 'abc.txt' állományba")

# 4. Kérjen be a felhasználótól két szót, és döntse el, hogy a két szó anagramma-e!
#   Ha azok voltak, írja ki a képernyőre az „Anagramma” szót, ha nem, akkor pedig a „Nem anagramma” szöveget!
print("\n4. feladat")
szo_1 = input("Egyik szó = ")
szo_2 = input("Másik szó = ")
if get_szo_abc(szo_1) == get_szo_abc(szo_2):
    print("Anagramma")
else:
    print("Nem anagramma")

# 5. Kérjen be a felhasználótól egy szót!
#   A szotar.txt állomány szavaiból keresse meg a szó anagrammáit (a szót önmagát is annak tekintve)!
#   Ha van találat, azokat egymás alá írja ki a képernyőre, ha nem volt találat, akkor írja ki a „Nincs a szótárban anagramma” szöveget!
print("\n5. feladat")
szo_betui = get_szo_abc(input("Szó = "))
anagrammak = []
for szo in szotar:
    if szo_betui == get_szo_abc(szo):
        anagrammak.append(szo)
if len(anagrammak) == 0:
    print("Nincs a szótárban anagramma")
else:
    print("Anagrammák:")
    for anagramma in anagrammak:
        print(anagramma)

# 6. Határozza meg, hogy a szotar.txt állományban melyik a leghosszabb szó!
#   Ha több, ugyanannyi karakterből álló leghosszabb szó volt, akkor az ugyanazokat a karaktereket tartalmazó szavakat (amelyek egymás anagrammái) közvetlenül egymás alá írja ki!
#   A feltételnek megfelelő összes szó pontosan egyszer szerepeljen a kiírásban!
print("\n5. feladat")
# leghosszabb szó (indexének) megkeresése
max_i = 0
for i in range(1, len(szotar)):
    if len(szotar[i]) > len(szotar[max_i]):
        max_i = i

# leghosszabb szavak kiválogatása (kigyűjtése)
hosszu_anagrammak = []
max_hossz = len(szotar[max_i])
for szo in szotar:
    if len(szo) == max_hossz:
        hosszu_anagramma = {
            'szo': szo,
            'anagramma': "".join(get_szo_abc(szo))
        }
        hosszu_anagrammak.append(hosszu_anagramma)
# hosszú szavak rendezőfüggvénye az anagramma betűi alapján
def sort_by_anagramma(szo):
    return szo['anagramma']

# hosszú szavak kiiratása
hosszu_anagrammak.sort(key=sort_by_anagramma)
for hosszu_anagramma in hosszu_anagrammak:
    print(hosszu_anagramma['szo'])

# 7. Rendezze a szotar.txt állományban lévő szavakat a karakterek száma szerint növekvő sorrendbe!
#   Az egyforma hosszúságú és ugyanazokat a karaktereket tartalmazó szavak (amelyek egymás anagrammái) szóközzel elválasztva ugyanabba a sorba kerüljenek!
#   Az egyforma hosszúságú, de nem ugyanazokat a karaktereket tartalmazó szavak külön sorba kerüljenek!
#   A különböző hosszúságú szavakat egy üres sorral különítse el egymástól!
#   Az így rendezett szavakat írja ki a rendezve.txt állományba!
print("\n7. feladat")
# rendezéshez szükséges kulcs generálása
def get_szotar_key(szo):
    key = ""
    if len(szo) < 10:
        key += "0"
    key += str(len(szo))
    key += "_"
    key += "".join(get_szo_abc(szo))
    return key

# másolatot készítünk az eredeti szótárról és kiegészítjük a rendezéshez szükséges kulcsszóval
szotar2 = []
for szo in szotar:
    ujszo= {
        'szo': szo,
        'key': get_szotar_key(szo)
    }
    szotar2.append(ujszo)

# szavak rendezőfüggvénye a rendezési kulcs alapján
def sort_by_key(szo):
    return szo['key']

szotar2.sort(key=sort_by_key)
last_key = szotar2[0]['key']
line = ""
with open("rendezve.txt", "w") as fileKi:
    for ujszo in szotar2:
        if last_key == ujszo['key']:
            # anagramma
            # hozzáfűzzük az aktuális szót a kiirandó sorba
            line += ujszo['szo'] + " "
        else:
            # nem anagramma
            # kiírjuk az eddigi sort (az utolsó szóközt levágva)
            fileKi.write(line[:-1]+"\n")
            # ha hosszabb, mint az előző, akkor plusz sortörés
            if (len(ujszo['key']) > len(last_key)):
                fileKi.write("\n")
            # újrakezdjük a kiirandó sort
            line = ujszo['szo'] + " "
            # beállítjuk az új kulcsot
            last_key = ujszo['key']
print("Adatok kiírva a 'rendezve.txt' állományba.")
