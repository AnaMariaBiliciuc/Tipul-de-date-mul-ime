A=set(input('Introduceti elementele multimii A: '))
B=set(input('Introduceti elementele multimii B: '))
if  isinstance(A,int) :
    print('int')
if isinstance(B,int) :
    print('int')
print('Reuniunea multimilor A si B: ',A.union(B))
print('Intersectia multimilor A si B: ',A.intersection(B))
print('Diferenta multimii A si B: ',A.difference(B))
print('Diferenta multimii B si A: ',B.difference(A))