### Emelt Informatika Érettségi - 2021  május - Bányató

# 1. feladat: Olvassa be és tárolja el a melyseg.txt állomány adatait, és annak felhasználásával oldja meg a következő feladatokat!
banyato = []
szarazfold = 0
melyseg = 0
with open('melyseg.txt') as file:
    sor = int(file.readline().strip())
    oszlop = int(file.readline().strip())
    for i in range(0, sor):
        soradat = [int(adat) for adat in file.readline().strip().split()]
        banyato.append(soradat)
        szarazfold += soradat.count(0)
        melyseg += sum(soradat)
print(banyato)


# 2. feladat: Kérje be egy mérési eredmény sor- és oszlopazonosítóját, majd írassa ki az adott helyen mért adatot a képernyőre! (A sorok és oszlopok számozása kezdődjön 1-gyel!)
print("\n2. feladat")
sori = 12 # int(input("A mérés sorának azonosítója = ")
oszi = 6  # int(input("A mérés oszlopának azonosítója = ")
print(f"A mért mélység az adott helyen {banyato[sori-1][oszi-1]} dm")

# 3. feladat: Határozza meg a tó (vagyis az ábrán szürkével jelölt rész) felszínének területét, valamint a tó átlagos mélységét! Írassa ki a két eredményt a mintának megfelelően a képernyőre!
#    A tó átlagos mélysége méterben kifejezve, két tizedesjegy pontossággal jelenjen meg!
print("\n3. feladat")
to = sor * oszlop - szarazfold
print(f"A tó felszíne: {to} m2, átlagos mélysége: {melyseg/(10*to):.2f} m")

# 4. feladat: Mekkora a tó legnagyobb mélysége, és hol a legmélyebb a tó? Jelenítse meg a választ a képernyőn!
#    A legmélyebb pont koordinátáit a mintának megfelelően (sor; oszlop) formában írassa ki! Ha több ilyen mérési eredmény is van, mindegyik koordinátapárja jelenjen meg!
print("\n4. feladat")
legmelyebb = 0
legmelyebbek = []
for i in range(0, sor):
    for j in range(0, oszlop):
        if banyato[i][j] > legmelyebb:
            legmelyebb = banyato[i][j]
            legmelyebbek = [(i,j)]
        elif banyato[i][j] == legmelyebb:
            legmelyebbek.append((i,j))
print(f"A tó legnagyobb mélysége: {legmelyebb*10} dm")
print(f"A legmélyebb helyek sor-oszlop koordinátái:")
ki = ""
for koord in legmelyebbek:
    ki += f"({koord[0]+1}; {koord[1]+1})\t"
print(ki)

# 5. feladat: Milyen hosszú a tó partvonala, vagyis az ábrán a szürkével jelölt részt határoló vastag fekete vonal hossza?
#    A partvonalhoz vegye hozzá a tóban lévő szigetek kerületét is!
#    Írassa ki az eredményt a mintának megfelelően a képernyőre! (A megoldás során felhasználhatja, hogy a táblázat első és utolsó sorában és oszlopában minden adat 0.)
print("\n5. feladat")
part = 0
for i in range(1, sor-1):
    for j in range(1,oszlop-1):
        if banyato[i][j] > 0:
            if banyato[i-1][j] == 0: part += 1
            if banyato[i+1][j] == 0: part += 1 
            if banyato[i][j-1] == 0: part += 1 
            if banyato[i][j+1] == 0: part += 1 
print(f"A tó partvonala {part} m hosszú")

# 6. feladat: Kérje be a felhasználótól egy oszlop azonosítóját, és szemléltesse a diagram.txt szöveges állományban „sávdiagramon” a tó mélységét az adott oszlopban a következő módon!
#    A sor elején jelenjen meg a mérési adat sorának azonosítója pontosan két számjeggyel, majd tegyen egymás mellé annyi csillagot (*), ahány méter az adott helyen a tó mélysége!
#    A mérési adatokat a matematika szabályainak megfelelően kerekítse!
print("\n6. feladat")
oszi = 6  # int(input("A vizsgált szelvény oszlopának azonosítója = ")
with open("diagram.txt","w") as file:
    for i in range(0, sor):
        sorszam = "0" + str(i+1) if i < 9 else str(i)  
        file.write(f"{sorszam}{'*'*int(round(banyato[i][oszi-1]/10,0))}\n")


print("\n*. feladat: markdown table")
print("|  | " + " | ".join([str(i+1) for i in range(0,oszlop)]) + " | ")
# print("-----"*sor)
print("|:---:"*oszlop + "|:--:|")
for i in range(0, sor):
    print(f"|**{i+1}**| " + " | ".join([str(banyato[i][j]) for j in range(0, oszlop)]) + " | ")
    