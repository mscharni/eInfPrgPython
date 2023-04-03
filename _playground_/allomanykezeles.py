nevek = []
with open("osszesffi.txt", "r", encoding="iso-8859-2") as file:
    for line in file:
        nevek.append([line.strip(),"F"])
with open("osszesnoi.txt", "r", encoding="iso-8859-2") as file:
    for line in file:
        nevek.append([line.strip(),"N"])
nevek.sort()
with open("osszesnev.txt", "w", encoding="iso-8859-2") as file:
    for nev in nevek:
        file.writelines(nev[0] + " (" + nev[1] + ")\n")



