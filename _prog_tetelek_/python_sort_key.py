import random
adatok = []
for i in range(10):
  betu = chr(random.randint(65,91))
  pont = random.randint(0, 10)
  ertek = chr(random.randint(65,91)) + str(random.randint(0, 10))
  
  adat = {
    'nev': betu,
    'pont': pont,
    'ertek': ertek
  }
  adatok.append(adat)
print(adatok)

  
def rendez_nev(elem):
  # Név mező, mint rendezési kulcs
  return elem["nev"]

def rendez_pont(elem):
  # Pont mező, mint rendezési kulcs
  return elem["pont"]  
  
def rendez_ertek(elem):
  # Érték mezőben szereplő szám szerinti kulcs
  return int(elem['ertek'][1])
  
# Név szerint rendezve
adatok.sort(key=rendez_nev)
print("\nNév szerint rendezve")
for adat in adatok:
  print(adat)

# Pont szerint rendezve
adatok.sort(key=rendez_pont)
print("\nPontszám szerint rendezve")
for adat in adatok:
  print(adat)

# Kalkulált érték szerint rendezve
adatok.sort(key=rendez_ertek)
print("\nKalkulált érték szerint rendezve")
for adat in adatok:
  print(adat)
