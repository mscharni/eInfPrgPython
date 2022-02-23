import math
# sample 1
firstname = "nick"
lastname = "nolTE"

fullname = lambda fname, lname: f"{fname.strip().title()} {lname.strip().title()}"

print(fullname(firstname, lastname))

# sample 2
a = 1
b = 2
c = 1

solution = lambda a, b, c: [(-b+math.sqrt(b**2 - 4*a*c))/(2*a), (-b-math.sqrt(b**2 - 4*a*c))/(2*a)]
print(solution(a,b,c))


