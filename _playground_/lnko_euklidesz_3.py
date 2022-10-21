# megadjuk a két számot, amelynek a legnagyobb közös osztóját keressük
# példa számpárok
# [[299,221], [189,161], [190,150], [442342, 24234], [74,32], [210,78], [402,123]]
nagyobb = int(input(f"Egyik szám:"))
kisebb = int(input(f"Másik szám:"))

# letároljuk két segédváltozóba a két számot úgy, hogy közben 
# megcseréljük a két számot, ha a 'nagyobb' kisebb, mint a 'kisebb' 
if nagyobb < kisebb:
  a, b = kisebb, nagyobb
else:
  a, b = nagyobb, kisebb

# lnko(a,b)=ax+by, azaz a legnagyobb közös osztó kifejezhető a két szám lineáris kombinációjaként

r =[a,b]        # Az eredeti számok és a maradékok sorozata
q = [0,a//b]    # egész osztás eredménye
x = [1,0]       # segédvektor az 'a' együtthatójának meghatározásához
y = [0,1]       # segédvektor a 'b' együtthatójának meghatározásához

i = 2           # következő lépés sorszáma
print(f"N\tR\tQ\tX\tY")
print(f"{0}\t{r[0]}\t{q[0]}\t{x[0]}\t{y[0]}")

# addig fut a ciklus, míg a maradék értéke nulla nem lesz (másképpen: addig fut, amíg még nemnulla a maradék)
while r[i-1] != 0:
    r.append(r[i-2]-q[i-1]*r[i-1])
    x.append(x[i-1]*q[i-1]+x[i-2])
    y.append(y[i-1]*q[i-1]+y[i-2])
    if r[i] != 0:
        q.append(r[i-1]//r[i])
    else:
        q.append(0)
    print(f"{i-1}.\t{r[i-1]}\t{q[i-1]}\t{x[i-1]}\t{y[i-1]}")
    i= i+1
    
# letároljuk külön az lnko-t
lnko = r[i-2]
# kiszámoljuk az együtthatókat a megfelelő előjellel együtt
x = (-1)**(i-2)*x[i-2]
y = (-1)**(i-1)*y[i-2]
# kiiratjuk az eredményt
print(f"LNKO({a},{b}) = {lnko} = {x}*{a} + {y}*{b} (= {x*a + y*b})")          
