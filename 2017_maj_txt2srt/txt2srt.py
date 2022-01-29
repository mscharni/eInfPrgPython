### Emelt Informatika Ismeretek Érettségi - 2017 Május - Txt2Srt

# 1. Készítsen programot a következő feladatok megoldására, amelynek a forráskódját txt2srt néven mentse el!


# 2. feladat: Hozzon létre saját osztályt IdozitettFelirat azonosítóval és definiáljon benne két szöveg típusú adattagot, melyben egy felirat időzítését és magát a feliratot tudja majd tárolni! 
class IdozitettFelirat:

    # 3. feladat: Készítse el az osztály konstruktorát, ami a következő feladatokat hajtja végre! 
    #    a. Beállítja az időzítést tároló adattag értékét a konstruktor paraméterében megadott értékkel. 
    #    b. Beállítja a felirat szövegét tároló adattag értékét a konstruktor paraméterében megadott értékkel.
    def __init__(self, idozites, felirat):
        self.idozites = idozites
        self.felirat = felirat
        # 6. feladat: Készítsen az IdozitettFelirat osztályban jellemzőt vagy metódust SzavakSzama azonosítóval!
        #    A létrehozott jellemző vagy metódus segítségével határozza meg az időzített felirat szavainak a számát!
        self.SzavakSzama = self.felirat.count(" ")
        # 8. feladat: Készítsen az IdozitettFelirat osztályban jellemzőt vagy metódust SrtIdozites azonosítóval!
        #    A létrehozott jellemző vagy metódus az időzítéshez tartozó adattag értékét alakítsa át az SRT formátumnak megfelelően!
        #    A SRT formátumot a következő minta és a leírás alapján készítse el! 
        #    Időzítés: „00:01 - 00:03”
        #    SRT időzítés: „00:00:01 --> 00:00:03”
        self.SrtIdozites = self.IdozitesToSrtIdozites(self.idozites)
        
    def IdozitesToSrtIdozites(self, idozites):
        k_ora = int(idozites[0:2]) // 60
        k_prc = int(idozites[0:2]) - k_ora*60
        k_mp = idozites[3:5]
        v_ora = int(idozites[8:10]) // 60
        v_prc = int(idozites[8:10]) - v_ora*60
        v_mp = idozites[11:13]
        
        # to string
        k_ora = "0" + str(k_ora) if k_ora < 10 else str(k_ora)
        k_prc = "0" + str(k_prc) if k_prc < 10 else str(k_prc)
        v_ora = "0" + str(v_ora) if v_ora < 10 else str(v_ora)
        v_prc = "0" + str(v_prc) if v_prc < 10 else str(v_prc)
        
        srt_idozites = f"{k_ora}:{k_prc}:{k_mp} --> {v_ora}:{v_prc}:{v_mp}"
        return srt_idozites


feliratok = []

# 4. feladat: Olvassa be a feliratok.txt állomány sorait és hozzon létre osztálypéldányt (objektumot) minden egyes időzítés−felirat párhoz! 
with open("feliratok.txt") as fileBe:
    lines = fileBe.readlines()
for i in range(0, len(lines), 2):
    felirat = IdozitettFelirat(lines[i].strip(), lines[i+1].strip())
    feliratok.append(felirat)
    

# 5. feladat: . Határozza meg és írja ki a képernyőre a minta szerint, hogy hány felirat van a feliratok.txt állományban! 
print(f"5. feladat - feliratok száma: {len(feliratok)}")

# 7. feladat: Határozza meg és írja ki a legtöbb szóból álló feliratot!
#    Feltételezheti, hogy a feliratfájlban csak egy ilyen felirat van. Az eredményt a minta szerint jelenítse meg a képernyőn!
print("\n7. feladat - legtöbb szóból álló felirat")
max_felirat = feliratok[0]
for felirat in feliratok:
    if felirat.SzavakSzama > max_felirat.SzavakSzama:
        max_felirat = felirat
print(f"{max_felirat.felirat}")


# 9. feladat: Készítse el a felirat.srt állományt a minta szerint!
#    Az állományba kerüljön bele a felirat száma (a számozás 1-től kezdődik), az SRT időzítése és a felirat szövege!
#    A feliratokat egy-egy üres sor válassza el egymástól!

with open("felirat.srt", "w") as fileKi:
    sorszam = 1
    for felirat in feliratok:
        fileKi.write(f"{sorszam}\n")
        fileKi.write(f"{felirat.SrtIdozites}\n")
        fileKi.write(f"{felirat.felirat}\n")
        fileKi.write("\n")
        sorszam +=1
        
        