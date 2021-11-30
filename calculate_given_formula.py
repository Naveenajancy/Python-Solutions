from math import sqrt

C, H = 50, 30
#values = ''
def calculate(D):
    return sqrt((2*C*D)/H)


#for x in input().split(','):
    #out = calculate(int(x))
    #print(f" sqrt: {out}")
values = ','.join(str(int(calculate(int(x)))) for x in input().split(','))

print(f"Values: {values} ")
#for i in values:
 #  print(','.join(i))


#print(f"{values}")




