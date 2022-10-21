# megadjuk a két számot, amelynek a legnagyobb közös osztóját keressük
nagyobb = int(input(f"Egyik szám:"))
kisebb = int(input(f"Másik szám:"))
# letároljuk két segédváltozóba a két számot úgy, hogy közben 
# megcseréljük a két számot, ha a 'nagyobb' kisebb, mint a 'kisebb' 
if nagyobb < kisebb:
  a, b = kisebb, nagyobb
else:
  a, b = nagyobb, kisebb
# addig fut a ciklus, míg a maradék értéke nulla nem lesz (másképpen: addig fut, amíg még nemnulla a maradék)
while a % b != 0:
  # a nagyobbik érték legyen egyenlő a kisebbik értékkel, a kisebbik érték pedig legyen egyenlő a maradékkal
  a, b = b, a % b

# kiiratjuk az eredeti két számot és a legnagyobb közös osztójukat, ami a legutolsó nemnulla maradék
print(f"A {nagyobb} és {kisebb} legnagyobb közös osztója: {b}")
