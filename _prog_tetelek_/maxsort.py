# maximum kiválasztásos rendezés
def max_sort(lista):
    # a végétől az eleje felé rendre végigmegyünk az összes elemen
    for i in range(len(lista)-1,0,-1):
        # felttesszük, hogy az aktuális rész-lista legutolsó eleme a rész-lista maximuma  
        maxi = i
        # végigmegyünk a rész-lista összes elemén és megkeressük a maximumot
        for j in range(0, i-1):
            # ha az aktuális maximum elemnél találunk nagyobbat, megjegyezzük az indexét
            if lista[maxi] < lista[j]:
                maxi = j
        # felcseréljük a tervezett maximum elemet a tényleges maximum elemmel (ha a kettő ugyanaz, akkor is)
        cs = lista[maxi]
        lista[maxi] = lista[i]
        lista[i] = cs

lista=[63,54,33,45,23,99,43,10,35,87]
print(f"Rendezetlen lista = {lista}")
max_sort(lista)
print(f"Rendezett lista   = {lista}")
