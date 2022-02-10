### Emelt Informatika Érettségi - 2019 Május - Tantárgyfelosztás
# 1. feladat: Olvassa be és tárolja el a beosztas.txt állományban talált adatokat, és annak felhasználásával oldja meg a következő feladatokat!
bejegyzesek = []
tanarok = {}
osztalyok = {}
ossz_ora = 0

with open('beosztas.txt', 'r') as file:
    lines = file.readlines()
for i in range(0, len(lines), 4):
    bejegyzes = {
        'nev'  : lines[i+0].strip(),
        'tan'  : lines[i+1].strip(),
        'oszt' : lines[i+2].strip(),
        'ora'  : int(lines[i+3].strip())
    }
    bejegyzesek.append(bejegyzes)

    # tanár óráinak letárolása
    if bejegyzes['nev'] in tanarok:
        tanarok[f"{bejegyzes['nev']}"] += bejegyzes['ora']
    else:
        tanarok[f"{bejegyzes['nev']}"] = bejegyzes['ora']

    # össz óraszám
    ossz_ora += bejegyzes['ora']
    
    # osztályfőnökök letárolása
    if bejegyzes['tan'] == 'osztalyfonoki':
        if bejegyzes['oszt'] in osztalyok:
            osztalyok[f"{bejegyzes['oszt']}"] += bejegyzes['nev']
        else:
            osztalyok[f"{bejegyzes['oszt']}"] = bejegyzes['nev']


# 2. feladat: Hány bejegyzés található az állományban? Az eredményt írassa ki a képernyőre!
print(f"\n2. feladat")
print(f"A fájlban {len(bejegyzesek)} bejegyzés van.")


# 3. feladat: A fenntartó számára fontos információ, hogy az iskolában hetente összesen hány tanítási óra van. Határozza meg ezt az adatot és írassa ki a képernyőre!
print(f"\n3. feladat")
print(f"Az iskolában a heti összóraszám: {ossz_ora}")


# 4. feladat: Kérje be a felhasználótól egy tanár nevét, és írassa ki a képernyőre, hogy hetente hány órában tanít!
print(f"\n4. feladat")
tanar = "Albatrosz Aladin" # input("Egy tanár neve = ")
print(f"A tanár heti óraszáma: {tanarok[tanar]}")


# 5. feladat: Készítse el az of.txt fájlt, amely az osztályfőnökök nevét tartalmazza osztályonként az alábbi formában (az osztályok megjelenítésének sorrendje a mintától eltérhet):
#    9.a - Albatrosz Aladin
#    9.b - Hangya Hanna
#    9.c - Zerge Zenina
#    …
print(f"\n5. feladat")
with open('of.txt', 'w') as file:
    for osztaly in osztalyok:
        file.write(f"{osztaly} - {osztalyok[osztaly]}\n")

# 6. feladat: Egyes osztályokban bizonyos tantárgyakat a tanulók csoportbontásban tanulnak: ekkor az adott tantárgyra és osztályra két bejegyzést is tartalmaz a tantárgyfelosztás.
#    Kérje be egy osztály azonosítóját, valamint egy tantárgy nevét, és írassa ki a képernyőre, hogy az adott osztály a megadott tantárgyat csoportbontásban vagy osztályszinten tanulja-e!
#   (Feltételezheti, hogy a megadott osztály tanulja a megadott tantárgyat.)
print(f"\n6. feladat")
osztaly = '10.b' # input("Osztály = ")
tantargy= 'kemia'  # input("Tantárgy = ")
csoportszam = 0
for bejegyzes in bejegyzesek:
    if bejegyzes['oszt'] == osztaly and bejegyzes['tan'] == tantargy:
        csoportszam +=1
if csoportszam > 1:
    print(f"Csoportbontásban tanulják ({csoportszam})")
elif csoportszam == 1:
    print("Osztályszinten tanulják")
else:
    print("Nem tanulják")


# 7. feladat: 7. A fenntartó számára az is fontos információ, hogy hány tanár dolgozik az iskolában. Írassa ki ezt az adatot a képernyőre!
print(f"\n7. feladat")
print(f"Az iskolában {len(tanarok)} tanár tanít.")