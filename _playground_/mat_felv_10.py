for a in range(-200,200):
    for b in range(-200,200):
        for c in range(-200,200):
            szum = a+b+c
            if szum == 103:
                a2 = a+2
                b2 = b*2
                c2 = c/2
                szum2 = a2 + b2 + c2
                if szum == szum2:
                    print(f"{a}+{b}+{c}={szum} és {a2}+{b2}+{c2}={szum2}")
    
