abc_en = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
abc_hu = ['a','á','b','c','cs','d','dz','dzs','e','é','f','g','gy','h','i','í','j','k','l','ly','m','n','ny','o','ó','ö','ő','p','q','r','s','sz','t','ty','u','ú','ü','ű','v','w','x','y','z','zs']
# print(len(abc_en),len(abc_hu))
# szo = input("Betűk szóközzel elválasztva= ")
szo = "h ó k u sz p ó k u sz"
betuk = szo.split(' ')
for betu in betuk:
    print(betu,abc_hu.index(betu)+1)

