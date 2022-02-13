import random
# Python beépített rendezései

_szavak = ['alom', 'arany','arány', 'álom', 'cica', 'csak', 'csík', 'csök', 'csuk', 'arám', 'áram', 'érem', 'irány', 'irén', 'írem', 'írom', 'orom', 'öröm', 'üröm' ]
_rekordok = [
    {'nev': 'Alma', 'pont': 1},
    {'nev': 'Szilva', 'pont': 4},
    {'nev': 'Barack', 'pont': 6},
    {'nev': 'Narancs', 'pont': 5},
    {'nev': 'Citrom', 'pont': 3},
    {'nev': 'Datolya', 'pont': 2}
]
class Koordinata():
    def __init__(self, nev="-", X = 0, Y=0):
        self.nev = nev
        self.X = X
        self.Y = Y
        self.tav2 = X*X + Y*Y

print("Egydimenziós tömb (lista) rendezése")
print("Rendezendő adatok")
adatok = _szavak.copy()
random.shuffle(adatok)

print(f"{adatok}")

print("Rendezve - növekvő sorrend")
adatok.sort()
print(f"{adatok}")

print("Rendezve - csökkenő sorrend")
adatok.sort(reverse=True)
print(f"{adatok}")


print("Rendezve - első karakter, mint kulcs szerint")
abc = ['0','1','2','3','4','5','6','7','8','9','a','á','b','c','cs','d','dz','dzs','e','é','f','g','gy','h','i','í','j','k','l','ly','m','n','ny','o','ó','ö','ő','p','q','r','s','sz','t','ty','u','ú','ü','ű','v','w','x','y','z','zs']
# olyan (vagy összette adatszerkezet valamely tulajdonságát, vagy egy, valamely tulajdonság(ok) alapján generált) értéket kell visszaadni, ami alapján már (egydimenziós listaként) rendezni tud kulcsok alapján
def byLetterKey(elem):
    return abc.index(elem[0])
    
adatok.sort(key=byLetterKey)
print(f"{adatok}")

print()

print("Rekord (szótárakból álló lista) rendezése")
print("Rendezendő adatok")
adatok = _rekordok.copy()
random.shuffle(adatok)

print("Rendezve - 'nev' kulcs szerinti sorrend")
def byKeyNamed_Nev(elem):
    return elem['nev']
adatok.sort(key=byKeyNamed_Nev)
print(f"{adatok}")

print("Rendezve - 'pont' kulcs sorrendi sorrend")
def byKeyNamed_Pont(elem):
    return elem['pont']
adatok.sort(key=byKeyNamed_Pont)
print(f"{adatok}")


print("\nObjektumokból álló lista rendezése")
print("Rendezendő adatok")
_objektumok = [Koordinata(chr(i), random.randint(-20,20), random.randint(-20,20)) for i in range(65, 91)]
adatok = _objektumok.copy()
random.shuffle(adatok)
for adat in adatok:
    print(f"{adat.nev} ({adat.X};{adat.Y}) - {adat.tav2:.2f};")
print("Rendezve - 'nev' kulcs szerinti sorrend")
def byKey_Nev(elem):
    return elem.nev
adatok.sort(key=byKey_Nev)
for adat in adatok:
    print(f"{adat.nev} ({adat.X};{adat.Y}) - {adat.tav2:.2f};")

print("Rendezve - 'tav2' kulcs szerinti sorrend")
def byKey_Tav(elem):
    return elem.tav2
adatok.sort(key=byKey_Tav)
for adat in adatok:
    print(f"{adat.nev} ({adat.X};{adat.Y}) - {adat.tav2:.2f};")
