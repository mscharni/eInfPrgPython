f = [0,1]
for i in range(1,30):
    f.append(f[i] + f[i-1])
print(f)    
