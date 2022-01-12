### Emelt Informatika Érettségi - 2019 Május - Céges autók

#print('1.feladat')
adatok=[]
autok = [] # külön lista a 10 céges autó adatainak, amely elemei listák (az adott autó sorAdatai)
for k in range(0,10):
    autok.append([])

with open("autok.txt") as fileBe:
    for sor in fileBe:
        sorAdat = sor.strip().split(" ")
        # a 0, 1 értékeket lecseréljük "ki", "be" értékekre a könnyebb kezelhetőség kedvéért
        if(sorAdat[5] == "0"):
            sorAdat[5] = "ki"
        else:
            sorAdat[5] = "be" # bejövő autók listája
        # szótár létrehozása egy rekordhoz
        adat = {
            "idx": int(sorAdat[2][5:6]), # a rendszám utolsó karaktere az autok lista indexe
            "nap": sorAdat[0],
            "ido": sorAdat[1],
            "rsz": sorAdat[2],
            "dol": sorAdat[3],
            "km" : int(sorAdat[4]),
            "ki": sorAdat[5]
        }
        adatok.append(adat) # összes autó listája
        autok[adat["idx"]].append(adat) # a 10 auto szerint elkülönített listák
### beolvasás vége

print("2.feladat")
kiAuto = adatok[0]
for adat in adatok:
    if adat["ki"] == "ki":
      kiAuto =adat  
print("{}. nap rendszám: {}".format(kiAuto["nap"],kiAuto["rsz"]))

print("3.feladat")
benap = input("Nap: ")
print("Forgalom a(z) {}. napon ".format(benap))
for adat in adatok:
    if adat["nap"]==benap:
        print(adat["ido"],adat["rsz"],adat["dol"],adat["ki"])

print("4.feladat")
ki = 0
be = 0
for adat in adatok:
    if adat["ki"]== "ki":
        ki += 1
    else:
        be += 1
print("A hónap végén {} autót nem hoztak vissza.".format(ki-be))

print("5.feladat")
for auto in autok:
    print(auto[1]["rsz"],int(auto[-1]["km"])-int(auto[0]["km"]),' km')    

print("6.feladat")
maxKm = 0
maxDol = 0
for k in range(1,10):
    for auto in autok[k]:
        if auto["ki"] == "ki":
            aktKI = auto["km"]
        else:
            aktBE = auto["km"]
            tav = aktBE - aktKI
            if maxKm < tav:
                maxKm = tav
                maxDol = auto["dol"]
print("Leghosszabb út: {} km, személy: {}".format(maxKm, maxDol))

print("7.feladat")
rendBe = input("Rendszám: ")
ri = int(rendBe[5:6])
fileKi = open(rendBe+"_menetlevel.txt", "w")
kiNap = ""
kiIdo = ""
kiKm = ""

for auto in autok[ri]:
    if auto["ki"] == "be":
        fileKi.write("{}\t{}.\t{}\t{} km\t{}.\t{}\t{} km\n".format(auto["dol"], kiNap, kiIdo, kiKm, auto["nap"], auto["ido"], auto["km"])) 
    else:
        kiNap = auto["nap"]
        kiIdo = auto["ido"]
        kiKm = auto["km"]
# ha utoljára kiment, azt is ki kell írni
if auto["ki"] == "ki":
    fileKi.write("{}\t{}.\t{}\t{} km\n".format(auto["dol"], auto["nap"], auto["ido"], auto["km"])) 
print("Menetlevél kész.")
fileKi.close()
