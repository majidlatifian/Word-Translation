n = int(input())
dehkhoda = {}
for i in range(0,n):
    a = input().split()
    for j in range(1,len(a)):
        dehkhoda[a[j]] = a[0]

nahaie = []
jomle = input().split()
for k in range(0,len(jomle)):
    if jomle[k] in dehkhoda.keys():
        nahaie.append(dehkhoda[jomle[k]])
    else:
        nahaie.append(jomle[k])

tarjome = ''
for ozv in nahaie:
    tarjome += ozv + ' '


print (tarjome)