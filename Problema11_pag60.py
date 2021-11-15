A={'A','B','C','D'}
A1={i for i in A if i=='A'}
A2={i for i in A if i=='B'}
A3={i for i in A if i=='C'}
A4={i for i in A if i=='D'}
A5={i for i in A if i<'C'}
A6={i for i in A if i!='B' and i!='D'}
A7={i for i in A if i!='B' and i!='C'}
A8={i for i in A if i>'A' and i<'D'}
A9={i for i in A if i!='A' and i!='C'}
A10={i for i in A if i>'B'}
A11={i for i in A if i<'D'}
A12={i for i in A if i!='C'}
A13={i for i in A if i!='B'}
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)
print(A7)
print(A8)
print(A9)
print(A10)
print(A11)
print(A12)
print(A13)