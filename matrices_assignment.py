#reading the matrix and making the values integer
with open('maths.txt') as f:
    matrix1=[]
    a=f.read().splitlines()
for i in a:
    split1=i.split(" ")
    matrix1.append(split1)

for i in matrix1:
    for j in range(len(i)):
        i[j]=float(i[j])

#rref of the matrix
matrix1=sorted(matrix1,reverse=True)
print("Given Matrix:",matrix1)
print()

from sympy import * 
m1 = Matrix(matrix1)
rref,pivots = m1.rref()

matrix2=rref.tolist()

#parametric form
columns=[]
for i in range(len(matrix2[0])):
    col=[]
    for j in range(len(matrix2)):
        col.append(round(matrix2[j][i],2))
    columns.append(col)
print("RREF:",columns)
print()

indices=[]
pivots=[]
for i in columns:
    if 1 in i:
        if 0 in i:
            ind=columns.index(i)
            indices.append(ind)
            pivots.append(i)
#print(pivots)
#print(indices)

not_indices=[]
for i in range(len(columns)):
    if i not in indices:
        not_indices.append(i)

nonpivot = []
for i in columns:
    if i in pivots:
        pass
    else:
        nonpivot.append(i)
#print(empty)

matrix4=[]
for i in range(len(nonpivot)):
    empty=[]
    for m in range(len(columns)):
        empty.append(0)
    for j in range(len(indices)):
        empty[indices[j]] = (-nonpivot[i][j])
    matrix4.append(empty)
#print(matrix4)

a=0
for i in range(len(columns)):
    if i not in indices:
        matrix4[a][i]=1
        a+=1

#rounding off
for i in matrix4:
    for j in range(len(i)):
        a = str(i[j]).split('.')
        if len(a) > 1:
            if len(a[1])>2:
               i[j] = round(i[j])
        else:
            i[j] = round(i[j],2)

#solution 
print("Solution:", end=" ")
for i in range(len(matrix4)):
    print("x"+str(not_indices[i]), matrix4[i], "+", end=" ")
print()

print()
for i in matrix4:
        for j in i:
                print(j,end='\t')
        print()
