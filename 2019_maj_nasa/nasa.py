### Emelt Informatika Ismeretek Érettségi - 2019 Május - NASA

# 1. Feladat: Készítsen programot a következő feladatok megoldására, amelynek a forráskódját NASA néven mentse el!

# 2. Feladat: Hozzon létre saját osztályt Keres azonosítóval és definiáljon benne öt szöveges típusú adattagot, amelyben az egy kéréshez kapcsolódó adatokat tudja majd eltárolni!

class Keres:
    # 3. Feladat: Készítse el az osztály konstruktorát, ami a következő feladatokat hajtja végre!
    #    − Beállítja az ügyfél címét.
    #    − Beállítja a kérés idejét (dátum és idő).
    #    − Beállítja a GET paranccsal kezdődő kérést.
    #    − Beállítja a kéréshez tartozó állapotkódot.
    #    − Beállítja az elküldött JPG fájl méretét.
    #    Például:
    #    Cim: „204.239.210.188”
    #    DatumIdo: „20/Jul/1995:00:00:00”
    #    Get: „GET /shuttle/countdown/count70.jpg”
    #    HttpKod: „200”
    #    Meret: „46573”
    def __init__(self, line):
        global numbers
        datas = line.split("*")
        self.Cim = datas[0]
        self.DatumIdo = datas[1]
        self.Get = datas[2]
        datas = datas[3].split(" ")
        self.HttpKod = datas[0] 
        self.Meret = datas[1]
        # 6/A. Feladat: Készítsen 32 bites egész típusú jellemzőt vagy metódust (függvényt) ByteMeret azonosítóval a saját osztályában, amely a szöveges típusban tárolt elküldött válasz méretét szám típusúra alakítja át!
        #      Ügyeljen arra, hogy ha a válasznak nem volt mérete, akkor ott „-” szerepel, ami 0 bájtot jelent!
        self.ByteMeret = int(self.Meret) if self.Meret != "-" else 0
        # 7. Feladat: Készítsen logikai típusú jellemzőt vagy metódust (függvényt) Domain azonosítóval a saját osztályában, mely segítségével eldönti az ügyfél címéről, hogy az rendelkezett-e domain névvel!
        #    Domain névvel rendelkező címnek tekintheti azokat a címeket, amelyek utolsó karaktere nem számjegy.
        self.Domain = True if self.Cim[-1] not in numbers else False


#    számjegyek listája a 7-es feladathoz
numbers = [str(i) for i in range(0,10)]

# 4. Feladat: Olvassa be a NASAlog.txt állomány sorait, és hozzon létre osztálypéldányt (objektumot) minden egyes kéréshez és a példányokat egy összetett adatszerkezetben (pl. vektor, lista stb.) tárolja!
keresek = []
with open("NASAlog.txt", "r") as file:
    for line in file:
        keres = Keres(line.strip())
        keresek.append(keres)


# 5. Feladat: Határozza meg és írja ki a képernyőre a minta szerint, hogy hány kérés található a NASAlog.txt állományban!
print(f"\n5. feladat: Kérések száma: {len(keresek)}")


# 6/B. Feladat: Határozza meg és írja ki a képernyőre a minta szerint a kérésekre küldött válaszok összes méretét bájtban!
ossz_meret = 0
for keres in keresek:
    ossz_meret += keres.ByteMeret    
print(f"\n6. feladat: Válaszok összes mérete: {ossz_meret} byte")


# 8. Feladat: Határozza meg a NASAlog.txt állomány adatai alapján, hogy a kéréseknél milyen arányban rendelkezett az ügyfél címe domain névvel az összes kérésszámhoz viszonyítva! Az eredményt a minta szerint írja ki a képernyőre!
ossz_domain = 0
for keres in keresek:
    ossz_domain += 1 if keres.Domain else 0    
print(f"\n8. feladat: Domain-es késérek: {ossz_domain/len(keresek):.2%}")

# 9. Feladat: Készítsen statisztikát a NASAlog.txt állomány adatai alapján amely megadja, hogy az egyes állapotkódok hányszor fordultak elő!
#    A statisztika eredményét a minta szerint jelenítse meg a képernyőn! Megoldását úgy készítse el, hogy az egy tetszőlegesen megadott állományban előforduló állapotkódokat is fel tudja dolgozni!
kodok = []
kodok_db = []
for keres in keresek:
    if keres.HttpKod in kodok:
        idx = kodok.index(keres.HttpKod)
        kodok_db[idx] += 1
    else:
        kodok.append(keres.HttpKod)
        kodok_db.append(1)
print(f"\n9. feladat: Statisztika:")
for i in range(0, len(kodok)):
    print(f"{kodok[i]}: {kodok_db[i]} db")
