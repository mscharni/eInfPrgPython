def hetnapja(datum):
    _datum = datum.split(".")
    ev = int(_datum[0])
    ho = int(_datum[1])
    nap = int(_datum[2])
    napok = ['h', 'k', 'sze', 'cs', 'p', 'szo', 'v']
    szokoev = False
    if ev % 4 == 0:
            szokoev = True
    elif ev % 100 == 0:
            szokoev = False
    elif ev % 400 == 0:
            szokoev = True
    if szokoev:
            honapok = [0, 3, 3, 6, 2, 4, 6, 2, 5, 7, 3, 5]
    else:
            honapok = [0, 3, 3, 6, 2, 4, 6, 2, 5, 7, 3, 5]
    ev = ev 
    ho -= 1     # nullától számolunk
    nap -=1     # nullától számolunk
    print(f"{ev} {ho} {nap} {szokoev}")
    hetnapja = napok[(ev + honapok[ho] + nap) % 7]
    return hetnapja

datumok=["2010.01.01","2011.01.01","2012.01.01","2013.01.01","2014.01.01","2015.01.01","2016.01.01","2017.01.01","2018.01.01","2019.01.01","2020.01.01","2021.01.01","2022.01.01","2023.01.01","2024.01.01","2025.01.01"]
for datum in datumok:
    print(f"{datum} : {hetnapja(datum)}")
