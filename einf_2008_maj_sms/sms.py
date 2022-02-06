### Emelt Informatika Érettségi - 2008 Május - SMS

class Uzenet():
    def __init__(self, idx, line_1, line_2):
        self.idx = idx
        datas = line_1.split(" ")
        self.ora = int(datas[0])
        self.perc = int(datas[1])
        self.tel = datas[2]
        self.sms = line_2
        self.hossz = len(self.sms)

uzenetek = []

# 1. Olvassa be az sms.txt állományban talált adatokat, s annak felhasználásával oldja meg a következő feladatokat!
print("\n1. feladat")
# a mellékelt forrásállomány windows-1252 kódolású ékezetes karaktert tartalmaz...
with open("sms.txt", "r", encoding="windows-1252") as fileBe:
    sms_count = int(fileBe.readline().strip())
    for idx in range(1, sms_count+1):
        line_1 = fileBe.readline().strip()
        line_2 = fileBe.readline().strip()
        uzenetek.append(Uzenet(idx, line_1, line_2))
print("Adatok beolvasva a 'sms.txt' állományból.")

# 2. A fájlban tárolt utolsó üzenet érkezésekor melyik üzenet a legfrissebb a telefon memóriájában?
#   Írja az üzenet szövegét a képernyőre!
#   A telefon legfeljebb az először érkező 10 darab, egyenként legfeljebb 100 karakteres üzenetet tudja eltárolni.
print("\n2. feladat")
sms_10 = uzenetek[9]
print(f"{sms_10.sms}")

# 3. Adja meg a leghosszabb és a legrövidebb üzenetek adatait!
#   Ha több azonos hosszúságú üzenet van, akkor elegendő csak egyet-egyet megadnia!
#   A képernyőn óra, perc, telefonszám, üzenet formában jelenítse meg az adatokat!
print("\n3. feladat")
min_i = 0
max_i = 0
# minimum és maximumkiválasztás
for i in range(0, sms_count):
    if uzenetek[i].hossz < uzenetek[min_i].hossz:
        min_i = i
    if uzenetek[i].hossz > uzenetek[max_i].hossz:
        max_i = i
print(f"Legrövidebb: Idő = {uzenetek[min_i].ora:2}:{uzenetek[min_i].perc:2} Tel = {uzenetek[min_i].tel:9} Üzenet = {uzenetek[min_i].sms}")
print(f"Leghosszabb: Idő = {uzenetek[max_i].ora:2}:{uzenetek[max_i].perc:2} Tel = {uzenetek[max_i].tel:9} Üzenet = {uzenetek[max_i].sms}")

# 4. Készítsen karakterhossz szerinti statisztikát: 1-20, 21-40, 41-60, 61-80, 81-100!
#   Az intervallumok mellé a hozzájuk tartozó üzenetek darabszámát írja, mint eredményt a képernyőre!
print("\n4. feladat")
stat = [0, 0, 0, 0, 0]          # a statisztika
for i in range(0, sms_count):
    stat[(uzenetek[i].hossz-1) // 20] += 1          # eggyel rövidebb üzenetet osztunk el 20-al, hogy a határok (pl 20 jó sávba essen)
for i in range(0, len(stat)):
    tol = i*20 +1
    ig  = (i+1) *20
    print(f"{tol:3}-{ig:3} : {stat[i]:3}")

# 5. Ha Ernő minden óra 0. percében elolvasná a memóriában lévő üzeneteket (az éppen ekkor érkező üzeneteket nem látja), majd ki is törölné,
#   akkor hány olyan üzenet lenne, amelynek elolvasásához fel kellene hívnia a szolgáltatót?
#   Írja ezt a számot a képernyőre! (Az üzeneteket először 1, utoljára 24 órakor olvassa el.)
print("\n5. feladat")
# végigmegyünk az üzeneteken és növeljük az üzenetek számát
print("'A' változat")
#   Amikor óraváltás van, akkor megnézzük, hogy 10-nél több üzenet gyűlt-e össze, ha a többlettel növeljük a nem kézbesített üzenetek számát, majd "nullázzuk" az addigi üzenetek számát
sms_db = 0
sms_sum = 0
utso_ora = uzenetek[0].ora
for i in range(0, sms_count):
    if uzenetek[i].ora == utso_ora:
        sms_db += 1
    else:
        if sms_db > 10:
            sms_sum += sms_db -10
        sms_db = 1                      # az aktuális (óraváltáskori) üzenetet bele kell számolni
        utso_ora = uzenetek[i].ora      # frissítjük az utolsó óra értékét az aktuális üzenet órájára
print(f"{sms_sum} olyan üzenet lenne, amelynek elolvasásához fel kellene hívnia a szolgáltatót.")

print("'B' változat")
#   összeszámoljuk, hogy az adott órában hány üzenet érkezett, majd a végén kigyűjtjük azon órákat, amelyben 10-nél több üzenet érkezett
orak = [0 for i in range(0, 24)]
for i in range(0, sms_count):
    orak[uzenetek[i].ora] += 1
sms_sum = 0
for i in range(0, len(orak)):
    if orak[i] > 10:
        sms_sum += orak[i] - 10
print(f"{sms_sum} olyan üzenet lenne, amelynek elolvasásához fel kellene hívnia a szolgáltatót.")

# 6. Ernő barátnője gyakran küld sms-t az 123456789-es számról.
#   Mennyi volt a leghosszabb idő, amennyi eltelt két üzenete között?
#   Ha legfeljebb 1 üzenet érkezett tőle, akkor írja ki, hogy „nincs elegendő üzenet”, egyébként pedig adja meg a leghosszabb időtartamot óra perc alakban!
print("\n6. feladat")
# megkeressük az első üzenetet
erno_i = 0
erno_tel = "123456789"
max_ido = 0
while uzenetek[erno_i].tel != erno_tel and erno_i < len(uzenetek):
    erno_i += 1
if erno_i == len(uzenetek):
    print(f"Ernő nem kapott sms-t a {erno_tel} telefonszámról")
else:
    # végigmegyünk a maradék üzeneten
    elso_i = erno_i + 1
    for i in range(elso_i, len(uzenetek)):
        # ha a megadott számról érkezett
        if uzenetek[i].tel == erno_tel:
            # kiszámoljuk az előző üzenet érkezése óta eltelt időt percben
            tartam = (uzenetek[i].ora * 60 + uzenetek[i].perc) - (uzenetek[erno_i].ora * 60 + uzenetek[erno_i].perc)
            # ha nagyobb, akkor eltároljuk
            if tartam > max_ido:
                max_ido = tartam
            erno_i = i
    if max_ido == 0:
        # nem volt több üzenet a megadott számról
        print("Nincs elegendő üzenet")
    else:
        ora = max_ido // 60
        perc = max_ido - 60 * ora
        print(f"A leghosszabb időtartam két {erno_tel} üzenete között = {ora:2}:{perc:2}")

# 7. Egy üzenet véletlenül késett. Olvassa be a billentyűzetről ennek az sms-nek az adatait, majd tárolja el a memóriában a többihez hasonlóan!
print("\n7. feladat")
ora = input("Óra = ")
perc = input("Perc = ")
tel = input("Telefon = ")
sms = input("Üzenet = ")
line = ora + " " + perc + " " + tel
uzenetek.append(Uzenet(sms_count + 1, line, sms))

# 8. Az smski.txt állományban készítsen egy listát az üzenetekről telefonszám szerinti csoportosításban, telefonszám szerint növekvő sorrendben!
#   Egy csoporthoz tartozó első sorban a feladó telefonszáma szerepeljen!
#   Az alatta lévő sorokban a feladás ideje, majd a tőle újabb szóközzel elválasztva az üzenet szövege szerepeljen!
print("\n8. feladat")
# rendezzük az üzeneteket a telefonszám, s azon belül idő szerint
def sort_by_tel(uzenet):
    key = uzenet.tel + " "
    if uzenet.ora < 10:
        key += "0"
    key += str(uzenet.ora)
    if uzenet.perc < 10:
        key += "0"
    key += str(uzenet.perc)
    return key

uzenetek.sort(key=sort_by_tel)
utso_tel = ""

with open("smski.txt", "w", encoding="utf-8") as fileKi:
    # végigmegyünk az összes üzeneten
    for uzenet in uzenetek:
        # ha eltér az utolsó telefontól, akkor új csoport kezdősik
        if uzenet.tel != utso_tel:
            fileKi.write(f"{uzenet.tel}\n")
            utso_tel = uzenet.tel
        # kiírjuk az üzenet adatait
        fileKi.write(f"{uzenet.ora} {uzenet.perc} {uzenet.sms}\n")
