### Emelt Informatika Ismeretek Érettségi - 2019 Október - Játszma

# 1. Feladat: Készítsen programot a következő feladatok megoldására, amelynek a forráskódját Játszma5 néven mentse el!


# 6. Feladat: Játék osztály
#    a. Minden játszma játékokból áll, mely játékok általában 4-12 labdamenetnél nem hosszabbak.
#    Hozzon létre saját osztályt egy játék adatainak tárolására Játék azonosítóval!
class Jatek:
    
    # b. Egy játék aktuális eredményét a továbbiakban állásnak nevezzük. Az osztály adattagjai legyenek alkalmasak az állás (például: „AFAA”), az adogató játékos és a fogadó játékos neveinek a tárolására!
    # c. Készítsen a Játék osztályba konstruktort, ami paramétereken keresztül az adogató és a fogadó játékos nevét, valamint a játék aktuális állását állítja be!
    #    A konstruktorban további adattagok inicializálását is elvégezheti!
    def __init__(self, allas, adogato, fogado):
        self.Allas = allas
        self.Adogato = adogato
        self.Fogado = fogado
        # 9. feladathoz
        self.Nyertes = ""
    # d. Készítsen metódust Hozzáad azonosítóval, ami egy paraméterben átadott labdamenet eredményét („A” vagy „F”) adja majd hozzá az aktuális játék állásához!
    def Hozzaad(self,labdamenet):
        self.Allas += labdamenet
    # e. Készítsen metódust NyertLabdamenetekSzáma azonosítóval, mely segítségével a paraméterben kódolt adogató („A”) vagy fogadó („F”) játékos által megnyert labdamenetek számát határozza meg az aktuális állásból!
    def NyertLabdamenetekSzama(self, jatekos):
        return self.Allas.count(jatekos)
        
    # f. Mivel a forrás állományban nincs ténylegesen jelezve egy-egy játék vége, ezért készítsen logikai értékkel visszatérő metódust vagy jellemzőt JátékVége azonosítóval, ami a tárolt állás alapján meghatározza, hogy befejeződött-e az aktuális játék vagy még folyamatban van! A metódust a következő algoritmus szerint kódolja
    def JatekVege(self):
        nyertAdogato = self.NyertLabdamenetekSzama('A')
        nyertFogado = self.NyertLabdamenetekSzama('F')
        kulonbseg = abs(nyertAdogato-nyertFogado)
        return (nyertAdogato >=4 or nyertFogado >=4)  and (kulonbseg >=2)
    
    

# 2. Feladat: A játszma legkisebb pontozható egysége a labdamenet.
#    Az 5. játszma labdameneteinek eredménye a labdamenetek5.txt szöveges állományban áll rendelkezésünkre a következők szerint:
#    • a labdamenetet „A” betűvel kódoltuk, ha azt adogató játékos nyerte
#    • a labdamenetet „F” betűvel kódoltuk, ha azt a fogadó játékos nyerte
#    • soronként egy-egy labdamenet eredménye található időrendben
#    • az állományban kódolt utolsó labdamenet az 5. játszma végét jeleni
#    • az állományban lévő adatok értelmezéséhez egy táblázatot is készítettünk a feladat végén
#    Olvassa be a labdamenetek eredményeit a labdamenetek5.txt állományból és tárolja egy összetett adatszerkezetben!
labdamenetek = []
with open("labdamenetek5.txt", "r") as file:
    for line in file:
        labdamenetek.append(line.strip())


# 3. feladat: Számolja meg és írja ki a minta szerint a labdamenetek számát!
print(f"\n3. feladat: Labdamenetek száma:{len(labdamenetek)}")


# 4. Feladat: A teniszben a labdamenetet gyakran az adogató játékos nyeri.
#    Határozza meg és írja ki, hogy az adogató játékos hány százalékát nyerte meg a labdameneteknek!
print(f"\n4. feladat: Az adogató játékos {labdamenetek.count('A')/len(labdamenetek):%}-ban nyerte meg a lapdameneteket.")


# 5. Határozza meg és írja ki a minta szerint, hogy hány adogatásból állt az a leghosszabb sorozat, melyben mindig az adogató játékos nyert!
eleje = 0
# megkeressük az első 'A'-t
while labdamenetek[eleje] != 'A':
    eleje +=1
vege = eleje
hossz = vege - eleje +1
elozo = 'A'
for i in range(eleje+1,len(labdamenetek)):
    # ha 'A'
    if labdamenetek[i] == 'A':
        # ha 'A'-ra vált 'F'-ről
        if elozo == 'F' :
            eleje = i
            vege = i
        else:
            # 'A' sorozat belseje
            vege = i
    else:
        # ha 'F'-re vált 'A'-ról
        if elozo == 'A' :
            # végetér az 'A' sorozat
            if vege-eleje + 1 > hossz:
                hossz = vege - eleje + 1
    elozo = labdamenetek[i]
print(f"\n5. feladat: Leghosszabb sorozat:{hossz}")


# 7. Feladat: Hozzon létre egy példányt a Játék osztályból PróbaJáték azonosítóval az osztály teszteléséhez.
#    Inicializálja a példányt az alábbi adatokkal:
#    adogató: ’Mahut’, fogadó: ’Isner’, állás: ’FAFAA’
#    A Hozzáad metódus hívásával adja hozzá az aktuális álláshoz egy labdamenet eredményét, amiben az adogató nyert.
#    Ezt követően írja ki a minta szerint az új állást és hogy befejeződött-e a próbajáték. Utóbbihoz használja a JátékVége metódust!
print(f"\n7. feladat: A próba játék")
ProbaJatek = Jatek("FAFAA", "Mahut", "Isner")
ProbaJatek.Hozzaad("A")
print(f"Állás: {ProbaJatek.Allas}")
print(f"Befejeződött a játék: {'igen' if ProbaJatek.JatekVege() else 'nem'}")


# 8. feladat: Egy játékokon belül mindig ugyanaz a teniszező adogat, majd amikor a játék befejeződik, akkor a következő játék során az adogatás joga a másik versenyzőre száll az eredménytől függetlenül.
#    Hozzon létre egy Játék osztálypéldányt, majd töltse fel a Hozzáad metódus hívásával/hívásaival az 5. játszma első játékának állásával!
#    Ha az osztálypéldányban tárolt állás alapján az aktuális játéknak vége, azaz a JátékVége metódus igaz értékkel tér vissza, akkor mentse el az osztálypéldányt egy összetett adatszerkezetben, majd folytassa hasonlóan az 5. játszma többi játékának a feldolgozásával!
#    A feladat megoldásához lényeges, hogy az 5. játszma 1. játéka Isner adogatásával kezdődik.
#    Feltételezheti, hogy a labdamenetek5.txt állomány utolsó karaktere az 5. játszma utolsó játékának utolsó labdamenetét kódolja!
jatekok = []
adogato = "Isner"
fogado = "Mahut"
jatek = Jatek(labdamenetek[0], adogato, fogado)
for i in range(1, len(labdamenetek)):
    jatek.Hozzaad(labdamenetek[i])
    if jatek.JatekVege():
        # nyertes megállapítása
        if jatek.Allas.count('A') > jatek.Allas.count('F'):
            jatek.Nyertes = jatek.Adogato
        else:
            jatek.Nyertes = jatek.Fogado
        jatekok.append(jatek)
        # adogató és fogadó csere
        csere = adogato
        adogato = fogado
        fogado = csere
        # új játék létrehozása
        jatek = Jatek("", adogato, fogado)
        

# 9. Feladat: Számolja meg és írja ki a minta szerint, hogy az 5. játszmában hány játékot nyertek a teniszezők külön-külön!
#    Egy játékot az a teniszező nyert meg, akinek több megnyert labdamenete volt az adott játékban!
print(f"\n9. feladat: Az 5. játszma végeredménye:")
nyertes = {
    "Mahut" : 0,
    "Isner" : 0
}
# i = 1
for jatek in jatekok:
    # print(f"{i:3}. játék, adogat: {jatek.Adogato}, fogad: {jatek.Fogado}, labdamenet:{jatek.Allas}")
    # i += 1
    nyertes[jatek.Nyertes] +=1
print(f"Mahut: {nyertes['Mahut']}")
print(f"Isner: {nyertes['Isner']}")