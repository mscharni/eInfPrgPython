def opm2mp_1(o, p, m) -> int:
    ido = o*3600 + p*60+m
    return ido

def opm2mp_2(*args) -> int:
    if len(args) == 1:
        m = args[0]
        p = 0
        o = 0
    elif len(args) == 2:
        m = args[0]
        p = args[1]
        o= 0
    elif len(args) == 3:
        m = args[0]
        p = args[1]
        o = args[2]
    else:
        m = 0
        p = 0
        o = 0
    ido = o*3600 + p*60+m
    return ido

def opm2mp_3(time) -> int:
    o = time[0]
    p = time[1]
    m = time[2]
    ido = o*3600 + p*60+m
    return ido

def opm2mp_4(**time) -> int:
    o = time["ora"]
    p = time["perc"]
    m = time["mperc"]
    ido = o*3600 + p*60+m
    return ido

# variables
print(opm2mp_1(1, 2, 3))

# variables
print(opm2mp_2(3))
print(opm2mp_2(3, 2))
print(opm2mp_2(3, 2, 1))

# List
print(opm2mp_3([1, 2, 3]))
# tuple
print(opm2mp_3((1, 2, 3)))

# dictionary
print(opm2mp_4(ora = 1, perc = 2, mperc=3))