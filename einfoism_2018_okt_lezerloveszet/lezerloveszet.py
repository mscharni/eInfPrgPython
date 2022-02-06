### Emelt Informatika Ismeretek Érettségi - 2018 Október - Lézerlövészet
import math

# 1. Feladat: Készítsen programot a következő feladatok megoldására, amelynek a forráskódját LezerLoveszet néven mentse el!


# 2. Feladat: Hozzon létre saját osztályt JatekosLovese azonosítóval és definiáljon benne adattagokat a játékos nevének és egy lövés koordinátáinak eltárolására!
#    A lövéseket sorszámmal kell majd ellátni, így ehhez is készítsen adattagot!
class JatekosLovese:
    # 3. Feladat: Készítse el az osztály konstruktorát, ami a forrásállomány egy sora alapján rögzíti a játékos nevét, a lövés koordinátáit és a lövés sorszámát.
    #    A forrásállomány egy sora és a lövés sorszáma legyenek a konstruktor paraméterei!
    def __init__(self, sor, idx):
        sor = sor.split(";")
        self.Sorszam = idx
        self.Jatekos = sor[0]
        self.X = float(sor[1].replace(',','.'))
        self.Y = float(sor[2].replace(',','.'))
        self.Tavolsag = self.getTavolsag()
        self.Pontszam = self.getPontszam()
    
    # 6. Feladat: Készítsen Tavolsag azonosítóval valós típusú kódtagot (jellemzőt, metódust, stb.) a JatekosLovese osztályban, mellyel meghatározza a céltábla koordinátái és a lövés koordinátái közötti távolságot
    def getTavolsag(self):
        global CX, CY
        # megadott algoritmus (Pithagoras-tétel)
        dx = CX - self.X
        dy = CY - self.Y
        return math.sqrt(dx*dx + dy*dy)

    # 8. Feladat: Készítsen Pontszam azonosítóval valós típusú kódtagot (jellemzőt, metódust, stb.) a JatekosLovese osztályban, mellyel meghatározza egy-egy lövés pontszámát!
    #    A pontszámot a 10 - Tavolsag képlettel határozza meg! A pontszámot két tizedesjegyre kell a kódtagnak kerekítenie!
    #    Negatív pontszám nem lehet, ilyenkor a kódtag nulla értékkel térjen vissza!
    def getPontszam(self):
        return int(100*(10 - self.Tavolsag))/100 if self.Tavolsag < 10 else 0
        
    
# 4. feladat: Olvassa be a lovesek.txt állományban található adatokat és tárolja el őket!
#    A játékosok lövéseit tárolja tömbben vagy listában, melynek a típusa JatekosLovese legyen!
lovesek = []
with open("lovesek.txt", "r") as file:
    celtabla = file.readline().strip().split(';')
    CX = float(celtabla[0].replace(',','.'))
    CY = float(celtabla[1].replace(',','.'))
    idx = 1
    for line in file:
        lovesek.append(JatekosLovese(line, idx))
        idx += 1

# 5. feladat: Határozza meg és írja ki a minta szerint, hogy a játékosok hány lövést adtak le a játék során!
print(f"\n5. feladat: lövések száma:{len(lovesek)}")

# 7. Feladat: Határozza meg a céltábla középpontjához legközelebb eső (legpontosabb) lövés adatait és írja ki a minta szerint! Feltételezheti, hogy csak egy ilyen lövés van!
print("\n7. feladat: Legpontosabb lövés:")
pontos_loves = lovesek[0]
for loves in lovesek:
    if pontos_loves.Tavolsag > loves.Tavolsag:
        pontos_loves = loves
print(f"{pontos_loves.Sorszam}.; {pontos_loves.Jatekos}; x={pontos_loves.X}; y= {pontos_loves.Y}; távolság={pontos_loves.Tavolsag}")

# 9. Feladat: Határozza meg és írja ki a minta szerint a nulla pontos lövések számát!
nulla_pontos = 0
for loves in lovesek:
    if loves.Pontszam == 0:
        nulla_pontos += 1
print(f"\n9. feladat: Nulla pontos lövések száma: {nulla_pontos} db")

# 10. Feladat: Számolja meg és írja ki a képernyőre a játékban részvevő játékosok számát a minta szerint!
jatekosok = []
for loves in lovesek:
    if loves.Jatekos not in jatekosok:
        jatekosok.append(loves.Jatekos)
print(f"\n10. feladat: Játékosok száma: {len(jatekosok)}")

# 11. Feladat: Határozza meg játékosonként a leadott lövések számát! Megoldását úgy készítse el, hogy a játékosok nevei és száma nem ismert, de feltételezheti, hogy a számuk 2 és 10 fő közötti!
jatekos_lovesek = [0 for i in range(0, len(jatekosok))]
for loves in lovesek:
    idx = jatekosok.index(loves.Jatekos)
    jatekos_lovesek[idx] += 1
print("\n11. feladat: Lövések száma")
for i in range(0, len(jatekosok)):
    print(f"{jatekosok[i]} - {jatekos_lovesek[i]} db")

# 12. Feladat: Számítsa ki az átlagpontszámokat, majd jelenítse meg a minta szerint!
jatekos_pontok = [0 for i in range(0, len(jatekosok))]
for loves in lovesek:
    idx = jatekosok.index(loves.Jatekos)
    jatekos_pontok[idx] += loves.Pontszam
print("\n12. feladat: Átlagpontszámok")
for i in range(0, len(jatekosok)):
    print(f"{jatekosok[i]} - {jatekos_pontok[i] / jatekos_lovesek[i]}")


# 13. Feladat: Határozza meg a legmagasabb átlagpontszám alapján a nyertes játékos nevét! Feltételezheti, hogy nem alakult ki holtverseny.
maxi = 0
for i in range(1, len(jatekosok)):
    if jatekos_pontok[maxi] / jatekos_lovesek[maxi] < jatekos_pontok[i] / jatekos_lovesek[i]:
        maxi = i
print(f"\n13. feladat: A játék nyertese: {jatekosok[maxi]}")
