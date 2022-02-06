### Emelt Informatika Érettségi - 2006 október - Zenei adók

class Zene():
    def __init__(self, line):
        # először kettőspont szerint szeletelünk, mert abból csak egy van
        datas = line.strip().split(":")
        self.cim = datas[1]
        # majd az első felét szóköz szerint
        datas = datas[0].split(" ")
        self.ado = int(datas[0])
        self.perc = int(datas[1])
        self.mperc = int(datas[2])
        self.hossz = self.perc*60 + self.mperc  # 3. feladathoz: szám hossza másodpercben
        self.kezdet = adoidok[self.ado]         # 4. feladathoz: számok kezdési ideje 00:00-tól másodpercben számolva
        adoidok[self.ado] += self.hossz         # 4. feladathoz: szám hosszával növeljük az adón aktuálisan eltelt időt
        self.kezdet_opm = opm(self.kezdet)      # extra feladathoz 
        # a fenmaradó rész(ek) az előadó neve(i)
        ea = ""
        for i in range(3, len(datas)):
            ea += datas[i] + " "
        self.eloado = ea.strip()
        
# 3. feladathoz: a 00:00:00-tól másodpercben eltelt időt 'óó:pp:mm' formában adja vissza
def opm(ido):
    ora = ido // (60*60)
    perc = (ido - ora*60*60) // 60
    mperc = (ido - ora*60*60 - perc*60) 
    return f"{str(ora).zfill(2):2}:{str(perc).zfill(2):2}:{str(mperc).zfill(2)}"
                                                     
adoidok = [0,0,0,0]    # nulladik indexű elemet nem használjuk
zenek = []

# 1. Olvassa be a musor.txt állományban talált adatokat, s annak felhasználásával oldja meg a következő feladatokat!
print("\n1. feladat")
with open("musor.txt", "r") as fileBe:
    # első sor beolvasása
    zene_db = int(fileBe.readline().strip())
    for line in fileBe:
        zene = Zene(line)
        zenek.append(zene)
print("Adatok beolvasva a 'musor.txt' állományból.")

#2. Írja a képernyőre, hogy melyik csatornán hány számot lehetett meghallgatni!
print("\n2. feladat")
# max 3 adó van
adok = [0,0,0,0]    # nulladik indexű elemet nem használjuk
for zene in zenek:
    adok[zene.ado] += 1
for i in range(1,4):
    print(f"A {i}. adón {adok[i]} számot lehetett meghallgatni")

# 3. Adja meg, mennyi idő telt el az első Eric Clapton szám kezdete és az utolsó Eric Clapton szám vége között az 1. adón!
#   Az eredményt óra:perc:másodperc formában írja a képernyőre!
print("\n3. feladat")
ido = 0
elso_idx = 0
# első 1. adón lejátszott Eric Clapton szám
while zenek[elso_idx].eloado != "Eric Clapton" and zenek[elso_idx].ado != 1:
    elso_idx += 1
ido += zenek[elso_idx].hossz
# utolsó 1. adón lejátszott Eric Clapton szám
utso_idx = len(zenek)-1

print("\n3.A megoldás: hossz alapján")
while zenek[utso_idx].eloado != "Eric Clapton"  and zenek[elso_idx].ado != 1:
    utso_idx -= 1
ido += zenek[utso_idx].hossz
# végigmegyünk a kettő közötti összes számon
for i in range(elso_idx + 1, utso_idx):
    # ha 1. adón játszott szám, akkor növeljük a szám időtartamával az eltelt időt
    if zenek[i].ado == 1:
        ido += zenek[i].hossz
print(f"{opm(ido)} idő telt el az első és utolsó Eric Clapton szám között.")

print("\n3.B megoldás: kezdési idő alapján")
ido = zenek[utso_idx].kezdet + zenek[utso_idx].hossz - zenek[elso_idx].kezdet
print(f"{opm(ido)} idő telt el az első és utolsó Eric Clapton szám között.")

    
# 4. Amikor az „Omega:Legenda” című száma elkezdődött, Eszter rögtön csatornát váltott.
#   Írja a képernyőre, hogy a szám melyik adón volt hallható, és azt, hogy a másik két adón milyen számok szóltak ekkor.
#   Mivel a számok a kezdés időpontja szerint növekvő sorrendben vannak, így a másik két adón már elkezdődött a számok lejátszása.
#   Feltételezheti, hogy a másik két adón volt még adás.
# FIXIT: Ellenőrizze, hogy a másik két adón volt-e ekkor adás...
print("\n4. feladat")
idx = 0
# az első Omega:Legenda szám
while zenek[idx].eloado != "Omega" or zenek[idx].cim != "Legenda":
    idx += 1
print(f"Az {zenek[idx].eloado}:{zenek[idx].cim} szám a {zenek[idx].ado}. adón volt hallható {zenek[idx].kezdet_opm} kezdettel. ")
kezdet = zenek[idx].kezdet
# megállapítjuk, hogy melyik a másik két adó.
if zenek[idx].ado == 1:
    ado2 = 2
    ado3 = 3
elif zenek[idx].ado == 2:
    ado2 = 1
    ado3 = 3
else:
    ado2 = 1
    ado3 = 2
# megkeressük, hogy a másik két adón mi szólt ekkor
idx2 = len(zenek)-1
while zenek[idx2].ado != ado2 or zenek[idx2].kezdet > kezdet:
    idx2 -= 1
if zenek[idx2].kezdet < kezdet  and kezdet < zenek[idx2].kezdet + zenek[idx2].hossz:
    print(f"A {ado2}. adón eközben a {zenek[idx2].eloado} előadó {zenek[idx2].cim} száma volt hallható {zenek[idx2].kezdet_opm} kezdettel.")    
else:
    print(f"A {ado2}. adón eközben nem volt adás!")    
idx3 = len(zenek)-1
while zenek[idx3].ado != ado3 or zenek[idx3].kezdet > kezdet:
    idx3 -= 1
if zenek[idx3].kezdet < kezdet  and kezdet < zenek[idx3].kezdet + zenek[idx3].hossz:    
    print(f"A {ado3}. adón eközben a {zenek[idx3].eloado} előadó {zenek[idx3].cim} száma volt hallható {zenek[idx2].kezdet_opm} kezdettel.")
else:
    print(f"A {ado3}. adón eközben nem volt adás!")    

# 5. Az egyik rádióműsorban sms-ben, telefonon, de akár képeslapon is kérhető szám.
#   Ám a sokszor csak odafirkált kéréseket olykor nehéz kibetűzni.
#   Előfordul, hogy csak ennyi olvasható: „gaoaf”, tehát ezek a betűk biztosan szerepelnek, mégpedig pontosan ebben a sorrendben.
#   Annyi biztos, hogy először a szerző neve szerepel, majd utána a szám címe.
#   Olvassa be a billentyűzetről a felismert karaktereket, majd írja a keres.txt állományba azokat a számokat, amelyek ennek a feltételnek megfelelnek.
#   Az állomány első sorába a beolvasott karaktersorozat, majd utána soronként egy zeneszám azonosítója kerüljön!
#   A feladat megoldása során ne különböztesse meg a kis- és a nagybetűket!
print("\n5. feladat")
keres = input("Keresendő zeneszám = ").lower()
talalt_list = []
for zene in zenek:
    szamazo = zene.eloado.lower() + zene.cim.lower()
    megfelel = True
    # a keresendő kifejezésen betűnként végigmegyünk és rendre megnézzük hogyszerepel-e aszam azonosítójának maradék részébe
    for c in keres:
        hely = szamazo.find(c)
        if hely > -1:
            szamazo = szamazo[hely+1:]
        else:
            megfelel = False
            break
    if megfelel:
        # kigyűjtjük egy listába
        talalt_list.append(f"{zene.eloado}:{zene.cim}")
# a talált számok listájából halmazt csinálunk, hogy egy szám biztosan csak egyszer szerepeljen (unique)
talalt_set = set(talalt_list)
# kiírjuk állományba
with open("keres.txt", "w") as fileKi:
    fileKi.write(f"{keres}\n")
    for talalt in talalt_set:
        fileKi.write(f"{talalt}\n")
print("Adatok kiírva a 'keres.txt' állományba")    

# 6. Az 1. adón változik a műsor szerkezete: minden számot egy rövid, egyperces bevezető előz majd meg, és műsorkezdéstől minden egész órakor 3 perces híreket mondanak.
#   Természetesen minden szám egy részletben hangzik el továbbra is, közvetlenül a bevezető perc után.
#   Így ha egy szám nem fejeződne be a hírekig, el sem kezdik, az üres időt a műsorvezető tölti ki.
#   Írja a képernyőre óra:perc:másodperc formában, hogy mikor lenne vége az adásnak az új műsorszerkezetben!
# EXTRA (nem része az érettségi feladatnak: írja ki az új műsorrendet a 'ujmusor.txt' állományba!)
print("\n6. feladat")
bev = 60
hir = 3*60
ido = 0
fileKi = open("ujmusor.txt", "w",)
for zene in zenek:
    # ha az 1. adón megy
    if zene.ado == 1:
        # ha nem esik a hírekbe a bevezetővel együtt, azaz a szám kezdete és vége ugyanabba az órába kerül
        szamvege = ido + bev + zene.hossz
        if ido // (60*60) == szamvege // (60*60):
            fileKi.write(f"{opm(ido + bev)} - {opm(ido + zene.hossz + bev)} [{zene.hossz:>3}] {zene.eloado:25}:{zene.cim:30}\n")
            ido = szamvege
        else:
            # hírek ideje
            ido = 60*60*(1 + ido // (60*60)) 
            fileKi.write(f"{opm(ido)} - {opm(ido + hir)} [{hir:>3}] *** == - Hírek - == ***\n")
            ido += hir
fileKi.flush()
fileKi.close()
print(f"Az adásnak {opm(ido)}-kor lenne vége az új műsorrend szerint.")
