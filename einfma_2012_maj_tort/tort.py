### Emelt Informatika Alapismertek - 2012 Május - Tört

# 1. Feladat: Kérjen be a felhasználótól két számot, amely egy közönséges tört számlálója és nevezője! 
#    Döntse el, hogy az így bevitt tört felírható-e egész számként! Ha igen, írja ki értékét egész számként, ha nem, írja ki „Nem egész”!
print("Egyik tört")
a = int(input("Számlálója = "))
b = int(input("Nevezője ="))
if a/b == a // b :
    print(f"{a} / {b} = {a//b}")
else:
    print("Nem egész!")


# 2. feladat: A közönséges törteket úgy tudjuk a legegyszerűbb alakra hozni, ha a számlálóját és nevezőjét elosztjuk a két szám legnagyobb közös osztójával, és az így kapott érték lesz az új számláló, illetve nevező.
#    Az egyszerűsítéshez készítsen egy rekurzív függvényt az  alább leírt euklideszi algoritmusnak megfelelően!
def lnko(a, b):
 if a==b:
     return a
 if a<b:
     return lnko(a, b-a) 
 if a>b:
     return lnko(a-b, b) 


# 3. feladat: Az első feladatban bekért törtet hozza a legegyszerűbb alakra a létrehozott függvény segítségével!
#    Amennyiben nem sikerül az előírt függvényt elkészítenie, alkalmazhat más megoldást, hogy a további feladatokat meg tudja oldani.
#    Az eredményt írja ki a következő formában: 24/32 = 3/4
#    Amennyiben a tört felírható egész számként, akkor ebben az alakban jelenjen meg: 24/6 = 4
if a/b == a // b :
    print(f"{a} / {b} = {a//b}")
else:
    ko = lnko(a,b)
    print(f"{a} / {b} = {a//ko} / {b//ko}")

# 4. feladat: Két törtet úgy tudunk összeszorozni, hogy a két tört számlálóját összeszorozva kapjuk az eredmény számlálóját, és a két tört nevezőjét összeszorozva kapjuk az eredmény nevezőjét.
#    Kérjen be a felhasználótól egy újabb közönséges törtet a számlálójával és a nevezőjével! Szorozza meg ezzel a törttel az első feladatban bekért törtet!
#    Az eredményt hozza a legegyszerűbb alakra, és ezt írja ki a következő formában: 24/32 * 12/15 = 288/480 = 3/5
print("Másik tört")
c = int(input("Számlálója = "))
d = int(input("Nevezője ="))

def osszeszoroz(a,b,c,d):
    e = a*c
    f = b*d
    if e/f == e // f :
        return f"{a}/{b} * {c}/{d} = {e}/{f} = {e//f}"
    else:
        ko = lnko(e,f)
        return f"{a}/{b} * {c}/{d} = {e}/{f} = {e//ko} / {f//ko}"
print(osszeszoroz(a,b,c,d))

# 5. feladat: Két közönséges tört összeadásához a következő lépésekre van szükség: 
#    • Mindkét számot bővíteni kell, azaz mind a számlálóját, mind a nevezőjét ugyanazzal a számmal kell megszorozni.
#      Ezt a bővítést úgy célszerű elvégezni, hogy a közös nevező a két eredeti nevező legkisebb közös többszöröse legyen.
#      Ez lesz az összeg nevezője. 
#    • A két bővített alakú tört számlálóját összeadjuk, ez lesz az eredmény számlálója. 
#      Ehhez készítsen függvényt az alábbiakban leírtak szerint – a korábban elkészített lnko függvény felhasználásával – a legkisebb közös többszörös meghatározására!
def lkkt(a, b):
    return a * b // lnko(a, b)


# 6. feladat: A függvény segítségével határozza meg a két bekért tört összegét, és ezt adja meg a következő formában!
#    (Amennyiben nem sikerül az előírt függvényt elkészítenie, alkalmazhat más megoldást, hogy a további feladatokat meg tudja oldani.) 
#    24/32 + 8/3 = 72/96 + 256/96 = 328/96 = 41/12
#    Amennyiben az eredmény felírható egész számként, akkor ebben az alakban jelenjen meg: 
#    22/4 + 27/6 = 66/12 + 54/12 = 120/12 = 10
def osszead(a,b,c,d):
    f = lkkt(b,d)
    e = a* f//b + c * f//d
    if e/f == e // f :
        return f"{a}/{b} + {c}/{d} = {a*f//b}/{f} + {c*f//d}/{f} =  {a*f//b + c*f//d} / {f} = {e//f}"
    else:
        ko = lnko(e,f)
        return f"{a}/{b} + {c}/{d} = {a*f//b}/{f} + {c*f//d}/{f} = {a*f//b + c*f//d} / {f} = {e//ko} / {f//ko}"
    
print(osszead(a,b,c,d))

# 7. feladat: Az adat.txt állományban található műveleteket végezze el, és az eredményeket a korábbi, képernyőre kiírt formátumnak megfelelően írja az eredmeny.txt állományba!
#    Az adat.txt fájlnak legfeljebb 100 sora lehet; soronként 4 számot és egy műveleti jelet tartalmaz, melyeket mindenhol egy szóköz választ el egymástól.
#    Műveleti jelként csak összeadás és szorzás szerepel.
with open("adat.txt", "r") as file:
    lines = file.readlines()
with open("eredmeny.txt", "w") as file:
    for line in lines:
        datas = line.strip().split(" ")
        a = int(datas[0])
        b = int(datas[1])
        c = int(datas[2])
        d = int(datas[3])
        m = datas[4]
        if m == "+":
            file.write(osszead(a,b,c,d))
        else:
            file.write(osszeszoroz(a,b,c,d))
        file.write('\n')