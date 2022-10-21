import math
v = input("Átfogót, vagy befogót akar számolni? 'a'/bármi: ")
if v == 'a':
  print("Adja meg a derékszögű háromszög két befogóját!")
  a = float(input("Egyik befogó = "))
  b = float(input("Másik befogó = "))
  c = math.sqrt(a*a + b*b)
  print(f"Átfogó = {c:.2f}")
else:
  import math
  print("Adja meg a derékszögű háromszög átfogóját és egyik befogóját!")
  c = float(input("Átfogó="))
  a = float(input("Egyik befogó="))
  b = math.sqrt(c*c - a*a)
  print(f"Másik befogó = {b:.2f}")
