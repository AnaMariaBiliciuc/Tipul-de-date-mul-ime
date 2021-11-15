A=set(input('Introduceti elementele multimii A: '))
B=set(input('Introduceti elementele multimii B: '))
a=0
b=0
for i in A :
    if i.islower() :
        a+=1 
for i in B :
    if i.islower() :
        b+=1
if (a==0) and (b==0):
    print('Reuniunea multimilor A si B: ',A.union(B))
    print('Intersectia multimilor A si B: ',A.intersection(B))
    print('Diferenta multimii A si B: ',A.difference(B))
    print('Diferenta multimii B si A: ',B.difference(A))
else :
    print('Introduceti o alta multime')
