A={1 , 2 , 3 , 4}
from itertools import combinations
A1=set(combinations(A,1))
print('Submultimile formate dintr-un singur element: ',A1)
A2=set(combinations(A,2))
print('Submultimile formate din 2 elemente: ', A2)
A3=set(combinations(A,3))
print('Submultimile formate din 3 elemente: ', A3)
A4=set(combinations(A,4))
print('Submultimile formate din 4 elemente: ',A4)