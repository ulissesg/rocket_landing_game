import math
''' float float float -> (float, float) ou float ou false'''
def bhaskara(a,b,c):
    delta = b**2-4*a*c
    if delta < 0:
        return False
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        return (x1, x2)

#chamando:
resultado = bhaskara(1,5,3)
print(resultado)

'''
x**2 +2x+3 =0
2x**2+ 2x+3=0
3x**2+ 2x += 0
...

'''
for i in range(1,1001):
    resultado = bhaskara(2,i,3)
    print(resultado)
    
