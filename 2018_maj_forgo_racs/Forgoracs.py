# 1. feladat: Készítsen programot a következő feladatok megoldására, amelynek a forráskódját Forgoracs néven mentse el!

# 2. feladat: Hozzon létre saját osztályt Fracs azonosítóval és definiáljon benne két karakter típusú mátrixot (kétdimenziós tömböt) Kodlemez és Titkositott azonosítóval,
#    illetve egy karakterlánc típusú, csak olvasható jellemzőt Titkositando azonosítóval melyekben az adatokat tudja a feladat megoldása során tárolni!
#    A mátrixok sorai és oszlopai 0-tól 7-ig legyenek indexelve!

class Fracs:
    # 3. feladat: Készítse el az osztály kétparaméteres konstruktorát, ami a következő feladatokat hajtja végre:
    def __init__(self, filename, secret):
        # 3./a. Inicializálja a Kodlemez és Titkositott mátrixokat 8×8-as mérettel!
        self.Kodlemez = [['' for i in range(0,8)] for j in range(0,8)]
        self.Titkositott = [['' for i in range(0,8)] for j in range(0,8)]
        self.feltolt(filename)
        # 3./d. A Titkositando változó értékét átalakítja az Atalakit() metódus (függvény) hívásával, mely működését a következő (4.) feladatban írtuk le!
        # TODO: Két lépes (egy felesleges értékadás) ahelyett, hogy egyből az átalakított értéket raknánk a tulajdonságba, pl:
        # self._Titkositando = self.Atalakit(secret)
        self._Titkositando = secret
        self.Atalakit()

    
    # 2.b. csak olvasható tulajdonság
    @property
    def Titkositando(self):
        return self._Titkositando

    # 3./b. Feltölti a Kodlemez mátrixot a „#” és „A” karakterekkel egy szöveges állományból.
    #       A feldolgozandó szövegesfájl nevét a konstruktor paramétereként adjuk át!
    #       A feladat megoldásához használandó kodlemez.txt állomány 8 sora, soronként 8 karakterrel tárolja a kódlemez felépítését.
    #       A kódlemez „ablakait” az „A” karakterekkel jelöltük. Ahol nincs ablak, ott a „#” karakter szerepel a fájlban.
    def feltolt(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()
        for i in range(0,8):
            for j in range(0,8):
                self.Kodlemez[i][j] = lines[i][j]
    
    # 3./c. A Titkositando azonosítójú karakterlánc típusú változó értékét meghatározza a konstruktor másik paraméterében megadott paraméterrel!
    @Titkositando.setter
    def Titkositando(self, secret):
        self._Titkositando = secret
        # TODO: Valójában teljesen felesleges feltölteni az átadott paraméter értékével, mert utána egyből át kell alakítani, meg lehetne csinálni egy lépésben is...
        
    # 4. feladat: Hozzon létre az Fracs osztályban Atalakit() azonosítóval metódust, ami a következő feladatokat hajtja végre:
    #    a. A Titkositando változóból törli a szóközöket, pontokat és vesszőket!
    #    b. Kivételt dob „Túl hosszú a titkosítandó szöveg!” üzenettel, ha a törlések után a szöveg hossza nagyobb, mint 64 karakter!
    #    c. A Titkositando változó étékét jobbról „X” karakterekkel tölti fel úgy, hogy a titkosítandó szöveg hossza pontosan 64 karakter legyen!
    def Atalakit(self):
        self._Titkositando = self._Titkositando.replace(' ', '').replace('.', '').replace(',', '')
        if len(self._Titkositando) > 64:
            raise Exception("Túl hosszú a titkosítandó szöveg!")
        self._Titkositando = self._Titkositando + "X"*(64-len(self._Titkositando))


    # 7. feladat / A: Készítsen az Fracs osztályba KiirKodlemez azonosítóval metódust, ami a minta szerint megjeleníti a Kodlemez mátrixban eltárolt karaktereket!
    # TODO: Praktikusabb lett volna a feladatban egy Kiir(Matrix) eljárást előírni, hogy ne kelljen külön-külön metódust írni a tökegyforma két mátrix kiiratására...
    def KiirKodlemez(self):
        for i in range(0,8):
            sor = ""
            for j in range(0,8):
                sor += self.Kodlemez[i][j]
            print(sor)

    # 8. Feladat / A: Definiálja a Fracs osztályban a ForgatJKodLemez() metódust (függvényt) a megadott algoritmus kódolásával!
    def ForgatKodLemez(self):
        ujKodLemez = [['' for i in range(0,8)] for j in range(0,8)]
        for sor in range(0,8):
            for oszlop in range(0,8):
                ujKodLemez[7-oszlop][sor] = (self.Kodlemez[sor][oszlop])
        return ujKodLemez
    
    # 10. feladat: Készítsen az Fracs osztályban metódust Titikosit() azonosítóval, ami a bevezetőben ismertetett eljárással titkosítja az átalakított Titkositando változó értékét a Titkositott karakter típusú mátrixba a Kodlemez mátrix felhasználásával!
    #     A Kodlemez mátrixot minden 16 karakter titkosítása után el kell forgatnia balra 90°-kal a 9. feladatban definiált ForgatKodlemez() metódus hívásával!
    #     A titkosított szöveget (mátrixot) jelenítse meg a képernyőn a minta szerint!
    def Tititkosit(self):
        index = 0
        for forgatas in range(0, 4):
            for oszlop in range(0,8):
                for sor in range(0,8):
                    if self.Kodlemez[sor][oszlop] == 'A':
                        self.Titkositott[sor][oszlop] = self.Titkositando[index]
                        index += 1
            self.Kodlemez = self.ForgatKodLemez()

    # 10./b: megjeleníti a Titkositott mátrixban eltárolt karaktereket!
    # TODO: Praktikusabb lett volna a feladatban egy Kiir(Matrix) eljárást előírni, hogy ne kelljen külön-külön metódust írni a tökegyforma két mátrix kiiratására...
    def KiirTitkositott(self):
        for i in range(0,8):
            sor = ""
            for j in range(0,8):
                sor += self.Titkositott[i][j]
            print(sor)
                

# 5. Feladat: Töltse be és tárolja egy szöveges változóban a titkosítandó szöveget a szoveg.txt állományból, majd írja ki a képernyőre a minta szerint!
print("\n 5. feladat")
with open("szoveg.txt", "r") as file:
    forras =  file.readline().strip()
print(forras)


# 6. Feladat: Hozzon létre egy Fracs típusú osztálypéldányt (objektumot), melynek a konstruktora a kodlemez.txt forrásállomány nevét és a titkosítandó szöveget kapja aktuális paraméterként feldolgozásra!
fracs = Fracs('kodlemez.txt', forras)

# 7. feladat / B: ...megjeleníti a Kodlemez mátrixban eltárolt karaktereket!
print("\n 7. feladat")
fracs.KiirKodlemez()

# 8. feladat / B: Jelenítse meg a képernyőn az átalakított titkosítandó szöveget a minta szerint!
print("\n 8. feladat")
print(fracs.Titkositando)


# 10. feladat / B: A titkosított szöveget (mátrixot) jelenítse meg a képernyőn a minta szerint!
print("\n 10. feladat")
fracs.Tititkosit()
fracs.KiirTitkositott()