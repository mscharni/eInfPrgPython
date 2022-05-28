# 1. feladat
sorok = []
with open("utca.txt") as fileBe:
    for sor in fileBe:
        sorok.append(sor.strip())
adosavszorzo = [int(i) for i in sorok[0].split()]
print(adosavszorzo)
sorok.remove(sorok[0])
adatok = []
for sor in sorok:
    adatsor = sor.split(" ")
    adatok.append([adatsor[0], adatsor[1], adatsor[2], adatsor[3], int(adatsor[4])])

# 2. feladat
print(f"2. feladat. A mintában {len(adatok)} telek szerepel")

# 3. feladat
# adoszam = input("3. feladat. Egy tulajdonos adószáma:")
adoszam = "68396"
nincs = True
for sor in adatok:
    if sor[0] == adoszam:
        nincs = False
        print(f"{sor[1]} utca {sor[2]}")
if nincs:
    print("Nem szerepel az adatállományban")

# 4. feladat
adosavok = {
    "A" : adosavszorzo[0],
    "B" : adosavszorzo[1],
    "C" : adosavszorzo[2]
}
def ado(adosav, alapterulet):
    adoosszeg = adosavok[adosav]*alapterulet
    if adoosszeg < 10000:
        adoosszeg = 0
    return adoosszeg

# 5. feladat
print("5. feladat")
adosavszum = {
    "A": {
        "db":0,
        "sum":0
    },
    "B": {
        "db":0,
        "sum":0
    },
    "C": {
        "db":0,
        "sum":0
    }
}
for adat in adatok:
    adosavszum[adat[3]]["db"] += 1
    adosavszum[adat[3]]["sum"] += ado(adat[3], adat[4])
print(f"A sávba {adosavszum['A']['db']} telek esik, az adó {adosavszum['A']['sum']} Ft.")
print(f"B sávba {adosavszum['B']['db']} telek esik, az adó {adosavszum['B']['sum']} Ft.")
print(f"C sávba {adosavszum['C']['db']} telek esik, az adó {adosavszum['C']['sum']} Ft.")

# 6. feladat
print("6. feladat: A több sávba sorolt utcák:")
utcak = {}
for adat in adatok:
    if adat[1] not in utcak.keys():
        utcak.update({adat[1]: [adat[3]]})
    else:
        if adat[3] not in utcak[adat[1]]:
            utcak[adat[1]].append(adat[3])

for utca in utcak:
    if len(utcak[utca])>1 :
        print(utca)

# 7. feladat
adozok = {}
for adat in adatok:
    if adat[0] not in adozok.keys():
        adozok.update({adat[0]: ado(adat[3], adat[4])})
    else:
        adozok[adat[0]] += ado(adat[3], adat[4])
print(adozok)
with open("fizetendo.txt", "w") as fileKi:
    for adozo in adozok:
        print(adozo, adozok[adozo], file=fileKi)