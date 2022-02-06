### Emelt Informatika Érettségi - 2007 Október - Foci

class Merkozes():
    def __init__(self, idx, line):
        datas = line.strip().split(" ")
        self.idx = idx
        self.fordulo = int(datas[0])            # max 20 forduló
        self.gol_meccs_hazai = int(datas[1])    # max 9 gól
        self.gol_meccs_vendeg = int(datas[2])   # max 9 gól
        self.gol_felido_hazai = int(datas[3])   # max 9 gól
        self.gol_felido_vendeg = int(datas[4])  # max 9 gól
        self.csapat_hazai = datas[5]            # max 20 karakter
        self.csapat_vendeg = datas[6]           # max 20 karakter

merkozesek = []

# 1. Olvassa be a meccs.txt állományban talált adatokat, s annak felhasználásával oldja meg a következő feladatokat!
print("\n1.feladat")
with open("meccs.txt", "r") as fileBe:
    fileBe.readline()           # nem használjuk, csak ki kell olvasni
    i = 0
    for line in fileBe:
        merkozes = Merkozes(i, line.strip())
        merkozesek.append(merkozes)
print("Adatok beolvasva a 'meccs.txt' állományból.")

# 2. Kérje be a felhasználótól egy forduló számát, majd írja a képernyőre a bekért forduló mérkőzéseinek adatait a következő formában:
#   Edes-Savanyu: 2-0 (1-0)
#   Soronként egy mérkőzést tüntessen fel! A különböző sorokban a csapatnevek ugyanazon a pozíción kezdődjenek!
#   FIXIT: a kitűzött feladathoz mellékelt mintában nincs formázott kiírás
print("\n2.feladat")
fordulo = int(input("Forduló száma = "))
for merkozes in merkozesek:
    if merkozes.fordulo == fordulo:
        # minta szerinti kimenet
        print(f"{merkozes.csapat_hazai}-{merkozes.csapat_vendeg}: {merkozes.gol_meccs_hazai}-{merkozes.gol_meccs_vendeg} ({merkozes.gol_felido_hazai}-{merkozes.gol_felido_vendeg})")
        # feladat kitűzése szerinti kimenet
        # print(f"{merkozes.csapat_hazai:20}-{merkozes.csapat_vendeg:20}: {merkozes.gol_meccs_hazai}-{merkozes.gol_meccs_vendeg} ({merkozes.gol_felido_hazai}-{merkozes.gol_felido_vendeg})")

# 3. Határozza meg, hogy a bajnokság során mely csapatoknak sikerült megfordítaniuk az állást a második félidőben!
#   Ez azt jelenti, hogy a csapat az első félidőben vesztésre állt ugyan, de sikerült a mérkőzést megnyernie.
#   A képernyőn soronként tüntesse fel a forduló sorszámát és a győztes csapat nevét!
print("\n3.feladat")
print("'A' megoldás")
for merkozes in merkozesek:
    # félidő nyertese
    if merkozes.gol_felido_vendeg > merkozes.gol_felido_hazai:
        nyertes_felido = merkozes.csapat_vendeg
    elif merkozes.gol_felido_vendeg < merkozes.gol_felido_hazai:
        nyertes_felido = merkozes.csapat_hazai
    else:
        nyertes_felido = ""
    # meccs nyertese
    if merkozes.gol_meccs_vendeg > merkozes.gol_meccs_hazai:
        nyertes_meccs = merkozes.csapat_vendeg
    elif merkozes.gol_meccs_vendeg < merkozes.gol_meccs_hazai:
        nyertes_meccs = merkozes.csapat_hazai
    else:
        nyertes_meccs = ""
    # ha a félidő és a meccs nyertese nem ugyanaz és egyik sem üres, akkor
    if nyertes_felido != nyertes_meccs and nyertes_meccs != "" and nyertes_felido != "":
        print(f"{merkozes.idx} {nyertes_meccs}")

print("'B' megoldás")
for merkozes in merkozesek:
    # a gólkólönbségek előjelén alapuló megoldás: :
    # a két gólkülönbség szorzata csak akkor és csak akkor negatív, ha a félidőt és a meccset nem ugyanaz nyerte és nem is döntetlen
    if (merkozes.gol_felido_vendeg - merkozes.gol_felido_hazai) * (merkozes.gol_meccs_vendeg - merkozes.gol_meccs_hazai) < 0:
        if merkozes.gol_meccs_vendeg > merkozes.gol_meccs_hazai:
            nyertes = merkozes.csapat_vendeg
        else:
            nyertes = merkozes.csapat_hazai
        print(f"{merkozes.idx} {nyertes}")


# 4. Kérje be a felhasználótól egy csapat nevét, és tárolja el!
#   A következő két feladat megoldásához ezt a csapatnevet használja!
print("\n4.feladat")
csapat = input("Csapat neve = ")

# 5. Határozza meg, majd írja ki, hogy az adott csapat összesen hány gólt lőtt és hány gólt kapott!
#   Például: lőtt: 23 kapott: 12
print("\n5.feladat")
lott = 0
kapott = 0
for merkozes in merkozesek:
    if merkozes.csapat_vendeg.lower() == csapat.lower():
        lott += merkozes.gol_meccs_vendeg
        kapott += merkozes.gol_meccs_hazai
    elif merkozes.csapat_hazai.lower() == csapat.lower():
        lott += merkozes.gol_meccs_hazai
        kapott += merkozes.gol_meccs_vendeg
print(f"{csapat} lőtt: {lott:2} kapott: {kapott:2}")

# 6. Határozza meg, hogy az adott csapat otthon melyik fordulóban kapott ki először és melyik csapattól!
#   Ha egyszer sem kapott ki (ilyen csapat például a Bogarak), akkor „A csapat otthon veretlen maradt.” szöveget írja a képernyőre!
print("\n6.feladat")
i = 0
while i < len(merkozesek) and not(merkozesek[i].csapat_hazai.lower() == csapat.lower() and merkozesek[i].gol_meccs_hazai < merkozesek[i].gol_meccs_vendeg):
    i += 1
# meg kell nézni, hogy melyik feltétel miatt lépett ki a ciklusból
if i == len(merkozesek):
    print(f"A '{csapat}' csapat otthon veretlen maradt.")
else:
    print(f"A {csapat} a {merkozesek[i].fordulo}. fordulóban kapott ki először a {merkozesek[i].csapat_vendeg} csapattól")

# 7. Készítsen statisztikát, amely megadja, hogy az egyes végeredmények hány alkalommal fordultak elő!
#   Tekintse egyezőnek a fordított eredményeket (például 4-2 és 2-4)!
#   A nagyobb számot mindig előre írja! Az elkészült listát a stat.txt állományban helyezze el!
print("\n7.feladat")
# a mindkét gólérték egyjegyű, így a két számból képzett kétjegyű szám egyértelműen beazonosítja a végeredményt, így 100 (00..99) méretű lista elegendő
# pl 3-2 --> 32 vagy 2-4 --> 42
statisztika = [0 for i in range(0,100)]
for merkozes in merkozesek:
    if merkozes.gol_meccs_hazai > merkozes.gol_meccs_vendeg:
        veg = str(merkozes.gol_meccs_hazai) + str(merkozes.gol_meccs_vendeg)
    else:
        veg = str(merkozes.gol_meccs_vendeg) + str(merkozes.gol_meccs_hazai)
    statisztika[int(veg)] +=1

with open("stat.txt", "w") as fileKi:
    for i in range(0, 100):
        db = statisztika[i]
        if db > 0:
            # tizesek - egyesek : sb
            fileKi.write(f"{i // 10}-{i-10*(i // 10)}: {db:2} darab\n")
print("Adatok kiírva a 'stat.txt' állományba")
