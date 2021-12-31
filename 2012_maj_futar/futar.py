class Fuvar:
     def __init__(self, line):
        global heti_fizetes
        datas = line.strip().split(" ")
        self.nap = int(datas[0])                # 1..7
        self.fszam = int(datas[1])              # 1..40
        self.tav = int(datas[2])                # 1..30
        self.fizu = fizetes(self.tav)           # egyből kiszámoljuk az adott útért járó fizettséget
        napi_ossztav[self.nap] += self.tav      # egyből összegezzük a napi megtett távolságot
        napi_osszfuvar[self.nap] += 1           # egyből összegezzük a napi fuvarok számát
        heti_fizetes += self.fizu               # egyből összegezzük a heti fizetést

# Fuvarok rendezése nap és azon belül a fuvarszám szerint: a két értékből egy közös értéket generálunk, ami a rendezés alapja lesz:
def sortFutar(futar):
    return futar.nap*100 + futar.fszam

# a távolság függvényében történő fizetés függvénye
def fizetes(tav):
    if tav <= 2:
        penz = 500
    elif tav <= 5:
        penz = 700
    elif tav <= 10:
        penz = 900
    elif tav <= 20:
        penz = 1400
    else:
        penz = 2000
    return penz

fuvarok = []
napi_ossztav = [0 for i in range(0,8)]         # a nulladik indexű elemet nem fogjuk használni
napi_osszfuvar = [0 for i in range(0,8)]       # a nulladik indexű elemet nem fogjuk használni
heti_fizetes = 0

# 1. Olvassa be a tavok.txt állományban talált adatokat, s annak felhasználásával oldja meg a következő feladatokat!
print("\n1. feladat")
with open("tavok.txt", "r") as file:
    for line in file:
        fuvar = Fuvar(line)
        fuvarok.append(fuvar)
# a további feladatok megoldásához érdemes rendezni az adatokat nap és azon belül futárszám szerint
fuvarok.sort(key=sortFutar)

# 2. Írja ki a képernyőre, hogy mekkora volt a hét legelső útja kilométerben!
#   Figyeljen arra, hogy olyan állomány esetén is helyes értéket adjon, amiben például a hét első napján a futár nem dolgozott!
print("\n2. feladat")
print(f"A hét legelső útja {fuvarok[0].tav} km hoszú volt.")

# 3. Írja ki a képernyőre, hogy mekkora volt a hét utolsó útja kilométerben!
print("\n3. feladat")
print(f"A hét legutolsó útja {fuvarok[-1].tav} km hosszú volt.")

# 4. Tudjuk, hogy a futár minden héten tart legalább egy szabadnapot.
#   Írja ki a képernyőre, hogy a hét hányadik napjain nem dolgozott a futár!
print("\n4. feladat")
# megkeressük, hogy melyik nap tett meg nulla kilométert
szabadnapok = ""
for i in range(1,8):
    if napi_ossztav[i] == 0:
        szabadnapok += str(i) + "., "
szabadnapok = szabadnapok[:-2]
print(f"A futár a(z) {szabadnapok} napo(ko)n tartott szabadnapo(ka)t")

# 5. Írja ki a képernyőre, hogy a hét melyik napján volt a legtöbb fuvar!
#   Amennyiben több nap is azonos, maximális számú fuvar volt, elegendő ezek egyikét kiírnia.
print("\n5. feladat")
# megkeressük a legtöbb fuvart tartalmazó napot
max_fuvar_napja = 1
for i in range(2, 8):
    if napi_osszfuvar[i] > napi_osszfuvar[max_fuvar_napja]:
        max_fuvar_napja = i
print(f"A hét {max_fuvar_napja} napján volt a legtöbb fuvar.")

# 6. Számítsa ki és írja a képernyőre a mintának megfelelően, hogy az egyes napokon hány kilométert kellett tekerni!
print("\n6. feladat")
for i in range(1,8):
    print(f"{i}. nap: {napi_ossztav[i]:3} km")

# 7. A futár az egyes utakra az út hosszától függően kap fizetést.
#   Kérjen be a felhasználótól egy tetszőleges távolságot, és határozza meg, hogy mekkora díjazás jár érte! Ezt írja a képernyőre!
print("\n7. feladat")
tav = int(input("Adja meg a távolságot [1..30]= "))
print(f"A {tav} km hosszú útra {fizetes(tav)} Ft a fizetség.")

# 8. Határozza meg az összes rögzített út ellenértékét!
#   Ezeket az értékeket írja ki a dijazas.txt állományba nap szerint, azon belül pedig az út sorszáma szerinti növekvő sorrendben
print("\n8. feladat")
with open("dijazas.txt", "w") as file:
    for fuvar in fuvarok:
        file.writelines(f"{fuvar.nap}. nap {fuvar.fszam}. út: {fuvar.fizu} Ft")

# 9. Határozza meg, és írja ki a képernyőre, hogy a futár mekkora összeget kap a heti munkájáért!
print("\n9. feladat")
print(f"A futár {heti_fizetes:,}Ft fizetést kap a heti munkájáért!".replace(',', ' '))
