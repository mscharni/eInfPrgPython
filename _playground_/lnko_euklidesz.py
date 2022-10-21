# függvény deklarációja
# a függvény neve: 'lnko', így tudunk rá hivatkozni
# a függvény paraméterei az 'a' és 'b' változók, amelyek a függvény meghívásakor veszik fel az átadott értéket
def lnko(a,b):
  # megcseréljük a két számot, ha a 'a' kisebb, mint a 'b'
  if a < b:
    a, b = kisebb, nagyobb
  # addig fut a ciklus, míg a maradék értéke nulla nem lesz (másképpen: addig fut, amíg még nemnulla a maradék)
  while a % b != 0:
    # a nagyobbik érték legyen egyenlő a kisebbik értékkel, a kisebbik érték pedig legyen egyenlő a maradékkal
    a, b = b, a % b
  # ciklus vége
  # a ciklusból kilépve megkapjuk a legnagyobb közös osztót (a kisebbik szám) és visszaadjuk a függvényt meghívó programrésznek
  return b
# függvény deklarációs rész vége

# megadjuk a két számot, amelynek a legnagyobb közös osztóját keressük
nagyobb = int(input(f"Egyik szám:"))
kisebb = int(input(f"Másik szám:"))
# a kiiratáson belül meghívjuk az lnko függvényünket, ami visszaadja értékként a legnagyobb közös osztót, s az jelenik meg
print(f"A {nagyobb} és {kisebb} legnagyobb közös osztója: {lnko(nagyobb, kisebb)}")
