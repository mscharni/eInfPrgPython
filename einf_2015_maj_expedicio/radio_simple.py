### Emelt Informatika Érettségi - 2015 Május - Expedíció

uzenetek = []

# 1. feladat: Olvassa be és tárolja a veetel.txt fájl tartalmát!
print("\n1. feladat:")
with open("veetel.txt", "r") as file:
    lines = file.readlines()
for i in range(0, len(lines), 2):
    line1 = lines[i].strip().split(" ")
    line2 = lines[i+1].strip()
    uzenet = {
        'nap' : int(line1[0]),
        'ado' : int(line1[1]),
        'msg' : line2
        }
    uzenetek.append(uzenet)


# 2. feladat: Írja a képernyőre, hogy melyik rádióamatőr rögzítette az állományban szereplő első és melyik az utolsó üzenetet!
print("\n2. feladat:")
print(f"Az első üzenet rögzítője: {uzenetek[0]['ado']}")
print(f"Az utolsó üzenet rögzítője: {uzenetek[-1]['ado']}")
 

# 3. feladat: Adja meg az összes olyan feljegyzés napját és a rádióamatőr sorszámát, amelynek szövegében a „farkas” karaktersorozat szerepel!
print("\n3. feladat:")
for uzenet in uzenetek:
    if uzenet['msg'].find("farkas") > -1:
        print(f"{uzenet['nap']}. nap {uzenet['ado']}. rádióamatőr")

# 4. feladat: Készítsen statisztikát, amely megadja, hogy melyik napon hány rádióamatőr készített feljegyzést.
#   Azok a napok 0 értékkel szerepeljenek, amikor nem született feljegyzés!
#   Az eredmény a képernyőn jelenjen meg a napok sorszáma szerint növekvően!
#   A megjelenítést a feladat végén látható minta szerint alakítsa ki!
print("\n4. feladat:")
napok = [0 for i in range (11)]
for uzenet in uzenetek:
    napok[uzenet['nap']-1] += 1    # nullától indul az indexelés, ezért eggyel kisebb, mint a nap értéke
for i in range (11):
    print(f"{i+1:2}. nap {napok[i]:2} rádióamatőr") # a nap értéke eggyel nagyobb, mint a lista indexé


# 5. feladat: A rögzített üzenetek alapján kísérelje meg helyreállítani az expedíció által küldött üzenetet!
#   Készítse el az adaas.txt fájlt, amely napok szerinti sorrendben tartalmazza a küldött üzeneteket!
#   Ha egy időpontban senkinél nem volt vétel, akkor azon a ponton a # jel szerepeljen!
print("\n5. feladat:")
file = open("adaas.txt", "w")
for nap in range (11):
    uzi = [['' for i in range(90)] for j in range(12)]
    for uzenet in uzenetek:
        if uzenet['nap'] == nap+1:
            for c in range(90):
                betu = uzenet['msg'][c]
                if betu != '#' :
                    uzi[nap][c] = betu
    file.write("".join(uzi[nap]))
    file.write("\n") # sortörés
file.flush() # kiírja a buffer tartalmát a fileba
file.close() # bezérja a file-t


# 6. feladat: Készítsen függvényt szame néven az alábbi algoritmus alapján!
#   A függvény egy karaktersorozathoz hozzárendeli az igaz vagy a hamis értéket.
#   A függvény elkészítésekor az algoritmusban megadott változóneveket használja!
print("\n6. feladat:")
def szame(szo):
    valasz = True
    for i in range(0, len(szo)):     # nullától indul a szó karaktereinek indexelése
        if szo[i] < '0' or szo[i]> '9':
            valasz = False
    return valasz


# 7. feladat: Olvassa be egy nap és egy rádióamatőr sorszámát, majd írja a képernyőre a megfigyelt egyedek számát (a kifejlett és kölyök egyedek számának összegét)!
#   Ha nem volt ilyen feljegyzés, a „Nincs ilyen feljegyzés” szöveget jelenítse meg!
#   Ha nem volt megfigyelt  egyed vagy számuk nem állapítható meg, a „Nincs információ” szöveget jelenítse meg!
#   Amennyiben egy számot közvetlenül # jel követ, akkor a számot tekintse nem megállapíthatónak!
print("\n7. feladat:")
nap = int(input("Adja meg a nap sorszámát! "))
ado = int(input("Adja meg a rádióamatőr sorszámát! "))
db = 0
vane = False
joe = False
for uzenet in uzenetek:
    if uzenet['nap'] == nap and uzenet['ado'] == ado:
        vane = True
        # a szövege elején az első szóközig terjedő részben vannak az egyedszámok 
        eleje = uzenet['msg'].split(' ')[0]
        # a két számot "/" -jel választja el egyástól (ha van benne)
        szamok = eleje.split('/')
        if len(szamok) == 2:
            if szame(szamok[0]) and szame(szamok[1]):
                db += int(szamok[0])
                db += int(szamok[1])
                joe = True
        break
if vane:
    if joe:
        print(f"A megfigyelt egyedek száma: {db}")
    else:
        print("Nincs információ")
else:
    print("Nincs ilyen feljegyzés")