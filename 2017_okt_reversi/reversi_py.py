### Emelt Informatika Ismeretek Érettségi - 2017 Október - Reversi

# 1. Feladat: Készítsen programot a következő feladatok megoldására, amelyeknek a forráskódját reversi néven mentse el!

# 2. Feladat: Hozzon létre saját osztályt Tabla azonosítóval és definiáljon benne egy karaktertípusú mátrixot (kétdimenziós tömböt) „t” azonosítóval, amelyben egy játék pillanatnyi állását tudja majd tárolni!
#    A mátrix sorait és oszlopait 0-tól 7-ig indexelje!

# 3. feladat: Készítse el az osztály konstruktorát, ami a következő feladatokat hajtja végre:
#    a. Inicializálja a „t” mátrixot 8×8-as mérettel.
#    b. Feltölti a „t” mátrixot a „#”, „K” és „F” karakterekkel egy szöveges állományból.
#       A feldolgozandó szöveges fájl nevét a konstruktor paramétereként adjuk át!
#       A feladat megoldásához használandó allas.txt állomány 8 sora, soronként 8 karakterrel tárolja a játék állását.
#       A tábla üres mezőit a „#” karakter, a játékosok korongjait a „K” (kék) és „F” (fehér) karakterek kódolják.

class Tabla:
    def __init__(self, filename):
        # ez valójában felesleges, de a 2. feladat ezt írja elő...
        self.t = [['' for i in range(0,8)] for j in range(0,8)]
        with open(filename, "r") as fileBe:
            for i in range(0,8):
                line = fileBe.readline().strip()
                for j in range(0,8):
                    self.t[i][j] = line[j]
    # 5. Feladat: Készítsen a Tabla osztályba Megjelenit azonosítóval metódust, ami a minta szerint megjeleníti a „t” mátrixban eltárolt játék állását!
    def Megjelenit(self, offset):
        for i in range(0,8):
            line = " "*offset
            for j in range(0,8):
                line += self.t[i][j]
            print(line)
        
    # 6. feladat: Készítsen a játék állásáról összegzést a minta szerint!
    # Az egyes karakterek („#”, „K”, „F”) megszámlálását a Tabla osztályban definiált paraméterezhető metódus segítségével végezze!
    def Megszamlal(self, figura):
        fig_db = 0
        for i in range(0,8):
            for j in range(0,8):
                if self.t[i][j] == figura:
                    fig_db +=1
        return fig_db

    # 7. feladat: Definiáljon a Tabla osztályban metódust VanForditas néven a következő algoritmus kódolásával!
    def VanForditas(self, jatekos, sor, oszlop, iranySor, iranyOszlop):
        aktSor = sor + iranySor
        aktOszlop = oszlop + iranyOszlop
        ellenfel = 'K'
        if jatekos == 'K':
            ellenfel = 'F'
        nincsEllenfel = True
        while aktSor > 0 and aktSor < 8 and aktOszlop > 0 and aktOszlop < 8 and self.t[aktSor][aktOszlop] == ellenfel:
            aktSor = aktSor + iranySor
            aktOszlop = aktOszlop + iranyOszlop
            nincsEllenfel = False
        if nincsEllenfel or aktSor < 0 or aktSor > 7 or aktOszlop < 0 or aktOszlop > 7 or self.t[aktSor][aktOszlop] != jatekos:
            return False
        return True


# 4. feladat: Hozzon létre egy Tabla típusú osztálypéldányt (objektumot), melynek a konstruktora az allas.txt forrásállomány nevét kapja aktuális paraméterként feldolgozásra!
myt = Tabla("allas.txt")

# 5. Feladat: Készítsen a Tabla osztályba Megjelenit azonosítóval metódust, ami a minta szerint megjeleníti a „t” mátrixban eltárolt játék állását!
print("\n5. feladat: A betöltött tábla")
myt.Megjelenit(7)

# 6. feladat: Készítsen a játék állásáról összegzést a minta szerint!
# Az egyes karakterek („#”, „K”, „F”) megszámlálását a Tabla osztályban definiált paraméterezhető metódus segítségével végezze!
print("\n6. feladat: Összegzés")
print(f"Kék korongok száma: {myt.Megszamlal('K')}")
print(f"Fehér korongok száma: {myt.Megszamlal('F')}")
print(f"Üres mezők száma: {myt.Megszamlal('#')}")
