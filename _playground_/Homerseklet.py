def c2f(_c) -> float:
    _f = _c * 9 / 5 + 32
    return _f


def f2c(_f) -> float:
    _c = (_f - 32) * 5 / 9
    return _c


def hovalto(fok, mod = "C") -> float:
    if mod == "F":
        _h = (fok - 32) * 5 / 9
    else:
        _h = (fok - 32) * 5 / 9
    return _h


# Celsius to Fahrenheit
# c = float(input("C°= "))
# print(f"{c}°C = {c2f(c):.2f}°F")

# Fahrenheit to Celsius
# f = float(input("F°= "))
# print(f"{f}°F = {f2c(f):.2f}°C")

# 0-100 Celsius to Fahrenheit
# print("Celsius to Fahrenheit")
# for c in range(0, 101):
#     print(f"{c}°C = {c2f(c):.2f}°F")

# 0-100 Fahrenheit to Celsius
# print("Fahrenheit to Celsius")
# for f in range(0, 101):
#     print(f"{f}°F = {f2c(f):.2f}°C")

# Hőváltó
fok = float(input("fok = "))
mod = ""
print("")
print("C: °F --> °C | F: °C --> °F")
while mod != "C" and mod !="F":
    mod = input("Adja meg az átváltás módját [C|F]:").upper()

print(f"{fok} = {hovalto(fok, mod):.2f}")
