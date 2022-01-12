### Informatika Emelt Érettségi - 2013 október - Közúti ellenőrzés

import datetime as dt

# a 'jarmu.txt' állományban szereplő egy-egy sornyi adatnak megfelelő osztály
class Jarmu():
    rendszam = ""                   # jármű rendszáma
    ido = dt.datetime.now().time()  # áthaladási idő
    idomp = 0                       # áthaladási idő másodpercben a nap elejétől számítva
    tipus = 0                       # a jármű típusának kódja

    def __init__(self, line):
        datas = line.split(" ")
        self.rendszam = datas[3]
        self.ido = dt.time(int(datas[0]), int(datas[1]), int(datas[2]))
        self.idomp = int(datas[0])*60*60 + int(datas[1])*60 + int(datas[2])
        tipus = self.rendszam[0].upper()
        if tipus == "B":
            self.tipus = 1  # busz
        elif tipus == "K":
            self.tipus = 2  # kamion
        elif tipus == "M":
            self.tipus = 3  # motor
        else:
            self.tipus = 0 # személygépkocsi

    # a rendszám ellenőrzését megvalósító metódus
    def match(self, query):
        matched = True
        for i in range(0, len(self.rendszam)):
            # csak azon karaktereket kell ellenőrizni, ami nem '*'
            if query[i] != "*":
                # ha legalább egy karakter nem egyezik, akkor a visszadott érték mindenképpen False lesz
                matched = matched and self.rendszam[i].upper() == query[i].upper()
        return matched

# a járművek adatait tartalmazó lista
jarmuvek = []

# 1. Olvassa be a jarmu.txt állományban talált adatokat, s annak felhasználásával oldja meg a következő feladatokat!
print("\n1. feladat")
with open("jarmu.txt", "r") as fileBe:
    for line in fileBe:
        jarmu = Jarmu(line.strip())
        jarmuvek.append(jarmu)
print("Adatok beolvasva.")

# 2. Határozza meg, hogy aznap legalább hány óra hosszat dolgoztak az ellenőrzést végzők, ha munkaidejük egész órakor kezdődik, és pontosan egész órakor végződik!
#   (Minden óra 0 perc 0 másodperckor kezdődik, és 59 perc 59 másodperccel végződik.) Az eredményt jelenítse meg a képernyőn!
print("\n2. feladat")
work_time = jarmuvek[-1].ido.hour - jarmuvek[0].ido.hour + 1
print(f"Legalább {work_time} órát dolgoztak az ellenőrzést végzők.")

# Műszaki ellenőrzésre minden órában egy járművet választanak ki. Azt, amelyik abban az órában először halad arra.
#   Az ellenőrzés óráját és az ellenőrzött jármű rendszámát jelenítse meg a képernyőn a következő formában:
#   9 óra: AB-1234!
# Minden óra adata külön sorba kerüljön! Csak azon órák adatai jelenjenek meg, amikor volt ellenőrizhető jármű!
print("\n3. feladat")
act_hour = jarmuvek[0].ido.hour
for jarmu in jarmuvek:
    if jarmu.ido.hour == act_hour:
        print(f"{act_hour} óra: {jarmu.rendszam}")
        act_hour +=1

# 4. A rendszám első karaktere külön jelentéssel bír. Az egyes betűk közül a „B” autóbuszt,
#   a „K” kamiont, az „M” motort jelöl, a többi rendszámhoz személygépkocsi tartozik.
#   Jelenítse meg a képernyőn, hogy az egyes kategóriákból hány jármű haladt el az ellenőrző pont előtt!
print("\n4. feladat")
# a típusnak megfelelő sorszámú összesítések listája
jarmu_count = [0, 0, 0, 0]
for jarmu in jarmuvek:
    jarmu_count[jarmu.tipus] += 1
print(f"{jarmu_count[0]} szzemélygépjármű, {jarmu_count[1]} autóbusz, {jarmu_count[2]} kamion, {jarmu_count[3]} motor haladt át az ellenőrző pont előtt")

# 5. Mettől meddig tartott a leghosszabb forgalommentes időszak? A választ jelenítse meg a képernyőn a következő formában:
#   9:9:13 - 9:15:3!
print("\n5. feladat")
idle_index = 0
# az első üresjárati időintervallum
idle_period = jarmuvek[idle_index + 1].idomp - jarmuvek[idle_index].idomp
for i in range(1, len(jarmuvek)-1):
    if jarmuvek[i + 1].idomp - jarmuvek[i].idomp > idle_period:
        idle_index = i
        idle_period = jarmuvek[i + 1].idomp - jarmuvek[i].idomp
print(f"A leghosszabb forgalommentes időszak: {jarmuvek[idle_index].ido} - {jarmuvek[idle_index+1].ido}, ami {idle_period} másodperc volt. ")

# A rendőrök egy baleset közelében látott járművet keresnek rendszám alapján.
#   A szemtanúk csak a rendszám bizonyos karaktereire emlékeztek, így a rendszám ismeretlen karaktereit a * karakterrel helyettesítve keresik a nyilvántartásban.
#   Kérjen be a felhasználótól egy ilyen rendszámot, majd jelenítse meg a képernyőn az arra illeszthető rendszámokat!
print("\n6. feladat")
# a keresésnek megfelelő rendszámok listája (nem kötelező, közvetlenül is ki lehetne írni a megfelelő rendszámokat a listában való letárolás helyett)
matched = []
rendsz = input("Adja meg a keresett rendszámot! (7 karakter): ")
for jarmu in jarmuvek:
    if jarmu.match(rendsz):
        matched.append(jarmu.rendszam)
if len(matched) == 0 :
    print(f" A '{rendsz}' keresésnek egyetlen rendszám sem felel meg!")
else:
    print(f"A '{rendsz}' keresésnek megfelelő rendszámok:")
    for i in range(0, len(matched)):
        print(matched[i])

# 7. Egy közúti ellenőrzés pontosan 5 percig tart. Amíg az ellenőrzés folyik, a járművek szabadon elhaladhatnak,
#   a következő megállítására csak az ellenőrzés befejezése után kerül sor.
#   Ha a rendőrök a legelső járművet ellenőrizték, akkor mely járműveket tudták ellenőrizni a szolgálat végéig?
#   Írja az ellenőrzött járművek áthaladási idejét és rendszámát a vizsgalt.txt állományba az áthaladás sorrendjében,
#   a bemenettel egyező formában!
#   Ügyeljen arra, hogy az időadatokhoz tartozó számok a bevezető nullákat tartalmazzák!
print("\n7. feladat")
act_idx = 0
# 5 perc másodpercben megadva
time_diff = 5*60
with open("vizsgalt.txt", "w") as fileKi:
    for i in range(1, len(jarmuvek)):
        if jarmuvek[i].idomp >= jarmuvek[act_idx].idomp + time_diff:
            fileKi.write(f"{jarmuvek[i].ido.strftime('%H %M %S')} {jarmuvek[i].rendszam}\n")
            act_idx = i
print("Vizsgált járművek adatai kiírva a 'vizsgalt.txt' állományba!")
