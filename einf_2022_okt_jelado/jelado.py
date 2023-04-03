import math

# 1. Feladat
file = open("jel.txt",'r')
jelek =[]
db = 0
for sor in file:
    adatokS = sor.strip().split(" ")
    adatok = []
    for adatS in adatokS:
        adatok.append(int(adatS))
    jelek.append(adatok)
    db +=1
print(db)

# 2. feladat
print("2. feladat")
sorsz = int(input("Adja meg a jel sorszámát! "))
x = jelek[sorsz-1][3]
y = jelek[sorsz-1][4]
print(f"x={x} y={y}")

# 3. feladat
def eltelt(o1,p1,m1,o2,p2,m2):
    mp1 = o1 * 3600 + p1 * 60 + m1
    mp2 = o2 * 3600 + p2 * 60 + m2
    return mp2-mp1

print()
# 4. feladat
print("4. feladat")
o1 = jelek[0][0] # első adatsor óra értéke
p1 = jelek[0][1] # első adatsor perc értéke
m1 = jelek[0][2] # első adatsor másodperc értéke
o2 = jelek[-1][0] # utolsó adatsor óra értéke
p2 = jelek[-1][1] # utolsó adatsor perc értéke
m2 = jelek[-1][2] # utolsó adatsor másodperc értéke
ido = eltelt(o1,p1,m1,o2,p2,m2)
o3 = ido // 3600
p3 = (ido - o3*3600) // 60
m3 = ido-o3*3600 - p3*60
print(f"Időtartam: {o3}:{p3}:{m3}")

print()
# 5. feladat
print("5. feladat")
minx = jelek[0][3]
miny = jelek[0][4]
maxx = jelek[0][3]
maxy = jelek[0][4]
for jel in jelek:
    # legkisebb x
    if jel[3] < minx:
        minx = jel[3]
    # legkisebb y
    if jel[4] < miny:
        miny = jel[4]
    # legnagyobb x
    if jel[3] > maxx:
        maxx = jel[3]
    # legnagyobb y
    if jel[4] > maxy:
        maxy = jel[4]
print(f"Bal alsó: {minx} {miny}, jobb felső: {maxx} {maxy}")        

print()
# 6. feladat
print("6. feladat")
ossz = 0
for i in range(0, len(jelek)-1):
    ossz += math.sqrt((jelek[i][3]-jelek[i+1][3])**2 + (jelek[i][4]-jelek[i+1][4])**2)
print(f"Elmozdulás: {ossz:.3f} egység")    




