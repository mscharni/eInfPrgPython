# modul importálása
import random

         #01234567890123
# text = "indul a GÖRRÖG GÖRÖG GÖRÖG aludni"
# print(text.replace('ö', 'o'))
# print(" ".join(text))
# print("-".join(['a', 'b']))
# print(text.upper())
# print(text.lower())
# print(text.count('a'))
# print("x".join(text).upper().count('X'))
# print(text.find('Ö'))
# print(text.find('Ö')+text[text.find('Ö')+1:].find('Ö')+1) # második 'Ö'

# maganhangzo = ['a', 'e', 'ö', 'u', 'i']
# print(maganhangzo[0])
# print(maganhangzo[0:2])
# print(maganhangzo[2:])
# 
# gorog = list(text)
# print(gorog)
# 
# gorog = text.split(" ")
# print(gorog)
# gorog = list(text.split(" "))
# print(gorog)

# egydimenziós tömb (nested list)
veletlenek = [random.randint(0,10) for i in range(20)]
print(veletlenek)
print(8 in veletlenek)
if 8 in veletlenek:
    print(veletlenek.index(8))
print(min(veletlenek))
print(max(veletlenek))
rendezett = veletlenek.copy()
rendezett.sort()
print(f"rendezett {rendezett}")
print(f"veletlenek {veletlenek}")


# kétdimenziós tömb (nested list)
# A = [0,-4]
# B = [1,2]
# C = [-1,3]
# 
# koord = [A, B, C]
# print(koord)
# print(koord[1][1]) # B_y


# klasszikus módszer
# matrix = []
# for i in range(10):
#     veletlenek = []
#     for j in range(3):
#         veletlenek.append(random.randint(0,100))
#     matrix.append(veletlenek)
# print(matrix)

# 'pythonos' módszer
# matrix = [[random.randint(0,100) for j in range(3)] for i in range(10)]
# print(matrix)

# szótár
# koord = {'X':2,'Y':3}
# print(koord)
# print(koord['X'])
