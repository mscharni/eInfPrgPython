class Cim():
    ipv6 = ""
    type = 0
    short = ""
    def __init__(self, ip):
        self.ipv6 = ip.strip()
        self.type = self.get_type()
        self.short = self.get_short()
        self.shorter = self.get_shorter()

    def get_type(self):
        _type = 0
        if self.ipv6[0:9] == "2001:0db8":
            # dokumentációs cím
            _type = 1
        elif self.ipv6[0:7] == "2001:0e":
            # globális egyedi cím
            _type = 2
        elif self.ipv6[0:2] == "fc" or self.ipv6[0:2] == "fd":
            # helyi egyedi cím
            _type = 3
        return _type

    def get_short(self):
        # TODO: Az egyes csoportokban a bevezető nullák elhagyhatók. \
        #  Például: 2001:0db8:03cd:0000:0000:ef45:0006:0123
        #  Rövidítve: 2001:db8:3cd:0:0:ef45:6:123
        _segments = self.ipv6 + "_"
        _segments = _segments.replace(":0000", ":0")
        _segments = _segments.replace(":000", ":0")
        _segments = _segments.replace(":00", ":0")
        _segments = _segments.replace(":0", ":")
        # vissza kell rakni a dupla kettőspontok közé a nullát...
        _segments = _segments.replace("::", ":0:")
        _segments = _segments.replace("::", ":0:")
        _segments = _segments.replace("::", ":0:")
        # ha a végén csupa nulla áll, azt külön  le kell kezelni
        _segments = _segments.replace(":_", ":0_")
        return _segments[:-1]

    def get_shorter(self):
        # TODO: Kettő vagy több csak nullákból álló csoportot le lehet egyszerűsíteni két kettőspont közötti üres csoportra. \
        #  Ezzel a szabállyal tovább egyszerűsítve az előző címet: \
        #  Például: 2001:0db8:03cd:0000:0000:ef45:0006:0123
        #  Rövidítve: 2001:db8:3cd::ef45:6:123 \
        #  Ha egy címben több helyen is vannak csak nullákból álló csoportok, akkor is csak  egyszer lehet ez utóbbi módszerrel rövidítést végrehajtani. \
        #  Ilyen esetben mindig a több nullás csoportot kell rövidíteni. \
        #  Ha azonos számú nullás csoport található a címen belül több helyen is, akkor balról az elsőt kell rövidíteni. \
        #  Például: 2001:0000:0000:00f5:0000:0000:0000:0123 \
        #  Rövidítve: 2001:0:0:f5::123
        _segments = self.short + ":"
        # csak nullás csoportokból a baloldalról leghosszabbat kell helyettesíteni
        _strs = ":0:0:0:0:0:0:0:"
        _find = False
        _end = False
        for i in range(len(_strs), 3, -2):
            _str = _strs[0:i]
            _idx =_segments.find(_str)
            if _idx > 0 and _find == False:
                _find = True
                if _idx + len(_str) == len(_segments):
                    _end = True
                _segments = _segments[0: _idx] + "::" + _segments[_idx + len(_str):]

        if _end:
            # ha a legvégén van a rövídítendő, akkor korrigálni kell
            _segments = _segments + ":"
        return _segments[: -1]

cimek = []

# 1. Olvassa be az ip.txt állományban talált adatokat, s annak felhasználásával oldja meg a következő feladatokat!
print("\n1. feladat")
with open("ip.txt", "r") as file:
    for line in file:
        cim = Cim(line)
        cimek.append(cim)


# 2. Határozza meg és írja a képernyőre, hogy hány adatsor van az állományban!
print("\n2. feladat")
print(f"Az állományban {len(cimek)} darab adatsor van.")

# 3. Írja a képernyőre az állományban található legalacsonyabb IP-címet!
# A megoldásában felhasználhatja, hogy a betűk ASCII-kódjai a számok ASCII-kódjai után találhatók a kódtáblában.
print("\n3. feladat")
lowest_cim = cimek[0].ipv6
for i in range(1, len(cimek)):
    if lowest_cim > cimek[i].ipv6:
        lowest_cim = cimek[i].ipv6
print(f"A legalacsonyabb tárolt IP-cím: {lowest_cim}")

# 4. Határozza meg, hogy az állományban hány darab IP-cím van az egyes fajtákból!
# Az eredményt jelenítse meg a képernyőn a mintának megfelelően!
print("\n4. feladat")
types = [0, 0, 0, 0]
for i in range(0, len(cimek)):
    types[cimek[i].type] += 1
print(f"Dokumentációs cím: {types[1]} darab")
print(f"Globális egyedi cím: {types[2]} darab")
print(f"Helyi egyedi cím: {types[3]} darab")

# 5. Gyűjtse ki a sok.txt állományba azokat az IP-címeket, melyek legalább 18 nullát tartalmaznak!
#  A fájlban minden sor elején szerepeljen az eredeti állományból a cím sorszáma!
#  Ezt kövesse egy szóközzel elválasztva a cím az ip.txt állományban szereplő alakjával!
with open("sok.txt", "w") as file:
    for i in range(0, len(cimek)):
        if cimek[i].ipv6.count("0") >= 18:
            file.writelines(f"{i+1} {cimek[i].ipv6}\n")

#6. Kérjen be a felhasználótól egy sorszámot!
# Az állományban a megadott sorszámon található IP-címet rövidítse a csoportokon belüli bevezető nullák elhagyásával!
# Az állományban található alakot és a rövidített változatot írja a képernyőre egymás alá!
print("\n6. feladat")
user_ip = int(input("Kérek egy sorszámot: "))
user_cim = cimek[user_ip-1]
print(cimek[user_ip-1].ipv6)
print(cimek[user_ip-1].short)

#7. Az előző feladatban használt IP-címet rövidítse tovább az egymást követő nullás csoportok rövidítésére vonatkozó szabályoknak megfelelően!
# Az eredményt jelenítse meg a képernyőn! Amennyiben nem rövidíthető, írja ki: „Nem rövidíthető tovább.”!
print("\n7. feladat")
if cimek[user_ip-1].short != cimek[user_ip-1].shorter:
    print(cimek[user_ip-1].shorter)
else:
    print("Nem rövidíthető tovább.")