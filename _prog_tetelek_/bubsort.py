# buborékos rendezés
def bub_sort(lista):
    # végigmegyük az összes elemen
    for i in range(0, len(lista) - 1):
        # végigmegyünk a még nem rendezett elemeken (fokozatosan egyre csökken)
        for j in range(1, len(lista)-i):
            # összehasonlítjuk az egymás mellett lévő két elemet
            if lista[j - 1] > lista[j]:
                # ha rossz sorrendben állnak, akkor megcseréljük őket
                cs = lista[j]
                lista[j] = lista[j - 1]
                lista[j - 1] = cs

lista=[63,54,33,45,23,99,43,10,35,87]
print(f"Rendezetlen lista = {lista}")
bub_sort(lista)
print(f"Rendezett lista   = {lista}")
