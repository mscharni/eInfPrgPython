import random
def listGenInt(n, range_from, range_to):
    _list = []
    if range_from > range_to:
        range_from, range_to = range_to, range_from
    for _i in range(0,n):
        _list.append(random.randint(range_from, range_to))
    return _list

def listGenInt2(n, range_from, range_to):
    if range_from > range_to:
        range_from, range_to = range_to, range_from
    return [random.randint(range_from, range_to) for i in range(0,n)]


def listGenChar(n):
    _list = []
    for _i in range(0,n):
        _list.append(chr(random.randint(32, 126)))
    return _list

def listGenChar2(n):
    return [chr(random.randint(32, 126)) for _i in range(0,n)]

def listGenLetter(n, caps = True):
    _letters = ["AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ", "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"]
    # feltételes értékadás, case értéke 0 lesz, ha caps értéke true, különben 1
    case = 0 if caps else 1
    _list = []
    for _i in range(0,n):
        _list.append(random.choice(_letters[case]))
    return _list
    

def listGenLetter2(n, caps = True):
    _letters = ["aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz", "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ"]
    #kihasználjuk, hogy a True = 1 és False = 0
    return [random.choice(_letters[int(caps)]) for _i in range(0,n)]
