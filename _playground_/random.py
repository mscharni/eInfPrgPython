import random
a = [0,1,2,3,4,5,6,7,8,9]
random.seed(1234)
b = a.copy()
random.shuffle(b)
print(a,b)
