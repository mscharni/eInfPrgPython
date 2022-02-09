# 1. feladat: Olvassa be és tárolja el a beosztas.txt állományban talált adatokat, és annak felhasználásával oldja meg a következő feladatokat!
with open('beosztas.txt', 'r') as file
    lines = file.readlines()
for i in range(0, len(lines), 4):
    bejegyzes = {
        'nev' : lines[0],
        'targy' : lines[1],
        'osztaly' : lines[2],
        'ora' : lines[3]
    }