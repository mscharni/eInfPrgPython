import math
def solution(a,b,c):
    try:
        return [(-b+math.sqrt(b**2 - 4*a*c))/(2*a), (-b-math.sqrt(b**2 - 4*a*c))/(2*a)]
    except BaseException as e:
        return type(e)



a = 1
b = 1
c = 1
print(solution(a,b,c))
