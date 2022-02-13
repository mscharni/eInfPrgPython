# Shell rendezés
def shell_rendezes(lista):
    gap = 1
    n = len(lista)
    while gap*2 <= n:
        gap *= 2
    gap = gap - 1
    while gap > 0:
        i = 0
        while i <= gap and i + gap < n:
            j = i + gap
            while j < n:
                elem = lista[j]
                index = j - gap
                while index > -1 and elem < lista[index]:
                    lista[index + gap] = lista[index]
                    index = index - gap
                lista[index + gap] = elem
                j += gap
            i += 1
        gap = gap // 2
    
lista=[63,54,33,45,23,99,43,10,35,87]
print(f"Rendezetlen lista = {lista}")
shell_rendezes(lista)
print(f"Rendezett lista   = {lista}")
