def hetnapja(datum):
    _datum = datum.split(".")
    ev = int(_datum[0])
    ho = int(_datum[1])
    nap = int(_datum[2])
    napok = ['v', 'h', 'k', 'sze', 'cs', 'p', 'szo']
    honapok = [0, 3, 2, 5, 1, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev = ev - 1
    hetnapja = napok[(ev + ev//4 - ev//100 + ev//400 + honapok[ho-1] + nap) % 7]
    return hetnapja

def hetnapja2(datum):
    _datum = datum.split(".")
    ev = int(_datum[0])
    ho = int(_datum[1])
    nap = int(_datum[2])
    napok = ['h', 'k', 'sze', 'cs', 'p', 'szo', 'v']
    honapok = [-1, 2, 2, 5, 1, 3, 5, 1, 4, 6, 2, 4]
    hetnapja = napok[(ev + ev//4 - ev//100 + ev//400 + honapok[ho-1] ) % 7]
    return hetnapja

def hetnapja3(datum):
    _datum = datum.split(".")
    ev = int(_datum[0])
    ho = int(_datum[1])
    nap = int(_datum[2])
    napok = ['h', 'k', 'sze', 'cs', 'p', 'szo', 'v']
    honapok = [0, 3, 3, 6, 2, 4, 6, 2, 5, 7, 3, 5]
    hetnapja = napok[(ev + ev//4 - ev//100 + ev//400 + honapok[ho-1] + nap -2) % 7]
    return hetnapja

datumok=["2022.01.01","2022.02.01","2022.03.01","2022.04.01","2022.05.01","2022.06.01","2022.07.01","2022.08.01","2022.09.01","2022.10.01","2022.11.01","2022.12.01"]

datumok=["2010.01.01","2011.01.01","2012.01.01","2013.01.01","2014.01.01","2015.01.01","2016.01.01","2017.01.01","2018.01.01","2019.01.01","2020.01.01","2021.01.01","2022.01.01","2023.01.01","2024.01.01","2025.01.01"]
for datum in datumok:
    print(f"{datum} : {hetnapja(datum)} - {hetnapja2(datum)} - {hetnapja3(datum)}")
