import math
x = 0
h = 1
dx=1
qx=0.1
delta=1.0e-38
epsz=1.0e-200
llim_1=math.sin(x-dx*dx)/(x-dx*dx)
llim_2=math.sin(x-dx)/(x-dx)
print(x-dx,llim_1,llim_2,)
while dx > delta:
    print(x-dx,llim_1,llim_2)
    llim_1=math.sin(x-dx*dx)/(x-dx*dx)
    llim_2=math.sin(x-dx)/(x-dx)
    dx*=qx
print(delta, epsz)
