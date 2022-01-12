### Emelt Informatika Érettségi - 2005 Október - Vigenere

# 1. Kérjen be a felhasználótól egy maximum 255 karakternyi, nem üres szöveget!
#   A továbbiakban ez a nyílt szöveg.
print("\n1. feladat")
szoveg = input("Nyílt szöveg = ")

# 2. Alakítsa át a nyílt szöveget, hogy a későbbi kódolás feltételeinek megfeleljen!
# A kódolás feltételei:
#   • A magyar ékezetes karakterek helyett ékezetmenteseket kell használni. (Például á helyett a; ő helyett o stb.)
#   • A nyílt szövegben az átalakítás után csak az angol ábécé betűi szerepelhetnek.
#   • A nyílt szöveg az átalakítás után legyen csupa nagybetűs.
print("\n2. feladat")
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(abc))
szoveg = szoveg.upper()
szoveg = szoveg.replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ö","O").replace("Ő","O").replace("Ú","U").replace("Ü","U").replace("Ű","U")
kodolando = ""
for c in szoveg:
    if c in abc:
        kodolando += c
print("Nyílt szöveg átalakítva.")

# 3. Írja ki a képernyőre az átalakított nyílt szöveget!
print("\n3. feladat")
print(f"Átalakított nyílt szöveg = {kodolando}")

# 4. Kérjen be a felhasználótól egy maximum 5 karakteres, nem üres kulcsszót!
# A kulcsszó a kódolás feltételeinek megfelelő legyen! (Sem átalakítás, sem ellenőrzés nem kell!)
# Alakítsa át a kulcsszót csupa nagybetűssé!
print("\n4. feladat")
kulcsszo = input("Kulcsszó = ").upper()
print(f"Kulcsszó = {kulcsszo}")

# 5. A kódolás első lépéseként fűzze össze a kulcsszót egymás után annyiszor, hogy az így kapott karaktersorozat (továbbiakban kulcsszöveg) hossza legyen egyenlő a kódolandó szöveg hosszával!
# Írja ki a képernyőre az így kapott kulcsszöveget!
print("\n5. feladat")
db = len(kodolando) // len(kulcsszo) +1
kulcsszoveg = kulcsszo * db
kulcsszoveg = kulcsszoveg[0:len(kodolando)]
print(f"kulcsszöveg = {kulcsszoveg}")

# 6. 6. A kódolás második lépéseként a következőket hajtsa végre!
#   Vegye az átalakított nyílt szöveg első karakterét, és keresse meg a vtabla.dat fájlból beolvasott táblázat első oszlopában!
#   Ezután vegye a kulcsszöveg első karakterét, és keresse meg a táblázat első sorában!
#   Az így kiválasztott sor és oszlop metszéspontjában lévő karakter lesz a kódolt szöveg első karaktere.
#   Ezt ismételje a kódolandó szöveg többi karakterével is!
print("\n6. feladat")
kodolt = ""
tabla = []
with open("vtabla.dat") as fileBe:
    for line in fileBe:
        sor = list(line.strip())
        tabla.append(sor)

for i in range(0, len(kodolando)):
    # kódolandó szöveg karakter az első oszlopból
    row = 0
    while tabla[row][0] != kodolando[i]:
        row += 1
    # kulcsszöveg karakter az első sorból
    col = 0
    while tabla[0][col] != kulcsszoveg[i]:
        col += 1
    kodolt += tabla[row][col]
print("A kódolás kész")

# 7. Írja ki a képernyőre és a kodolt.dat fájlba a kapott kódolt szöveget!
print(f"Kódolt szöveg = {kodolt}")
with open("kodolt.dat", "w") as fileKi:
    fileKi.write(kodolt)
