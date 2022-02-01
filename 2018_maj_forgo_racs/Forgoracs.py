# 1. feladat: Készítsen programot a következő feladatok megoldására, amelynek a forráskódját Forgoracs néven mentse el!

# 2. feladat: Hozzon létre saját osztályt Fracs azonosítóval és definiáljon benne két karakter típusú mátrixot (kétdimenziós tömböt) Kodlemez és Titkositott azonosítóval,
#    illetve egy karakterlánc típusú, csak olvasható jellemzőt Titkositando azonosítóval melyekben az adatokat tudja a feladat megoldása során tárolni!
#    A mátrixok sorai és oszlopai 0-tól 7-ig legyenek indexelve!

class Fracs:
    # 3. feladat: Készítse el az osztály kétparaméteres konstruktorát, ami a következő feladatokat hajtja végre:
    #    a. Inicializálja a Kodlemez és Titkositott mátrixokat 8×8-as mérettel!
    def __init__(self, filename, secret):
        self.Kodlemez = [['' for i in range(0,8)] for j in range(0,8)]
        self.Titkositott = [['' for i in range(0,8)] for j in range(0,8)]
        self.feltolt(filename)
        set_Titkositando(secret)
    # csak olvasható tulajdonság
    @property
    def Titkositando(self):
        return ''
    #    b. Feltölti a Kodlemez mátrixot a „#” és „A” karakterekkel egy szöveges állományból.
    #       A feldolgozandó szövegesfájl nevét a konstruktor paramétereként adjuk át!
    #       A feladat megoldásához használandó kodlemez.txt állomány 8 sora, soronként 8 karakterrel tárolja a kódlemez felépítését.
    #       A kódlemez „ablakait” az „A” karakterekkel jelöltük. Ahol nincs ablak, ott a „#” karakter szerepel a fájlban.
    def feltolt(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()
        for i in range(0,8):
            for j in range(0,8):
                self.Kodlemez[i][j] = lines[i][j]
    #    c. A Titkositando azonosítójú karakterlánc típusú változó értékét meghatározza a konstruktor másik paraméterében megadott paraméterrel!
    def set_Titkositando(self, secret):
        self.Titkositando = secret
        #    d. A Titkositando változó értékét átalakítja az Atalakit() metódus (függvény) hívásával, mely működését a következő (4.) feladatban írtuk le!
        # TODO: miért kell feltölteni az átadott paraméter értékével, ha utána egyből át kell alakítani. Miért nem egy lépés???!!!
        
    # 4. feladat: Hozzon létre az Fracs osztályban Atalakit() azonosítóval metódust, ami a következő feladatokat hajtja végre:
    #    a. A Titkositando változóból törli a szóközöket, pontokat és vesszőket!
    #    b. Kivételt dob „Túl hosszú a titkosítandó szöveg!” üzenettel, ha a törlések után a szöveg hossza nagyobb, mint 64 karakter!
    #    c. A Titkositando változó étékét jobbról „X” karakterekkel tölti fel úgy, hogy a titkosítandó szöveg hossza pontosan 64 karakter legyen!
    def Atalakit():
        
    
fracs = Fracs('kodlemez.txt', "titok")
print(fracs.Kodlemez)
