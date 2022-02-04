### Emelt Informatika Ismeretek Érettségi - 2019 Október - Játszma

# 1. Feladat:vKészítsen programot a következő feladatok megoldására, amelynek a forráskódját Játszma5 néven mentse el!

# 2. Feladat: A játszma legkisebb pontozható egysége a labdamenet.
#    Az 5. játszma labdameneteinek eredménye a labdamenetek5.txt szöveges állományban áll rendelkezésünkre a következők szerint:
#    • a labdamenetet „A” betűvel kódoltuk, ha azt adogató játékos nyerte
#    • a labdamenetet „F” betűvel kódoltuk, ha azt a fogadó játékos nyerte
#    • soronként egy-egy labdamenet eredménye található időrendben
#    • az állományban kódolt utolsó labdamenet az 5. játszma végét jeleni
#    • az állományban lévő adatok értelmezéséhez egy táblázatot is készítettünk a feladat végén
#    Olvassa be a labdamenetek eredményeit a labdamenetek5.txt állományból és tárolja egy összetett adatszerkezetben!
jatszmak = []
with open("labdamenetek5.txt", "r") as file:
    jatszmak = file.readlines()

