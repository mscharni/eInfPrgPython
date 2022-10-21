import math  # matematikai függvényeket tartalmazó programkönyvtár betöltése
# Megadjuk a nullára redukált másodfokú egyenlet együtthatóit
a = 1   # másodfokú tag együtthatója
b = 3  # elsőfokú tag együtthatója
c = 2   # konstans tag
d = b*b - 4*a*c   # diszkrimináns
print(d)
# egyik gyök kiszámolása
x1 = (-b + math.sqrt(d))/(2*a)
# másik gyök kiszámolása
x2 = (-b - math.sqrt(d))/(2*a)

print(f"x1 = {x1}, x2={x2}")
